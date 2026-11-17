# 🔁 Estruturas de Repetição Básicas em Python (`repeticoesPython`)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Licença](https://img.shields.io/badge/Licença-Acadêmica-lightgrey)

Implementação prática em **Python** das estruturas de repetição fundamentais (`while` e `for`), organizada de forma orientada a objetos através da classe **`AtividadeRepeticao`**. O projeto resolve problemas clássicos de controle de fluxo interativo, geração de padrões numéricos e acumulação matemática via interface de linha de comando (CLI).

> **Contexto Acadêmico:** Atividade Prática 1 — Disciplina de *Algoritmos e Estrutura de Dados* | Curso de Análise e Desenvolvimento de Sistemas (2026).

---

## 📑 Índice

1. [Objetivo do Projeto](#-objetivo-do-projeto)
2. [Estrutura do Repositório](#-estrutura-do-repositório)
3. [Arquitetura e Detalhamento da Classe](#-arquitetura-e-detalhamento-da-classe)
4. [Como Executar](#-como-executar)
5. [Exemplos de Uso e Saída](#-exemplos-de-uso-e-saída)
6. [Análise Técnica das Estruturas Utilizadas](#-análise-técnica-das-estruturas-utilizadas)
7. [Autoria](#-autoria)

---

## 🎯 Objetivo do Projeto

Compreender e aplicar na prática as estruturas de repetição **`while`** (repetição condicional/indeterminada) e **`for`** (repetição contada/determinística) em Python para automatizar tarefas repetitivas, validar entradas de usuário e resolver problemas lógicos e matemáticos com código limpo, tipado e documentado.

---

## 📁 Estrutura do Repositório

```text
repeticoesPython/
├── estruturas_repeticao.py   # Código-fonte principal contendo a classe AtividadeRepeticao e o menu CLI
└── README.md                 # Documentação técnica do repositório
```

---

## 🧩 Arquitetura e Detalhamento da Classe

Toda a lógica do projeto está encapsulada na classe **`AtividadeRepeticao`** (`estruturas_repeticao.py`), que mantém o estado da conta bancária simulada e organiza cada parte da atividade em métodos independentes:

### Classe `AtividadeRepeticao`
- **`__init__(self, saldo_inicial: float = 500.00)`**  
  Inicializa o atributo de instância `self.saldo` com o valor padrão de **R$ 500,00** exigido para a simulação do caixa eletrônico.

- **`simular_caixa_eletronico(self) -> None` *(Parte 1 — Loop `while`)***  
  Mantém um menu interativo em execução contínua enquanto a opção escolhida for diferente de `"3"`. Permite consultar o saldo atual, realizar saques com validação de valores positivos e verificação de saldo suficiente, além de tratar entradas inválidas (`ValueError`).

- **`exibir_quadrados_1_a_10(self) -> None` *(Parte 2.1 — Loop `for`)***  
  Percorre o intervalo `range(1, 11)` e exibe cada número inteiro de 1 a 10 acompanhado de seu quadrado (`numero ** 2`).

- **`exibir_quadrados_pares_1_a_10(self) -> None` *(Parte 2.2 — Loop `for` com passo)***  
  Utiliza o terceiro argumento (*step*) da função `range(2, 11, 2)` para iterar diretamente sobre os números pares de 2 a 10 e calcular seus respectivos quadrados sem necessidade de condicionais extras.

- **`calcular_soma_50_naturais(self) -> int` *(Parte 3 — Loop `for` acumulador)***  
  Utiliza uma variável acumuladora (`soma = 0`) dentro de um laço `for contador in range(1, 51)` para somar os 50 primeiros números naturais (`1 + 2 + ... + 50`), retornando o resultado exato **`1275`**.

- **`main() -> None`**  
  Função orquestradora que instancia `AtividadeRepeticao` e exibe um menu principal para navegar entre todas as partes da atividade.

---

## 🚀 Como Executar

### Pré-requisitos
- **Python 3.8 ou superior** instalado (utiliza apenas recursos nativos da linguagem, sem bibliotecas externas).

### Passo a passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/Thallitasp/repeticoesPython.git](https://github.com/Thallitasp/repeticoesPython.git)
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd repeticoesPython
   ```
3. Execute o script principal:
   - **Windows (PowerShell / CMD):**
     ```powershell
     py estruturas_repeticao.py
     ```
   - **Linux / macOS:**
     ```bash
     python3 estruturas_repeticao.py
     ```

---

## 🖥️ Exemplos de Uso e Saída

### Menu Principal
```text
#############################################
  ATIVIDADE PRÁTICA 1 - ESTRUTURAS DE REPETIÇÃO
#############################################
1 - Parte 1: Caixa Eletrônico (Loop while)
2 - Parte 2.1: Quadrados de 1 a 10 (Loop for)
3 - Parte 2.2: Quadrados dos Pares de 1 a 10 (Loop for)
4 - Parte 3: Soma dos 50 Primeiros Naturais (Loop for)
0 - Sair
#############################################
Selecione a parte que deseja executar:
```

### Parte 1 — Simulador de Caixa Eletrônico (`while`)
```text
==========================================
            CAIXA ELETRÔNICO
==========================================
1 - Verificar saldo
2 - Realizar saque
3 - Sair do sistema
------------------------------------------
Escolha uma opção: 2
Digite o valor que deseja sacar: R$ 150.00

[Sucesso] Saque de R$ 150.00 realizado!
[Saldo] Novo saldo disponível: R$ 350.00
```

### Parte 2.2 — Quadrados dos Números Pares (`for`)
```text
==========================================
   NÚMEROS PARES DE 1 A 10 E SEUS QUADRADOS
==========================================
Número par: 02 | Quadrado (2²): 4
Número par: 04 | Quadrado (4²): 16
Número par: 06 | Quadrado (6²): 36
Número par: 08 | Quadrado (8²): 64
Número par: 10 | Quadrado (10²): 100
```

### Parte 3 — Soma dos 50 Primeiros Números Naturais (`for`)
```text
==========================================
    SOMA DOS PRIMEIROS 50 NÚMEROS NATURAIS
==========================================
Expressão: 1 + 2 + 3 + ... + 50
Resultado acumulado: 1275
```

---

## 📊 Análise Técnica das Estruturas Utilizadas

| Problema | Estrutura | Justificativa Técnica |
| :--- | :---: | :--- |
| **Caixa Eletrônico** | `while` | O número de operações que o usuário realizará é **indeterminado**; o laço depende exclusivamente da condição de saída (`opcao != "3"`). |
| **Quadrados (1 a 10 e Pares)** | `for` | Elimina código repetitivo encapsulando inicialização, limite e passo em `range()`, tornando o algoritmo escalável e legível. |
| **Soma de 1 a 50** | `for` | Como os limites inicial (`1`) e final (`50`) são **conhecidos previamente**, o laço contado evita risco de loop infinito e calcula `1275` ($S_{50} = \frac{50 \times 51}{2}$) de forma determinística. |

---

## 👩‍💻 Autoria

Desenvolvido por **Thallita da Silva Pedreira**  
Repositório: github.com/Thallitasp/repeticoesPython
