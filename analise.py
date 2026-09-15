import pandas as pd

# 1. Carregando a planilha

caminho_arquivo = 'data/vendas_equipamentos_hospitalares.xlsx'
df = pd.read_excel(caminho_arquivo)

# 2. Mostrando as 5 primeiras linhas
print("---- PRIMEIRAS LINHAS----")
print(df.head())

# 3. Verificando o tamanho da tabela (Linhas, Colunas)
print("\n--- DIMENÇÕES DA TABELA (Linhas e colunas) ---")
print(df.shape)

# 4. Verificando os tipos de dados e colunas
print("\n--- INFORMAÇÕES GERAIS ---")
print(df.info())

# 5. Filtrado dados especificos
#Exemplo: Apenas equipamentos da categoria 'Suporte à Vida' na região 'Sudeste'
filtro_suporte_sudeste = df[(df['Categoria'] == 'Suporte à Vida') & (df['Regiao'] == 'Sudeste')]
print("\n--- EXIBINDO AS PRIMEIRAS VENDAS FILTRADAS --- ")
print(filtro_suporte_sudeste.head())

# Vendo quantidade de vendas( linhas) que atendem a esse critério
print("\n --- TOTAL DE VENDAS NESSE FILTRO ---")
print(f"Total de registros encontrados: {len(filtro_suporte_sudeste)}")

# 6. Calculando o faturamento total da base inteira
faturamento_total = df['Faturamento_Total'].sum()
print(f"\n--- FATURAMENTO TOTAL ---")
print(f"R$ {faturamento_total:,.2f}")

# 7. Calculando a Média do Preço unitário dos Equipamentos 
media_preco = df['Preco_Unitario'].mean()
print(f"\n--- MÉDIA DE PREÇO UNITÁRIO ---")
print(f"R$ {media_preco:,.2f}")

# 8. Agrupando dados Faturamento Total por Categoria de Equipamento
faturamento_por_categoria = df.groupby('Categoria')['Faturamento_Total'].sum().reset_index()
print("\n ---  FATURAMENTO TOTAL POR CATEGORIA DE EQUIPAMENTO ---")
print(faturamento_por_categoria)

# 9. Salvando essa visão resumida em um novo arquivo
faturamento_por_categoria.to_excel('data/faturamento_por_categoria.xlsx', index=False)
print("\n[INFO] Tabela resumida salva com sucesso na pasta data/ para uso futuro!")