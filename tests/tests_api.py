from src.main import obter_cotacao_dolar

def test_api_cotacao():
    cotacao = obter_cotacao_dolar()
    assert cotacao is not None
    assert cotacao > 0