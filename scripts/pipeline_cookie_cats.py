import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Caminho do arquivo CSV (usando raw string 'r' para evitar conflitos de barra)
caminho_csv = r"C:\Users\dguer\OneDrive\Documentos\Projetos Analista\Games - Analise de Churn e Retenção\dados\cookie_cats.csv"

# 2. Leitura dos dados brutos do jogo
df = pd.read_csv(caminho_csv)
print(f"Dataset carregado com sucesso! Total de linhas: {len(df)}")
print(df.head())

# 3. Configuração de acesso ao banco MySQL local
# Dica: Se a sua senha terminava com '@', substitua por '%40' para a URL entender corretamente
usuario = "root"
senha = "suasenha"  # Ex: "minhasenha%40"
host = "localhost"
porta = "3306"
banco = "cookie_cats_db"

# 4. Criação da engine de conexão via SQLAlchemy
url_conexao = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"
engine = create_engine(url_conexao)

# 5. Ingestão dos dados para a tabela no MySQL
df.to_sql("raw_cookie_cats", con=engine, if_exists="replace", index=False)
print("Dados importados para a tabela 'raw_cookie_cats' no MySQL com sucesso!")