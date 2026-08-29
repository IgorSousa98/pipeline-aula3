from src.app import build_status


def test_build_status():
    assert build_status() == "Pipeline CI/CD executado com sucesso!"

#Simulação do Cenário de Falha

#from src.app import build_status

#ef test_build_status():
    # Forcando falha para validar bloqueio do pipeline
    #assert build_status() == "Texto Incorreto Que Vai Falhar"

    