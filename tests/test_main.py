import pytest
from src.main import adicionar_gasto, total_gastos, listar_gastos, gastos

def setup_function():
    gastos.clear()

def test_adicionar_gasto():
    adicionar_gasto(10, "Lanche")
    assert len(listar_gastos()) == 1

def test_valor_negativo():
    with pytest.raises(ValueError):
        adicionar_gasto(-5, "Erro")

def test_total():
    adicionar_gasto(10, "A")
    adicionar_gasto(20, "B")
    assert total_gastos() == 30