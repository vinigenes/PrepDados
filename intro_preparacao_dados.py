#Análise Exploratória de Dados (AED)
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string(), '\n')


print('Verificação de Dados')
print(df.info(), '\n')

print('Análise de dados nulos:\n', df.isnull().sum(), '\n')
print('% de dados nulos:\n', df.isnull().mean() * 100, '\n')
df.dropna(inplace=True)
print('Confirmar remoção de dados  nulos: \n', df.isnull().sum().sum(), '\n')

print('Análise de dados duplicados: \n', df.duplicated().sum(), '\n')

print('Análise de dados únicos: \n', df.nunique(), '\n')

print('Estatísticas dos dados: \n', df.describe(), '\n')

#print(df.columns)

df = df[['idade', 'data','endereco', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
# df = df.reindex(columns=['idade', 'data', 'estado', 'salario', 'nivel-educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'])
print(df.head().to_string())

#df.to_csv('clientes-v2-tratados.csv', index=False)