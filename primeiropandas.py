from readline import redisplay
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
#isin()
regioes_sul_suldeste = ['Sul','Suldeste']
vendas_sul_suldeste = df_vendas[df_vendas['regiao'].isin(regioes_sul_suldeste)]

print(f"Número de vendas nas regiões Sul e Sudeste: {len(vendas_sul_suldeste)}")
print("Primeiras 5 vendas nas regiões Sul e Sudeste: ")
print(vendas_sul_suldeste.head())

#between()

vendas_1000_2000 = df_vendas[df_vendas['valor_venda'].between(1000,2000)]

print(f"Número de enda entre R$1000,00 e R$2000,00: {len(vendas_1000_2000)}")

print("Primeiras 5 vendas entre R$1000,00 e R$2000,00:")
print(vendas_1000_2000.head())

## 2_Exercício 2: Filtragem de Dados
#2.1_Selecione apenas as colunas 'data','produto' e 'valor_venda' do DataFrame:
colunas_data_produto_venda = df_vendas[['data','produto','valor_venda']]

print("5 primeiras linhas das colunas selecionadas:")
print(colunas_data_produto_venda.head())
print(f"Tipo de dados{type(colunas_data_produto_venda)}")

#2.2_Filtre o DataFrame para mostrar apenas as vendas do canal 'Online':
canal_online = df_vendas[df_vendas['canal_venda'] == 'Online']
print(f"Número de vendas do canal Online: {len(canal_online)}")

print("Cinco primeiras linhas das vendas feitas pelo canal online:")
print(canal_online.head())

#2.3_Filtre o DataFrame para mostrar vendas de 'Roupas' com valor acima de 500:
valor_roupas = df_vendas[(df_vendas['categoria'] == 'Roupas') &
                         (df_vendas['valor_venda'] > 500)]

print(f"Número de venda de roupas: {len(valor_roupas)}")
print("Cinco primeiras linhas da venda de Roupas:")
print(valor_roupas.head())

#2.4_Use o método isin() para filtrar vendas dos produtos 'Smartphone' e 'Laptop':
smartphone_laptop = ['Smartphone','Laptop']
vendas_smartphone_laptop = df_vendas[df_vendas['produto'].isin(smartphone_laptop)]

print(f"Número de vendas de Smartphone e Laptop: {len(vendas_smartphone_laptop)}")
print("Primeiras cinco linhas das vendas de Smartphone e Laptop:")
print(vendas_smartphone_laptop.head())

#2.5_Use o método between() para encontrar vendas com quantidades entre 3 e 5 unidades:

quantidade_3_5 = df_vendas[df_vendas['quantidade'].between(3,5)]
print(f"Quantidade de vendas entre 3 e 5 produtos: {len(quantidade_3_5)}")
print("Primeiras 5 vendas de 5 e 3 produtos:")
print(quantidade_3_5.head())

##3. Ordenação e Indexação

#3.1 Ordenando dados:
#sort_values():
#Ordenando por uma coluna em ordem crescente (padrão)
df_ordenado_crescente = df_vendas.sort_values('valor_venda')

print("5 vendas com os menores valores:")
print(df_ordenado_crescente.head())
#Ordenando por uma coluna em ordem decrescente
df_ordenando_decrescente = df_vendas.sort_values('valor_venda',ascending=False)

print("5 vendas com maiores valores:")
print(df_ordenando_decrescente.head())

#Ordenando mútiplas colunas:
#Primeiro por categoria (A-Z) e depois por valor_venda (maior para menor)
df_ordenado_multi = df_vendas.sort_values(['categoria','valor_venda'],
                                          ascending=[True,False])
print("Ordenação por categoria e depois por valor (decrescente):")
print(df_ordenado_multi.head(10))

#3.2 Redefinindo e Usando Índices
#Definindo uma coluna como índice
df_indexado =  df_vendas.set_index('data')

print("DataFrame com 'data' como índice:")
print(df_indexado.head())

#Resetando o índice para voltar ao formato original
df_reset = df_indexado.reset_index()

print("DataFrame após reset do índice:")
print(df_reset.head())

#Acessando dados através do índice
#(Importante: assumindo que 'data' ainda é o índice)
print("Vendas em uma data específica:")
try:
    data_exemplo = df_indexado.index[0]#pegando a primeira data como exemplo
    print(f"Vendas em {data_exemplo}:")
    redisplay(df_indexado.loc[data_exemplo])
except:
    print("Certifique-se de que o DataFrame está indexado por 'data'")

##Execício 3: Ordenação e Indexação

#3.1_Ordene o DataFrame por 'avaliação' em ordem decrescente e mostre as 10 primeiras linhas
ordem_avaliacao = df_vendas.sort_values('avaliacao',ascending=False)

print("Cinco primeiras avaliações com menores valores:")
print(ordem_avaliacao.head())

#3.2_Ordene o DataFrame primeiro por 'regiao' (A-Z) e depois por 'valor_venda'
#(maior para menor)

ordem_regiao = df_vendas.sort_values('regiao',ascending=True)
ordem_venda = df_vendas.sort_values('valor_venda',ascending=False)

print("Regiões de A-Z")
print(ordem_regiao.head())
print("Maiores vendas:")
print(ordem_venda.head())

#3.3_Defina a coluna 'produto' como índice do DataFrame e mostre as 5 primeiras linhas
df_index_2 = df_vendas.set_index('produto')

print("DataFrame 'produto' como índice:")
print(df_index_2.head())

#3.4_Com o DataFrame indexado por ´produto´na questão anterior,acesse os dados do produto 'Smartphone'
#(use loc)

print("Ìndice de Smartphones")
try:
    produto_smartphone = df_index_2.index[0]
    print(f"Vendas de {produto_smartphone}")
    redisplay(df_index_2.loc[produto_smartphone])

except:
    print("Certifique-se de que o DataFrame está indexado por 'produto'")