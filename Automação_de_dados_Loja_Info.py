import sqlite3
import pandas as pd

# Conexão com o banco de dados (SQLite no exemplo)
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Criação da tabela (se não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL,
        vendas INTEGER,
        devolucoes INTEGER,
        performance INTEGER,
        pedidos INTEGER
    )
''')

# Função para buscar e atualizar dados
def atualizar_dados():
    df = pd.read_sql_query("SELECT * FROM produtos", conn)

    # Cálculo dos produtos mais vendidos
    mais_vendidos = df.nlargest(5, 'vendas')
    print("Produtos Mais Vendidos:\n", mais_vendidos)

    # Cálculo dos produtos com mais devoluções
    mais_devolvidos = df.nlargest(5, 'devolucoes')
    print("\nProdutos Mais Devolvidos:\n", mais_devolvidos)

    # Cálculo dos produtos mais caros e mais baratos
    mais_caros = df.nlargest(5, 'preco')
    mais_baratos = df.nsmallest(5, 'preco')
    print("\nProdutos Mais Caros:\n", mais_caros)
    print("\nProdutos Mais Baratos:\n", mais_baratos)

    # Cálculo dos produtos de alta performance
    alta_performance = df.nlargest(5, 'performance')
    print("\nProdutos de Alta Performance:\n", alta_performance)

    #calculo de produtos em pedidos
    produtos_em_pedidos = df.nlargest(5, 'pedidos')
    print('\n Produtos em pedidos:\n', produtos_em_pedidos)

    # Aqui você pode adicionar lógica para atualizar o banco de dados
    # Por exemplo, atualizar a coluna "vendas" com novos dados

# Chamada da função
atualizar_dados()

# Commit e fechamento da conexão
conn.commit()
conn.close()