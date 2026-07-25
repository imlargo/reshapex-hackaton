from __future__ import annotations

import streamlit as st

from .config import get_settings
from .ingest import records_from_uploads
from .provider import create_deepseek_model
from .runner import AgentRunError, AgentRunner
from .tools import EvidenceStore, ToolRegistry


def render_app() -> None:
    st.set_page_config(
        page_title="AgentSprint • Evidence Decision",
        page_icon="◆",
        layout="wide",
    )
    _styles()
    settings = get_settings()

    st.markdown('<p class="eyebrow">AGENTSPRINT · GROUNDED DECISION</p>', unsafe_allow_html=True)
    st.title("Turn source material into a defensible next move.")
    st.caption(
        "One bounded agent. Typed tools. Every material recommendation tied to visible evidence."
    )

    with st.sidebar:
        st.subheader("Run control")
        if settings.provider_is_configured:
            st.success(f"DeepSeek ready · {settings.llm_model}")
        else:
            st.error("DeepSeek key not configured")
            st.code("Copy-Item .env.example .env\n# then set LLM_API_KEY", language="powershell")
        st.caption(
            f"Limits · {settings.agent_max_steps} steps · "
            f"{settings.agent_max_retries} repair · "
            f"{settings.tool_timeout_seconds:g}s/tool"
        )
        st.divider()
        st.subheader("Evidence")
        uploaded = st.file_uploader(
            "Upload source files",
            type=["txt", "md", "csv", "json"],
            accept_multiple_files=True,
            help="Raw files remain in memory; chunks receive stable evidence IDs for this run.",
        )
        st.caption("Accepted: UTF-8 TXT, Markdown, CSV, JSON")

    records = []
    source_error = ""
    if uploaded:
        try:
            records = records_from_uploads([(item.name, item.getvalue()) for item in uploaded])
        except ValueError as exc:
            source_error = str(exc)
            st.error(source_error)

    left, right = st.columns([1.65, 1], gap="large")
    with left:
        st.markdown("### Decision request")
        request = st.text_area(
            "What grounded recommendation or action should the agent produce?",
            height=180,
            placeholder=(
                "Example: Based only on the uploaded evidence, which option should we choose, "
                "what risk remains, and what should happen next?"
            ),
            label_visibility="collapsed",
        )
        run_clicked = st.button(
            "Run grounded analysis →",
            type="primary",
            use_container_width=True,
            disabled=bool(source_error),
        )
    with right:
        st.markdown("### Evidence readiness")
        st.metric("Sources loaded", len(uploaded or []))
        st.metric("Evidence chunks", len(records))
        if records:
            st.success("Evidence tool is ready.")
            with st.expander("Preview evidence IDs"):
                for record in records[:12]:
                    st.markdown(f"`{record.evidence_id}` · {record.title} · {record.location}")
        else:
            st.info("Upload at least one source before running the judge path.")

    if not run_clicked:
        _empty_state()
        return
    if not request.strip():
        st.warning("Enter a decision request.")
        return
    if not records:
        st.warning("Upload evidence so the agent has a real knowledge-tool path.")
        return
    if not settings.provider_is_configured:
        st.error("The real provider is not configured; no fake fallback was used.")
        return

    try:
        with st.status("Running bounded evidence loop…", expanded=True) as status:
            st.write("Connecting to the configured DeepSeek model")
            runner = AgentRunner(
                model=create_deepseek_model(settings),
                tools=ToolRegistry(EvidenceStore(records)),
                settings=settings,
            )
            outcome = runner.run(request)
            st.write("Validating structure and citation IDs")
            status.update(label="Grounded result ready", state="complete")
    except (AgentRunError, ValueError) as exc:
        st.error(str(exc))
        st.caption("The run stopped honestly; no synthetic answer was substituted.")
        return

    _render_result(outcome)


def _render_result(outcome: object) -> None:
    result = outcome.result
    trace = outcome.trace
    st.divider()
    grade_class = f"grade-{result.evidence_grade}"
    st.markdown(
        f'<div class="result-card"><span class="grade {grade_class}">'
        f"{result.evidence_grade.upper()} EVIDENCE</span>"
        f"<h2>{result.answer}</h2></div>",
        unsafe_allow_html=True,
    )

    metric_columns = st.columns(4)
    metric_columns[0].metric("Confidence", result.confidence.title())
    metric_columns[1].metric("Citations", len(result.citations))
    metric_columns[2].metric("Agent steps", trace.steps)
    metric_columns[3].metric("Latency", f"{trace.duration_ms / 1000:.1f}s")

    risk, action = st.columns(2, gap="large")
    with risk:
        st.markdown("#### Unresolved risk")
        st.write(result.unresolved_risk)
    with action:
        st.markdown("#### Next action")
        st.write(result.next_action)

    st.markdown("### Evidence behind the answer")
    evidence_by_id = {item.evidence_id: item for item in outcome.evidence}
    for citation in result.citations:
        with st.expander(f"{citation.evidence_id} · {citation.claim}", expanded=True):
            record = evidence_by_id.get(citation.evidence_id)
            if record:
                st.caption(f"{record.source_id} · {record.title} · {record.location}")
                st.write(record.content)
            else:
                st.warning("The cited evidence was not available in the accepted result.")

    with st.expander("Technical trace"):
        st.caption(
            f"Run {trace.run_id} · model {trace.model} · "
            f"{trace.usage.input_tokens} input / {trace.usage.output_tokens} output tokens"
        )
        for event in trace.events:
            duration = f" · {event.duration_ms} ms" if event.duration_ms is not None else ""
            st.markdown(f"**{event.kind.upper()} · {event.name}**{duration}  \n{event.summary}")


def _empty_state() -> None:
    st.divider()
    st.markdown("### The judge-visible contract")
    columns = st.columns(4)
    items = [
        ("01", "Grounded answer", "A direct recommendation or honest decline."),
        ("02", "Visible citations", "Exact evidence IDs and source previews."),
        ("03", "Bounded reliability", "Six steps, one repair, explicit timeouts."),
        ("04", "Operational next step", "Remaining risk and a concrete action."),
    ]
    for column, (number, title, body) in zip(columns, items, strict=True):
        with column:
            st.markdown(
                f'<div class="contract-card"><span>{number}</span><h4>{title}</h4>'
                f"<p>{body}</p></div>",
                unsafe_allow_html=True,
            )


def _styles() -> None:
    st.markdown(
        """
        <style>
          :root {
            --ink: #17201f;
            --muted: #64706e;
            --paper: #f6f3ec;
            --accent: #d85a3a;
            --teal: #0c7468;
          }
          .stApp {
            background:
              radial-gradient(circle at 85% 0%, rgba(12,116,104,.10), transparent 34rem),
              linear-gradient(180deg, #faf8f3 0%, var(--paper) 100%);
            color: var(--ink);
          }
          .block-container { max-width: 1180px; padding-top: 3rem; }
          .eyebrow {
            color: var(--teal); font-weight: 800; letter-spacing: .16em;
            font-size: .75rem; margin-bottom: .5rem;
          }
          h1 { font-size: clamp(2.2rem, 5vw, 4.6rem) !important; max-width: 950px; }
          .stButton > button[kind="primary"] {
            background: var(--ink); border: 1px solid var(--ink); min-height: 3.25rem;
            font-weight: 750;
          }
          .result-card {
            background: var(--ink); color: #fff; border-radius: 20px;
            padding: 2rem; box-shadow: 0 18px 55px rgba(23,32,31,.15);
          }
          .result-card h2 { margin: .8rem 0 0; line-height: 1.25; }
          .grade {
            display: inline-block; padding: .3rem .6rem; border-radius: 99px;
            font-size: .72rem; font-weight: 800; letter-spacing: .08em;
          }
          .grade-strong { background: #a7f3d0; color: #064e3b; }
          .grade-partial { background: #fde68a; color: #78350f; }
          .grade-insufficient { background: #fecaca; color: #7f1d1d; }
          .contract-card {
            min-height: 175px; background: rgba(255,255,255,.72); border: 1px solid #ded9cf;
            border-radius: 16px; padding: 1.25rem;
          }
          .contract-card span { color: var(--accent); font-weight: 850; }
          .contract-card h4 { margin: .75rem 0 .4rem; }
          .contract-card p { color: var(--muted); line-height: 1.5; }
        </style>
        """,
        unsafe_allow_html=True,
    )
