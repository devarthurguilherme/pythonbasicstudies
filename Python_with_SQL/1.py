import pyodbc

# Dados de conexão
dadosDeConexao = (
    "Driver={SQL Server};"
    # Nome completo do servidor SQL Server com instância
    "Server=ThaveaSantos\\SQLEXPRESS;"
    # Nome do banco de dados
    "Database=PythonSQL;"
)


conexao = pyodbc.connect(dadosDeConexao)
print("Conexão Feita!!!")
