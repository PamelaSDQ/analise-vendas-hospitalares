# 🏥 Análise de Vendas de Equipamentos Hospitalares

## 📌 Sobre o Projeto
Este projeto faz parte do meu portfólio de dados e tem como objetivo simular uma análise gerencial de vendas de equipamentos hospitalares. O fluxo foi planejado para abranger desde a manipulação e extração de indicadores em **Python (Pandas)**, passando futuramente por modelagem em **SQL**, até a criação de dashboards executivos em **Power BI**.

## 🛠️ Tecnologias Utilizadas
- **Python 3.13**
- **Pandas** (Manipulação, filtros e agregações)
- **Openpyxl** (Leitura e escrita de arquivos Excel)
- **Git / GitHub** (Controle de versão e portfólio)

## 📊 Principais Indicadores Desenvolvidos
- Faturamento Total da base de dados.
- Média de preço unitário dos equipamentos hospitalares.
- Filtros avançados por categoria de equipamento e região de atuação.
- Agregação corporativa de faturamento por categoria (`GROUP BY`).

## 📁 Estrutura do Repositório
```text
analise-vendas-hospitalares/
│
├── data/
│   ├── vendas_equipamentos_hospitalares.xlsx (Base bruta)
│   └── faturamento_por_categoria.xlsx        (Base agregada para BI)
│
├── analise.py                                 (Script principal em Python)
└── README.md                                  (Documentação do projeto)