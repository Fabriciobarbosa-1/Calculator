import math


def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicacao(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def divisao(a, b):
    """Retorna a divisão de dois números. Levanta erro se b for zero."""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    return a / b


def potenciacao(base, expoente):
    """Retorna a base elevada ao expoente."""
    return base ** expoente


def raiz_quadrada(numero):
    """Retorna a raiz quadrada do número."""
    if numero < 0:
        raise ValueError("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(numero)


def logaritmo(numero, base=10):
    """Retorna o logaritmo de um número na base especificada (padrão: base 10)."""
    if numero <= 0:
        raise ValueError("Erro: O logaritmo só é definido para números positivos.")
    return math.log(numero, base)


def exibir_menu():
    """Exibe o menu de opções da calculadora."""
    print("\nCalculadora")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Logaritmo")
    print("0. Sair")


def main():
    """Função principal que executa a calculadora."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando a calculadora...")
            break

        if opcao in ["1", "2", "3", "4", "5"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            operacoes = {
                "1": soma,
                "2": subtracao,
                "3": multiplicacao,
                "4": divisao,
                "5": potenciacao,
            }

            try:
                resultado = operacoes[opcao](num1, num2)
                print(f"Resultado: {resultado}")
            except ValueError as erro:
                print(erro)

        elif opcao in ["6", "7"]:
            num = float(input("Digite o número: "))

            if opcao == "6":
                try:
                    print(f"Resultado: {raiz_quadrada(num)}")
                except ValueError as erro:
                    print(erro)

            elif opcao == "7":
                base = float(input("Digite a base do logaritmo (padrão: 10): ") or 10)
                try:
                    print(f"Resultado: {logaritmo(num, base)}")
                except ValueError as erro:
                    print(erro)

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()