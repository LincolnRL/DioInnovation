import pandas as pd
df = pd.read_csv('Desafio.csv', sep=';')

# extract
# carregar
user_ids = df['Nome'].tolist()
print(user_ids)

# transform
# separar somente duas colunas
colunas = ['Nome', 'Time']
df_Colunas = df[colunas]

# load
# salvar em outro csv
novo_Arquivo = 'Tabela.csv'
df_Colunas.to_csv(novo_Arquivo, index=False)