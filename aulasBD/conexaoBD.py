import psycopg2

# Conecte-se ao PostgreSQL (certifique-se de substituir os valores pelos seus próprios)
conn = psycopg2.connect(
    database="Loja",  # Nome do banco de dados
    user="postgres",  # Seu usuário do PostgreSQL
    password="senhapgadmin",  # Sua senha do PostgreSQL
    host="localhost",  # Host onde o PostgreSQL está rodando
    port="5432"  # Porta padrão do PostgreSQL
)

cur = conn.cursor()

# Resto do seu código para criar o banco de dados e a tabela

conn.commit()
conn.close()
