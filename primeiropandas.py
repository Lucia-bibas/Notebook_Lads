import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

datas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Casa', 'Beleza']
produtos = {
    'Eletrônicos': ['Smartphone', 'Laptop', 'Tablet', 'Fones de ouvido', 'Smart TV'],
    'Roupas': ['Camiseta', 'Calça', 'Vestido', 'Sapato', 'Jaqueta'],
    'Alimentos': ['Arroz', 'Feijão', 'Óleo', 'Açúcar', 'Café'],
    'Casa': ['Sofá', 'Mesa', 'Cadeira', 'Cama', 'Armário'],
    'Beleza': ['Shampoo', 'Condicionador', 'Sabonete', 'Perfume', 'Hidratante']
}
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
estados = {
    'Norte': ['AM', 'PA', 'RO', 'RR', 'AC'],
    'Nordeste': ['BA', 'PE', 'CE', 'MA', 'PB'],
    'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
    'Sudeste': ['SP', 'RJ', 'MG', 'ES'],
    'Sul': ['PR', 'SC', 'RS']
}
canais = ['Online', 'Loja Física', 'Aplicativo', 'Telefone']

n_registros = 1000
data_vendas = []

for _ in range(n_registros):
    data = np.random.choice(datas)
    categoria = np.random.choice(categorias)
    produto = np.random.choice(produtos[categoria])
    regiao = np.random.choice(regioes)
    estado = np.random.choice(estados[regiao])
    canal = np.random.choice(canais)
    valor = round(np.random.uniform(10, 5000), 2)  # Valor entre R$10 e R$5000
    quantidade = np.random.randint(1, 10)  # Entre 1 e 9 itens
    avaliacao = np.random.randint(1, 6)  # Avaliação de 1 a 5 estrelas
    
    data_vendas.append({
        'data': data,
        'categoria': categoria,
        'produto': produto,
        'regiao': regiao,
        'estado': estado,
        'canal_venda': canal,
        'valor_venda': valor,
        'quantidade': quantidade,
        'avaliacao': avaliacao
    })

df_vendas = pd.DataFrame(data_vendas)
df_vendas['data'] = df_vendas['data'].astype('object')

df_vendas.to_csv('dados_vendas.csv', index=False)

print(df_vendas.head())

#1.3

# Visualizando as primeiras linhas com head()
print("Primeiras 5 linhas do DataFrame:")
print(df_vendas.head(5))

#As últimas cinco linhas com tail:
print("As últimas 5 linhas doData Frame:")
print(df_vendas.tail(5))

#Verificando o formato do data frame (linhas,colunas) com o shape:
print(f"O Formato do data frame: {df_vendas.shape}")
print(f"O número de linhas: {df_vendas.shape[0]}")
print(f"Número de colunas: {df_vendas.shape[1]}")
print("Nome das colunas:")
print(df_vendas.columns.tolist())

#1.4:Informações e Estatisticas

#Verificando informações do data frame com o info()

print("Informações do data frame:")
print(df_vendas.info())

#Estátisticas decritivas com descibe:
print("Estatísticas descritias:")
print(df_vendas.describe())

#Contagem de valos unico com nunique():
print("Valores únicos em cada coluna:")
print(df_vendas.nunique())

#1.5 Valores unicos e nulos:
#Verificando valores únicos em uma coluna categórica:
print("Categorias únicas:")
print(df_vendas['categoria'].unique())

#Contando ocorrências de cada valor:

print("Contagem de cada categoria:")
print(df_vendas['categoria'].value_counts())
print("Valores nulos em cada coluna:")
print(df_vendas.isnull().sum())

## 1.Exercício: Exploração Básica de Dados

# 1.1_Use o método head() para mostrar as 10 primeiras linhas:

print("Visualizando as 10 primeiras linhas do Data Frame:")
print(df_vendas.head(10))

# 1.2_Use o shape para verificar quantar linhas e colunas tem o Data Frame:

print("Verificando quantas linhas e colunas tem o Data Frame:")
print(f"Quantidade de linhas: {df_vendas.shape[0]}")
print(f"Quantidade de colunas: {df_vendas.shape[1]}")

# 1.3_Use o método unique() para listar todas as regiõs do Data Frame:

print("Verificando todas as regiõe no data frame:")
print(df_vendas['regiao'].unique())

# 1.4_Use o método value_counts() para contar quantas vendas existem por 'canal_venda'
print("Quantas vendas existem por 'canal_venda':")
print(df_vendas['canal_venda'].value_counts())

# 1.5_Use o método describe() para obter estatíticas da coluna 'valor_venda'
print("Estatísticas de valores de venda:")
print(df_vendas['valor_venda'].describe())


#2.Seleção e filtragem de dados:

#2.1 Seleção de colunas:

#Selecionando uma coluna única:

valores_venda = df_vendas['valor_venda']
print("primeiros cinco valores de coluna 'valor_venda':")
print(valores_venda.head())
print(f"Tipos de dados: {type(valores_venda)}")

#Selecionando múltipla colunas(retorna um Data Frame):
selecao = df_vendas[['produto','valor_venda','quantidade']]

print("Primeiras 5 linhas das colunas selecionadas:")
print(selecao.head())
print(f"Tipos de dados de seleção: {type(selecao)}")

#2.2 Filtrando linhas com condições:

#Filtragem básica: vendas com valor acima de 1000

vendas_altas = df_vendas[df_vendas['valor_venda'] > 1000]
print(f"Número de vendas com valor acima de R$1000,00: {len(vendas_altas)}")

print("Primeiras 5 vendas com valor acima de R$1000,00:")
print(vendas_altas.head())

#Filtragem com múltiplas escolhas com operadores lógicos & (and) e | (or)

#Vendas de eletrônicos na região Sul

vendas_eletronicos_sul = df_vendas[(df_vendas['categoria'] == 'Eletrônicos') &
                                   (df_vendas['regiao'] == 'Sul')]
print(f"Número de vendas de eletrônicos na região Sul: {len(vendas_eletronicos_sul)}")

print("Primeiras 5 vendas de Eletrônicos na região Sul:")
print(vendas_eletronicos_sul.head())

#Filtrando com or lógico

#Vendas muito altas (>3000) ou com avaliação máxima (5):

vendas_premium = df_vendas[(df_vendas['valor_venda'] > 3000) |
                           (df_vendas['avaliacao'] == 5)]
print(f"Número de vendas premium: {len(vendas_premium)}")
print("Primeiras 5 vendas premium:")
print(vendas_premium.head())

#2.3 Filtragem com isin() e between()


