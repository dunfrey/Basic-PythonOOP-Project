import pandas as pd

# ler um arquivo .csv e obter dataframe
df = pd.read_csv(csv_filename)

# imprimir n-primeiras e n-ultimas linhas do dataframe (ex.: 5 itens)
df.head(5)
df.tail(5)

# adicionar uma nova linha no dataframe (2 metodos)
df.append(lista_de_dados, ignore_index=True)
df[-1] = lista_de_dados

# exportar conteudo do dataframe como .csv (ou sobrescrever)
df.to_csv(csv_filename)

# converter conteudo do dataframe em lista de listas
lista = df.to_numpy().tolist()

# obter o nome (titulo) de cada coluna do dataframe
# formato da lista sera: ['coluna_1', 'coluna_2', ... , 'coluna_n']
colunas = df.columns

# gerar grafico: Histograma
df.hist(column = colunas)

# gerar grafico: Dispersao
df.plot.scatter(x='coluna_1', y='coluna_2')

# gerar grafico: Boxplot
df.boxplot(column = colunas)
                    
# gerar grafico: FDA
df.hist(column = colunas, cumulative=True)
