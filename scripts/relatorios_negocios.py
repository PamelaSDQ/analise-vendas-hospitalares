import pandas as pd

def carregar_dados():
    
    caminho = "data/vendas_equipamentos_hospitalares.xlsx"
    df = pd.read_excel(caminho, sheet_name="Vendas_Equipamentos")
    return df

def calcular_ticket_medio_por_regiao(df):
    
    resumo = df.groupby('Regiao').agg(
        faturamento_total=('Faturamento_Total', 'sum'),
        ticket_medio=('Faturamento_Total', 'mean'),
        total_pedidos=('Faturamento_Total', 'count')
    ).reset_index()
    
    return resumo.sort_values(by='ticket_medio', ascending=False)

def analisar_por_categoria(df):
    
    resumo_categoria = df.groupby('Categoria').agg(
        faturamento=('Faturamento_Total', 'sum'),
        quantidade_vendida=('Quantidade', 'sum')
    ).reset_index()
    
    return resumo_categoria.sort_values(by='faturamento', ascending=False)

def consultar_regiao_especifica(df):
    
    print("\nRegiões disponíveis:", list(df['Regiao'].unique()))
    regiao = input("Digite o nome exato da Região que deseja consultar: ").strip()
    
    
    filtrado = df[df['Regiao'].str.lower() == regiao.lower()]
    
    if len(filtrado) > 0:
        faturamento_total = filtrado['Faturamento_Total'].sum()
        ticket_medio = filtrado['Faturamento_Total'].mean()
        total_pedidos = len(filtrado)
        
        print(f"\n--- RESULTADOS PARA A REGIÃO: {regiao.upper()} ---")
        print(f"Faturamento Total: R$ {faturamento_total:,.2f}")
        print(f"Ticket Médio: R$ {ticket_medio:,.2f}")
        print(f"Total de Pedidos: {total_pedidos}")
    else:
        print("\nRegião não encontrada. Verifique o nome digitado.")

def consultar_categoria_especifica(df):
    """
    Permite ao utilizador digitar uma categoria e ver os dados filtrados.
    """
    print("\nCategorias disponíveis:", list(df['Categoria'].unique()))
    categoria = input("Digite o nome exato da Categoria que deseja consultar: ").strip()
    
    filtrado = df[df['Categoria'].str.lower() == categoria.lower()]
    
    if len(filtrado) > 0:
        faturamento_total = filtrado['Faturamento_Total'].sum()
        quantidade_total = filtrado['Quantidade'].sum()
        
        print(f"\n--- RESULTADOS PARA A CATEGORIA: {categoria.upper()} ---")
        print(f"Faturamento Total: R$ {faturamento_total:,.2f}")
        print(f"Quantidade Vendida: {quantidade_total}")
    else:
        print("\nCategoria não encontrada. Verifique o nome digitado.")

# Menu Interativo Principal
if __name__ == "__main__":
    print("A carregar base de dados de vendas hospitalares...")
    df_vendas = carregar_dados()
    print(f"Base carregada com sucesso! Total de registos: {len(df_vendas)}")
    
    while True:
        print("\n========================================")
        print("      SISTEMA DE GESTÃO HOSPITALAR      ")
        print("========================================")
        print("[1] Ver Resumo Completo por Região")
        print("[2] Ver Resumo Completo por Categoria")
        print("[3] Consultar uma Região Específica")
        print("[4] Consultar uma Categoria Específica")
        print("[0] Sair do Sistema")
        print("========================================")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            resultado = calcular_ticket_medio_por_regiao(df_vendas)
            print("\n=== TICKET MÉDIO E FATURAMENTO POR REGIÃO ===")
            print(resultado.to_string(index=False))
            
        elif opcao == "2":
            resultado = analisar_por_categoria(df_vendas)
            print("\n=== DESEMPENHO POR CATEGORIA DE EQUIPAMENTO ===")
            print(resultado.to_string(index=False))
            
        elif opcao == "3":
            consultar_regiao_especifica(df_vendas)
            
        elif opcao == "4":
            consultar_categoria_especifica(df_vendas)
            
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 0 e 4.")