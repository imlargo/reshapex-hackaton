from streamlit.testing.v1 import AppTest


def test_streamlit_app_starts_without_provider_or_sources() -> None:
    app = AppTest.from_file("app.py", default_timeout=15).run()

    assert not app.exception
    assert app.title[0].value == "Turn source material into a defensible next move."
    assert any("Provider ready" in item.value for item in app.success) or any(
        "not configured" in item.value for item in app.error
    )
    assert app.button[0].label == "Run grounded analysis →"
