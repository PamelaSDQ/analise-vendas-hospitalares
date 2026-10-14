# 🏥 Sistema Interativo de Análise de Vendas Hospitalares

## 📌 Sobre o Projeto
Este projeto faz parte do meu portfólio de dados e tem como objetivo simular uma análise gerencial de vendas de equipamentos hospitalares. O fluxo foi planejado para abranger desde a manipulação e extração de indicadores em **Python (Pandas)** até a criação de um sistema de consulta interativo e dinâmico diretamente no terminal.

---

## 🚀 O que este sistema faz?
O projeto lê a base de dados consolidada e oferece um **menu interativo** no terminal onde podes escolher o que consultar em tempo real:
1. **Faturamento e Ticket Médio por Região**: Descobre quais as regiões que mais faturam e o valor médio por venda, ordenado do maior para o menor.
2. **Desempenho por Categoria**: Visualiza os tipos de equipamentos hospitalares que lideram em volume de vendas e faturamento.
3. **Consultas Específicas sob Demanda**: Digita o nome de uma região ou categoria específica para obter os números exatos instantaneamente.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.13**
- **Pandas** (Manipulação, filtros e agregações)
- **Openpyxl** (Leitura de arquivos Excel)
- **Git / GitHub** (Controle de versão e portfólio)

---

## 📁 Estrutura do Repositório
```text
analise-vendas-hospitalares/
│
├── data/
│   └── vendas_equipamentos_hospitalares.xlsx  # Base de dados principal
│
├── scripts/
│   └── relatorios_negocios.py              # Script principal com o menu interativo
│
└── README.md                               # Documentação do projeto