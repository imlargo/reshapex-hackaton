from __future__ import annotations

import html
import time

import streamlit as st

from .models import CandidatePlan, DemoCase, DemoOutcome
from .simulator import get_case, list_cases, simulate_case

STORAGE_ICONS = {
    "vector": "◌",
    "relational": "▦",
    "simple_graph": "⌘",
    "complex_graph": "✣",
}


def render_demo() -> None:
    st.set_page_config(
        page_title="Semantic Studio · Demo local",
        page_icon="◆",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    _styles()
    cases = list_cases()

    with st.sidebar:
        st.markdown(
            """
            <div class="side-brand">
              <div class="brand-mark">S</div>
              <div>
                <strong>SEMANTIC STUDIO</strong>
                <span>Knowledge compiler concept</span>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="live-pill">● SIMULACIÓN LOCAL</div>', unsafe_allow_html=True)
        st.caption("Sin DeepSeek · sin bases externas · corpus preparado")
        st.divider()
        st.markdown("#### Casos de ejemplo")
        selected_case_id = st.radio(
            "Selecciona un recorrido",
            options=[case.case_id for case in cases],
            format_func=lambda case_id: get_case(case_id).short_name,
            label_visibility="collapsed",
        )
        st.divider()
        st.markdown("#### Decisión adaptativa")
        st.caption(
            "El agente compara cuatro planes y asigna a cada uno un algoritmo de "
            "búsqueda. El grafo complejo solo se habilita si supera su gate."
        )
        for icon, label in [
            ("◌", "Vector · TF-IDF cosine"),
            ("▦", "Relacional · SQL filter + BM25"),
            ("⌘", "Grafo simple · breadth-first"),
            ("✣", "Grafo complejo · personalized PageRank"),
        ]:
            st.markdown(f'<div class="side-plan">{icon}<span>{label}</span></div>', True)
        st.divider()
        st.caption("Fuente del concepto · SRC-003—SRC-007 · commit 1e987e9")

    case = get_case(selected_case_id)
    _hero(case)
    _journey_input(case)

    run_clicked = st.button(
        "Ejecutar agente semántico",
        type="primary",
        use_container_width=True,
        key=f"run-{case.case_id}",
    )
    if run_clicked:
        outcome = simulate_case(case.case_id)
        _animate_agent(outcome)
        st.session_state["semantic_demo_outcome"] = outcome.model_dump(mode="json")

    stored_outcome = st.session_state.get("semantic_demo_outcome")
    if not stored_outcome:
        _journey_preview()
        return

    outcome = DemoOutcome.model_validate(stored_outcome)
    if outcome.case.case_id != case.case_id:
        st.info("Ejecuta este caso para generar su recorrido y resultado.")
        _journey_preview()
        return
    _render_outcome(outcome)


def _animate_agent(outcome: DemoOutcome) -> None:
    case = outcome.case
    plan = outcome.selected_plan
    comparison = " · ".join(
        f"{candidate.label}: {candidate.status}" for candidate in outcome.candidates
    )
    complex_candidate = next(
        candidate
        for candidate in outcome.candidates
        if candidate.requested_storage == "complex_graph"
    )
    complex_decision = (
        "El gate de grafo complejo se abre: hay densidad, ciclos y necesidad multi-salto."
        if complex_candidate.eligible
        else "El gate de grafo complejo permanece cerrado: su complejidad no está justificada."
    )
    decisions = [
        (
            "Objetivo aceptado",
            f"Prioridad detectada: {case.objective}",
        ),
        (
            "Corpus perfilado",
            (
                f"{case.document_count} fuentes · "
                f"{outcome.selection_signals['content_units']} unidades · "
                f"estructura {outcome.selection_signals['structured_ratio']:.0%} · "
                f"{outcome.selection_signals['relationships']} relaciones."
            ),
        ),
        (
            "Planes comparados",
            comparison,
        ),
        (
            "Gate de complejidad evaluado",
            complex_decision,
        ),
        (
            "Arquitectura decidida",
            (
                f"{plan.label} en modo automático · "
                f"plan {outcome.plan_id}."
            ),
        ),
        (
            "Algoritmo decidido",
            plan.algorithm,
        ),
        (
            "Resultado validado",
            (
                f"{len(case.evidence)} evidencias aceptadas · "
                f"límite conocido conservado · {outcome.validation_status}."
            ),
        ),
    ]

    st.markdown('<div class="section-label top-space">AGENTE · EJECUCIÓN EN VIVO</div>', True)
    with st.container(border=True):
        st.caption("AGENTE SEMÁNTICO")
        st.markdown("**Voy a diseñar la base antes de intentar responder.**")
        decision_feed = st.empty()
        progress = st.progress(0, text="Iniciando recorrido…")
        visible: list[str] = []
        for index, (title, detail) in enumerate(decisions, start=1):
            visible.append(
                f'<div class="agent-decision"><span>{index:02d}</span>'
                f"<div><strong>{html.escape(title)}</strong>"
                f"<p>{html.escape(detail)}</p></div></div>"
            )
            decision_feed.markdown(
                f'<div class="agent-feed">{"".join(visible)}</div>',
                unsafe_allow_html=True,
            )
            progress.progress(
                index / len(decisions),
                text=f"{title} · {index}/{len(decisions)}",
            )
            time.sleep(0.28)
        progress.empty()
        st.caption(
            "Decisiones operativas visibles de una simulación determinista; "
            "no se expone razonamiento interno ni se llama a un proveedor externo."
        )


def _hero(case: DemoCase) -> None:
    st.markdown(
        f"""
        <section class="hero">
          <div class="hero-copy">
            <div class="hero-kicker">CONCEPTO INTERACTIVO · EVIDENCIA REAL</div>
            <h1>Convierte documentación técnica<br>en una base que sabe <em>cómo buscar.</em></h1>
            <p>
              Un agente local simula el procesamiento semántico, compara arquitecturas
              y explica cada decisión antes de responder.
            </p>
          </div>
          <div class="case-ticket">
            <span>{html.escape(case.eyebrow)}</span>
            <strong>{html.escape(case.short_name)}</strong>
            <small>Recorrido preparado · reproducible</small>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _journey_input(case: DemoCase) -> None:
    st.markdown('<div class="section-label">01 · DEFINIR EL TRABAJO</div>', True)
    objective_column, corpus_column = st.columns([1.35, 1], gap="large")
    with objective_column:
        st.markdown("### ¿Qué debe lograr la base?")
        st.text_area(
            "Objetivo de uso",
            value=case.objective,
            height=116,
            disabled=True,
            label_visibility="collapsed",
            key=f"objective-{case.case_id}",
        )
        st.markdown('<div class="prompt-label">PREGUNTA DE VALIDACIÓN</div>', True)
        with st.container(border=True):
            st.caption("USUARIO")
            st.write(case.question)
    with corpus_column:
        st.markdown("### Corpus preparado")
        st.caption(case.description)
        for document in case.documents:
            st.markdown(
                f'<div class="document-row"><span>DOC</span>{html.escape(document)}</div>',
                unsafe_allow_html=True,
            )
        st.caption(
            f"{case.document_count} fuentes en el caso · "
            f"{case.simulated_chunks} unidades semánticas compiladas"
        )


def _journey_preview() -> None:
    st.markdown('<div class="section-label top-space">02 · RECORRIDO DEL AGENTE</div>', True)
    labels = [
        ("01", "Inventario"),
        ("02", "Extracción"),
        ("03", "Semántica"),
        ("04", "Selección"),
        ("05", "Índice"),
        ("06", "Validación"),
    ]
    markup = "".join(
        (
            f'<div class="preview-step"><b>{number}</b><span>{label}</span></div>'
            + ('<div class="preview-line"></div>' if index < len(labels) - 1 else "")
        )
        for index, (number, label) in enumerate(labels)
    )
    st.markdown(f'<div class="preview-journey">{markup}</div>', unsafe_allow_html=True)
    st.caption(
        "Ejecuta el agente para ver artefactos, elección de almacenamiento, "
        "algoritmo de búsqueda, respuesta y evidencia."
    )


def _render_outcome(outcome: DemoOutcome) -> None:
    case = outcome.case
    plan = outcome.selected_plan
    st.markdown('<div class="section-label top-space">02 · RECORRIDO COMPLETADO</div>', True)
    _stage_timeline(outcome)

    st.markdown('<div class="section-label top-space">03 · RESPUESTA DEL AGENTE</div>', True)
    response, decision = st.columns([1.3, 1], gap="large")
    with response:
        st.markdown("### Conversación")
        with st.container(border=True):
            st.caption("USUARIO")
            st.write(case.question)
        with st.container(border=True):
            st.caption("AGENTE SEMÁNTICO")
            st.write(case.answer)
            citation_tags = " ".join(f"`[{item.evidence_id}]`" for item in case.evidence)
            st.caption(f"Evidencia utilizada · {citation_tags}")
        st.warning(f"**Límite conocido:** {case.caveat}", icon="⚠️")
    with decision:
        st.markdown("### Decisión de arquitectura")
        st.markdown(
            f"""
            <div class="winner-card">
              <div class="winner-top">
                <span>{STORAGE_ICONS[plan.resolved_storage]}</span>
                <div>
                  <small>PLAN SELECCIONADO · MODO AUTOMÁTICO</small>
                  <h3>{html.escape(plan.label)}</h3>
                </div>
              </div>
              <div class="algorithm-label">ALGORITMO DE BÚSQUEDA</div>
              <strong>{html.escape(plan.algorithm)}</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write(case.selection_reason)
        metric_one, metric_two, metric_three = st.columns(3)
        metric_one.metric("Confianza", outcome.confidence.title())
        metric_two.metric("Entidades", outcome.selection_signals["entities"])
        metric_three.metric("Relaciones", outcome.selection_signals["relationships"])
        st.caption(
            f"Índice real · `{outcome.index_id}` · "
            f"{outcome.selection_signals['cycle_surplus']} ciclos excedentes"
        )

    decision_tab, knowledge_tab, evidence_tab, trace_tab = st.tabs(
        ["Comparación de planes", "Artefacto consultable", "Evidencia", "Trace técnico"]
    )
    with decision_tab:
        _candidate_comparison(outcome.candidates, plan)
    with knowledge_tab:
        _knowledge_artifact(outcome)
    with evidence_tab:
        _evidence(case)
    with trace_tab:
        _technical_trace(outcome)


def _stage_timeline(outcome: DemoOutcome) -> None:
    markup = "".join(
        f"""
        <div class="stage-card">
          <div class="stage-number">{stage.number:02d}</div>
          <div class="stage-check">✓</div>
          <strong>{html.escape(stage.name)}</strong>
          <p>{html.escape(stage.summary)}</p>
          <small>{html.escape(stage.artifact)}</small>
        </div>
        """
        for stage in outcome.stages
    )
    st.markdown(f'<div class="stage-grid">{markup}</div>', unsafe_allow_html=True)


def _candidate_comparison(
    candidates: list[CandidatePlan],
    selected_plan: CandidatePlan,
) -> None:
    st.markdown("#### Por qué este plan y no otro")
    st.caption(
        "Cada tarjeta se obtiene solicitando ese plan al AdaptiveRagCompiler. "
        "El core acepta la preferencia o la degrada mediante sus compuertas."
    )
    columns = st.columns(4, gap="small")
    by_storage = {candidate.requested_storage: candidate for candidate in candidates}
    storage_order = ["vector", "relational", "simple_graph", "complex_graph"]
    for column, storage in zip(columns, storage_order, strict=True):
        candidate = by_storage[storage]
        selected = candidate.status == "selected"
        css_class = "candidate-card selected" if selected else "candidate-card"
        state = (
            "SELECCIONADO"
            if selected
            else ("DISPONIBLE" if candidate.eligible else "DEGRADADO POR GATE")
        )
        with column:
            st.markdown(
                f"""
                <div class="{css_class}">
                  <span class="candidate-icon">
                    {STORAGE_ICONS[candidate.requested_storage]}
                  </span>
                  <small>{state}</small>
                  <h4>{html.escape(candidate.label)}</h4>
                  <div class="decision-value">
                    {html.escape(candidate.resolved_storage)}
                  </div>
                  <p>{html.escape(candidate.algorithm)}</p>
                  <em>{html.escape(candidate.gate_note)}</em>
                </div>
                """,
                unsafe_allow_html=True,
            )


def _knowledge_artifact(outcome: DemoOutcome) -> None:
    plan = outcome.selected_plan
    st.markdown(f"#### Vista consultable · {plan.label}")
    st.caption(
        f"El agente usaría **{plan.algorithm}** sobre este artefacto local preparado."
    )
    st.table(outcome.case.artifact_rows)


def _evidence(case: DemoCase) -> None:
    st.markdown("#### Evidencia detrás de la respuesta")
    st.caption("Los fragmentos provienen del corpus comprometido en `codex/semantic-processing`.")
    for evidence in case.evidence:
        with st.expander(
            f"{evidence.evidence_id} · {evidence.title}",
            expanded=True,
        ):
            st.caption(f"{evidence.source_id} · {evidence.location}")
            st.write(evidence.excerpt)
            st.markdown(f"**Sustenta:** {evidence.supports}")
            st.link_button("Abrir fuente original ↗", evidence.url)


def _technical_trace(outcome: DemoOutcome) -> None:
    st.markdown("#### Trace reproducible de la simulación")
    st.code(
        "\n".join(
            (
                f"[OK] stage={stage.number:02d} "
                f'name="{stage.name}" artifact="{stage.artifact}"'
            )
            for stage in outcome.stages
        )
        + (
            f'\n[OK] storage="{outcome.selected_plan.resolved_storage}" '
            f'algorithm="{outcome.selected_plan.algorithm}" '
            f'plan_id="{outcome.plan_id}" index_id="{outcome.index_id}"'
            f"\n[OK] evidence_ids="
            f"{','.join(outcome.retrieved_evidence_ids)}"
            "\n[INFO] mode=local_concept_simulation provider=none external_store=none"
        ),
        language="text",
    )
    st.markdown("##### `compiled.plan.model_dump()`")
    st.json(outcome.plan_dump)
    st.success(outcome.validation_status)


def _styles() -> None:
    st.markdown(
        """
        <style>
          @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
          :root {
            --ink: #11212f;
            --navy: #0b1d2a;
            --muted: #63717b;
            --line: #dce3e6;
            --paper: #f5f7f6;
            --white: #ffffff;
            --lime: #c7ff42;
            --teal: #21c7a8;
            --amber: #ffbd4a;
          }
          .stApp {
            color: var(--ink);
            background:
              radial-gradient(circle at 85% 2%, rgba(33,199,168,.12), transparent 24rem),
              linear-gradient(180deg, #fbfcfb 0%, var(--paper) 100%);
          }
          [data-testid="stSidebar"] {
            background: var(--navy);
            border-right: 1px solid rgba(255,255,255,.08);
          }
          [data-testid="stSidebar"] * { color: #edf5f3; }
          [data-testid="stSidebar"] .stCaptionContainer p { color: #9cb0b8; }
          [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,.12); }
          [data-testid="stSidebar"] [role="radiogroup"] label {
            border: 1px solid rgba(255,255,255,.12);
            border-radius: 12px;
            padding: .58rem .7rem;
            margin: .25rem 0;
            transition: all .15s ease;
          }
          [data-testid="stSidebar"] [role="radiogroup"] label:hover {
            border-color: var(--lime);
            background: rgba(199,255,66,.06);
          }
          .block-container { max-width: 1320px; padding: 2.2rem 3.2rem 5rem; }
          h1, h2, h3, h4 { font-family: "Space Grotesk", sans-serif !important; }
          p, label, span, small { font-family: "DM Sans", sans-serif; }
          .side-brand { display: flex; align-items: center; gap: .8rem; margin: .5rem 0 1rem; }
          .brand-mark {
            display: grid; place-items: center; width: 38px; height: 38px;
            background: var(--lime); color: var(--navy) !important; border-radius: 9px;
            font-family: "Space Grotesk"; font-weight: 800; font-size: 1.25rem;
          }
          .side-brand strong { display: block; letter-spacing: .08em; font-size: .86rem; }
          .side-brand span { display: block; color: #91a4ad !important; font-size: .72rem; }
          .live-pill {
            display: inline-flex; padding: .35rem .6rem; border-radius: 99px;
            background: rgba(33,199,168,.13); color: #60e6ca !important;
            font-size: .67rem; font-weight: 800; letter-spacing: .08em;
          }
          .side-plan {
            display: flex; align-items: center; gap: .65rem; padding: .45rem 0;
            color: var(--lime) !important;
          }
          .side-plan span { color: #c8d5d8 !important; font-size: .78rem; }
          .hero {
            position: relative; overflow: hidden; display: flex; justify-content: space-between;
            gap: 2rem; background: var(--navy); color: white; border-radius: 24px;
            padding: clamp(2rem, 4vw, 4.5rem); min-height: 360px;
            box-shadow: 0 24px 70px rgba(11,29,42,.16); margin-bottom: 2.2rem;
          }
          .hero::after {
            content: ""; position: absolute; width: 330px; height: 330px; right: -90px;
            top: -100px; border: 60px solid rgba(199,255,66,.08); border-radius: 50%;
          }
          .hero-copy { position: relative; z-index: 1; max-width: 910px; }
          .hero-kicker {
            color: var(--lime); font-size: .72rem; font-weight: 800;
            letter-spacing: .16em; margin-bottom: 1.2rem;
          }
          .hero h1 {
            color: white; font-size: clamp(2.15rem, 4.5vw, 4.5rem) !important;
            line-height: 1.02 !important; letter-spacing: -.055em; margin: 0 0 1.5rem;
          }
          .hero h1 em { color: var(--lime); font-style: normal; }
          .hero p { color: #bbcbcf; font-size: 1.05rem; max-width: 720px; line-height: 1.6; }
          .case-ticket {
            position: relative; z-index: 1; align-self: flex-end; min-width: 230px;
            border-left: 2px solid var(--lime); padding: .8rem 0 .8rem 1.1rem;
          }
          .case-ticket span, .case-ticket small {
            display: block; color: #91a6ad; font-size: .66rem;
          }
          .case-ticket strong { display: block; color: white; margin: .35rem 0; font-size: 1.1rem; }
          .section-label {
            color: #597078; font-size: .67rem; font-weight: 800;
            letter-spacing: .16em; margin-bottom: .7rem;
          }
          .top-space { margin-top: 2.8rem; }
          .prompt-label {
            color: #708087; font-size: .66rem; font-weight: 800;
            letter-spacing: .12em; margin: .9rem 0 .2rem;
          }
          .document-row {
            display: flex; align-items: center; gap: .65rem; padding: .65rem .8rem;
            margin: .42rem 0; background: white; border: 1px solid var(--line);
            border-radius: 10px; font-size: .82rem;
          }
          .document-row span {
            color: #52636a; background: #e9eff0; border-radius: 5px; padding: .2rem .35rem;
            font-size: .57rem; font-weight: 800; letter-spacing: .08em;
          }
          .stButton > button[kind="primary"] {
            min-height: 3.6rem; background: var(--navy); border: 1px solid var(--navy);
            border-radius: 12px; font-family: "Space Grotesk"; font-weight: 700;
            font-size: 1rem; box-shadow: 0 10px 30px rgba(11,29,42,.12);
          }
          .stButton > button[kind="primary"]:hover {
            color: var(--navy); background: var(--lime); border-color: var(--lime);
          }
          .preview-journey {
            display: flex; align-items: center; background: white; border: 1px solid var(--line);
            padding: 1.2rem; border-radius: 14px; overflow-x: auto;
          }
          .preview-step { min-width: 100px; text-align: center; }
          .preview-step b { display: block; color: var(--teal); font-size: .68rem; }
          .preview-step span { display: block; font-size: .78rem; font-weight: 700; }
          .preview-line { flex: 1; min-width: 22px; height: 1px; background: var(--line); }
          .stage-grid {
            display: grid; grid-template-columns: repeat(6, 1fr); gap: .65rem;
          }
          .stage-card {
            position: relative; min-height: 178px; background: white; border: 1px solid var(--line);
            border-radius: 14px; padding: 1rem; box-shadow: 0 8px 24px rgba(17,33,47,.04);
          }
          .stage-number { color: #8b999e; font-size: .65rem; font-weight: 800; }
          .stage-check {
            position: absolute; right: .8rem; top: .7rem; display: grid; place-items: center;
            width: 22px; height: 22px; border-radius: 50%; background: #dcfaef;
            color: #087e67; font-size: .72rem; font-weight: 900;
          }
          .stage-card strong { display: block; margin: 1.15rem 0 .45rem; font-size: .88rem; }
          .stage-card p { color: #586a71; font-size: .72rem; line-height: 1.4; min-height: 40px; }
          .stage-card small { color: #86959a; font-size: .62rem; line-height: 1.3; }
          .winner-card {
            background: var(--navy); color: white; border-radius: 16px; padding: 1.25rem;
            margin-bottom: 1rem; box-shadow: 0 14px 38px rgba(11,29,42,.13);
          }
          .winner-top { display: flex; gap: .8rem; align-items: center; margin-bottom: 1rem; }
          .winner-top > span {
            display: grid; place-items: center; width: 48px; height: 48px; border-radius: 12px;
            background: var(--lime); color: var(--navy); font-size: 1.45rem;
          }
          .winner-card small { color: #9fb1b7; font-size: .61rem; letter-spacing: .1em; }
          .winner-card h3 { color: white; margin: .1rem 0 0; }
          .algorithm-label {
            color: var(--lime); font-size: .59rem; font-weight: 800;
            letter-spacing: .12em; margin-bottom: .25rem;
          }
          .winner-card > strong { font-size: .84rem; }
          [data-testid="stChatMessage"] {
            background: white; border: 1px solid var(--line); border-radius: 14px;
            padding: .2rem .5rem;
          }
          .agent-feed { display: grid; gap: .42rem; margin-top: .8rem; }
          .agent-decision {
            display: flex; gap: .75rem; align-items: flex-start; padding: .68rem .75rem;
            border: 1px solid #dfe7e8; border-radius: 10px; background: #f8faf9;
            animation: agent-in .24s ease-out;
          }
          .agent-decision > span {
            display: grid; place-items: center; flex: 0 0 25px; height: 25px;
            border-radius: 50%; background: var(--navy); color: var(--lime);
            font-size: .58rem; font-weight: 800;
          }
          .agent-decision strong { display: block; font-size: .78rem; }
          .agent-decision p {
            color: #5c6e74; font-size: .7rem; line-height: 1.4; margin: .15rem 0 0;
          }
          @keyframes agent-in {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
          }
          .candidate-card {
            min-height: 280px; background: white; border: 1px solid var(--line);
            border-radius: 14px; padding: 1.1rem;
          }
          .candidate-card.selected {
            background: var(--navy); color: white; border-color: var(--navy);
            box-shadow: inset 0 4px 0 var(--lime);
          }
          .candidate-icon { font-size: 1.4rem; color: var(--teal); }
          .candidate-card small {
            display: block; margin-top: .8rem; color: #77898f; font-size: .58rem;
          }
          .candidate-card.selected small, .candidate-card.selected p,
          .candidate-card.selected em { color: #afc0c5; }
          .candidate-card.selected h4 { color: white; }
          .candidate-card h4 { margin: .25rem 0; }
          .candidate-card .decision-value {
            font-family: "Space Grotesk"; font-size: .85rem; font-weight: 700;
            color: var(--teal); margin: .7rem 0; overflow-wrap: anywhere;
          }
          .candidate-card.selected .decision-value { color: var(--lime); }
          .candidate-card p { color: #52656c; font-size: .72rem; min-height: 50px; }
          .candidate-card em {
            display: block; color: #86959a; font-size: .65rem;
            font-style: normal; line-height: 1.35;
          }
          [data-testid="stDataFrame"], [data-testid="stTable"] {
            background: white; border-radius: 12px; overflow: hidden;
          }
          @media (max-width: 1100px) {
            .stage-grid { grid-template-columns: repeat(3, 1fr); }
            .hero { flex-direction: column; }
          }
          @media (max-width: 700px) {
            .block-container { padding: 1.2rem 1rem 3rem; }
            .stage-grid { grid-template-columns: 1fr 1fr; }
            .hero { padding: 1.5rem; min-height: auto; }
          }
        </style>
        """,
        unsafe_allow_html=True,
    )
