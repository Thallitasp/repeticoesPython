# estruturas_repeticao.py


class AtividadeRepeticao:
    """
    Classe que encapsula as implementações da Atividade Prática 1
    sobre Estruturas de Repetição Básicas (while e for) em Python.
    """

    def __init__(self, saldo_inicial: float = 500.00):
        """
        Inicializa a instância da atividade com o saldo padrão do caixa eletrônico.

        Args:
            saldo_inicial (float): Valor inicial disponível na conta (padrão: R$ 500,00).
        """
        self.saldo = saldo_inicial

    # =========================================================================
    # PARTE 1: Loop While para Menus Interativos
    # =========================================================================
    def simular_caixa_eletronico(self) -> None:
        """
        Simula um caixa eletrônico interativo utilizando a estrutura 'while'.
        Permite consultar saldo, realizar saques validados e encerrar o sistema.
        """
        opcao = ""

        while opcao != "3":
            print("\n" + "=" * 42)
            print("            CAIXA ELETRÔNICO")
            print("=" * 42)
            print("1 - Verificar saldo")
            print("2 - Realizar saque")
            print("3 - Sair do sistema")
            print("-" * 42)
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                print(f"\n[Saldo] Seu saldo atual é: R$ {self.saldo:.2f}")

            elif opcao == "2":
                try:
                    entrada = input("Digite o valor que deseja sacar: R$ ").strip().replace(",", ".")
                    valor_saque = float(entrada)

                    if valor_saque <= 0:
                        print("\n[Erro] O valor do saque deve ser maior que zero.")
                    elif valor_saque <= self.saldo:
                        self.saldo -= valor_saque
                        print(f"\n[Sucesso] Saque de R$ {valor_saque:.2f} realizado!")
                        print(f"[Saldo] Novo saldo disponível: R$ {self.saldo:.2f}")
                    else:
                        print(f"\n[Negado] Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}")
                except ValueError:
                    print("\n[Erro] Entrada inválida! Digite um valor numérico.")

            elif opcao == "3":
                print("\nEncerrando o caixa eletrônico... Obrigado por utilizar nossos serviços!")

            else:
                print("\n[Erro] Opção inválida! Escolha 1, 2 ou 3.")

    # =========================================================================
    # PARTE 2: Padrões com Loop For
    # =========================================================================
    def exibir_quadrados_1_a_10(self) -> None:
        """
        Exibe os números inteiros de 1 a 10 e seus respectivos quadrados
        utilizando um loop 'for'.
        """
        print("\n" + "=" * 42)
        print("      NÚMEROS DE 1 A 10 E SEUS QUADRADOS")
        print("=" * 42)

        for numero in range(1, 11):
            quadrado = numero ** 2
            print(f"Número: {numero:02d} | Quadrado ({numero}²): {quadrado}")

    def exibir_quadrados_pares_1_a_10(self) -> None:
        """
        Exibe apenas os números pares entre 1 e 10 e seus respectivos quadrados
        utilizando o passo (step) do 'range' no loop 'for'.
        """
        print("\n" + "=" * 42)
        print("   NÚMEROS PARES DE 1 A 10 E SEUS QUADRADOS")
        print("=" * 42)

        for numero in range(2, 11, 2):
            quadrado = numero ** 2
            print(f"Número par: {numero:02d} | Quadrado ({numero}²): {quadrado}")

    # =========================================================================
    # PARTE 3: Resolução de Problema com Repetição
    # =========================================================================
    def calcular_soma_50_naturais(self) -> int:
        """
        Calcula a soma dos primeiros 50 números naturais (1 + 2 + ... + 50)
        utilizando um loop 'for' com variável acumuladora.

        Returns:
            int: Resultado total da soma (1275).
        """
        soma = 0

        for contador in range(1, 51):
            soma += contador

        print("\n" + "=" * 42)
        print("    SOMA DOS PRIMEIROS 50 NÚMEROS NATURAIS")
        print("=" * 42)
        print(f"Expressão: 1 + 2 + 3 + ... + 50")
        print(f"Resultado acumulado: {soma}")
        return soma


def main() -> None:
    """Função principal para executar e testar todas as partes da atividade."""
    atividade = AtividadeRepeticao(saldo_inicial=500.00)

    while True:
        print("\n" + "#" * 45)
        print("  ATIVIDADE PRÁTICA 1 - ESTRUTURAS DE REPETIÇÃO")
        print("#" * 45)
        print("1 - Parte 1: Caixa Eletrônico (Loop while)")
        print("2 - Parte 2.1: Quadrados de 1 a 10 (Loop for)")
        print("3 - Parte 2.2: Quadrados dos Pares de 1 a 10 (Loop for)")
        print("4 - Parte 3: Soma dos 50 Primeiros Naturais (Loop for)")
        print("0 - Sair")
        print("#" * 45)

        escolha = input("Selecione a parte que deseja executar: ").strip()

        if escolha == "1":
            atividade.simular_caixa_eletronico()
        elif escolha == "2":
            atividade.exibir_quadrados_1_a_10()
        elif escolha == "3":
            atividade.exibir_quadrados_pares_1_a_10()
        elif escolha == "4":
            atividade.calcular_soma_50_naturais()
        elif escolha == "0":
            print("\nPrograma finalizado. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número entre 0 e 4.")


if __name__ == "__main__":
    main()