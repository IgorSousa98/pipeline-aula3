from src.app import build_status


def test_build_status():
    assert build_status() == "Pipeline CI/CD executado com sucesso!"
    