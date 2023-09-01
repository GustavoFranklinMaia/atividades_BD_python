import psycopg2
import csv

def inserir_dados_do_csv():
    try:
        conn = psycopg2.connect(
            database="test",
            user="postgres",
            password="senhapgadmin",
            host="127.0.0.1",
            port="5432"
        )

        # Crie um cursor
        cur = conn.cursor()

        # Abra o arquivo CSV para leitura
        with open('PYDB\dados_extraidos.csv', 'r') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            
            # Pule o cabeçalho se houver um
            next(leitor_csv, None)

            
            
            # Itere sobre as linhas do arquivo CSV e insira os dados no banco de dados
            for linha in leitor_csv:
                
                dado1 = linha[0].strip()
                dado2 = linha[1].strip()
                dado3 = linha[2].strip()
                dado4 = linha[3].strip()
                dado5 = linha[4].strip()
                
                
                cur.execute("INSERT INTO deputado (nome, partido, uf, despesas, mes) VALUES (%s, %s, %s, %s, %s)", ([dado1, dado2, dado3, dado4, dado5]))
                
  
        conn.commit()
 #       inserir_dados_do_csv("PYDB\dados_extraidos.csv")
        print("Dados inseridos com sucesso!")

    except (Exception, psycopg2.Error) as error:
        print(f"Erro ao inserir dados: {error}")
        
    finally:
        # Feche a conexão
        if conn:
            conn.close()

inserir_dados_do_csv()
