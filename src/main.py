gastos = []

def adicionar_gasto(valor, descricao):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    gastos.append({"valor": valor, "descricao": descricao})

def listar_gastos():
    return gastos

def total_gastos():
    return sum(g["valor"] for g in gastos)

def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Ver total")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            try:
                valor = float(input("Valor: "))
                descricao = input("Descrição: ")
                adicionar_gasto(valor, descricao)
                print("Gasto adicionado!")
            except ValueError:
                print("Valor inválido!")

        elif opcao == "2":
            for g in listar_gastos():
                print(f"{g['descricao']} - R${g['valor']}")

        elif opcao == "3":
            print(f"Total: R${total_gastos()}")

        elif opcao == "4":
            break

if __name__ == "__main__":
    menu()