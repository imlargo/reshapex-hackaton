from streamlit.testing.v1 import AppTest

from semantic_demo import list_cases, simulate_case


def test_every_fixture_selects_its_expected_storage_and_algorithm() -> None:
    outcomes = [simulate_case(case.case_id) for case in list_cases()]

    assert {outcome.selected_plan.resolved_storage for outcome in outcomes} == {
        "vector",
        "relational",
        "simple_graph",
        "complex_graph",
    }
    assert all(
        outcome.selected_plan.resolved_storage == outcome.case.expected_storage
        for outcome in outcomes
    )
    assert {outcome.selected_plan.algorithm for outcome in outcomes} == {
        "tfidf_cosine",
        "sql_filter_bm25",
        "breadth_first_search",
        "personalized_pagerank",
    }


def test_complex_graph_is_gated_except_for_multihop_case() -> None:
    outcomes = [simulate_case(case.case_id) for case in list_cases()]

    for outcome in outcomes:
        complex_candidate = next(
            item
            for item in outcome.candidates
            if item.requested_storage == "complex_graph"
        )
        assert complex_candidate.eligible is (outcome.case.case_id == "nova-impact")


def test_demo_results_are_evidence_visible_and_honestly_limited() -> None:
    for case in list_cases():
        outcome = simulate_case(case.case_id)

        assert outcome.case.evidence
        assert outcome.case.caveat
        assert all(item.source_id.startswith("SRC-") for item in outcome.case.evidence)
        assert all(item.url.startswith("https://") for item in outcome.case.evidence)
        assert len(outcome.stages) == 6
        assert outcome.retrieved_evidence_ids
        assert outcome.plan_dump["plan_id"] == outcome.plan_id


def test_demo_app_starts_without_provider() -> None:
    app = AppTest.from_file("demo/semantic/app.py", default_timeout=15).run()

    assert not app.exception
    assert any("Convierte documentación técnica" in item.value for item in app.markdown)
    assert app.button[0].label == "Ejecutar agente semántico"


def test_demo_button_completes_the_agent_journey() -> None:
    app = AppTest.from_file("demo/semantic/app.py", default_timeout=15).run()
    app.button[0].click().run(timeout=15)

    assert not app.exception
    assert any("APROBADO PARA DEMO" in item.value for item in app.success)
    assert any("Conversación" in item.value for item in app.markdown)
