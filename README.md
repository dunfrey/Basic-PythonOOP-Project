# Projeto Final - ECT2540

## Finalidade do repositório

Esta repositório dispõe de um projeto para abordar os conhecimentos obtidos no curso de **Programação Orientada à Objeto em Python** (UFRN/ECT2540).

## Conteúdo abordado

Neste projeto iremos abordar os conhecimentos de Python, POO e um pouco dos métodos de ciência de dados para compreender os dados.

## Origem do trabalho

A plataforma africana [Zindi](https://zindi.africa/) é um ambiente em que profissionais e pesquisadores podem participar de desafios científicos e, em muitos casos, ganhar dinheiro, dependendo dos resultados.

Em 2019, a empresa Xente, que trabalha com pagamentos online, e-commerce e serviços financeiros em Uganda, propôs um [desafio no Zindi](https://zindi.africa/competitions/xente-fraud-detection-challenge), com finalidade de identificar transações verdadeiras ou fraudulentas usando **Ciência de Dados**.

# Projeto 

Iremos:
- simular o cadastro de transações, abordando os conteúdos apresentados no curso;
- fazer a leitura de dados e projeção através de interface gráfica.

## Parte 1: Escrita dos dados

## Parte 2: Leitura dos dados

Concluída a primeira etapa do projeto, vamos a parte visual do trabalho.

Devemos ter um sistema feito em Tkinter que nos possibilite ler um tabela excel ou arquivo .csv e nos mostre em tela. A seguir, um exemplo de como iremos visualizar:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/fig1.png" width="700">

Devemos ter a possibilidade de inserir novos itens a tabela, como também compreender melhor os dados através de gráficos.

Sugestões de GUI para criar suas janelas gráficas: 
- [Pygubu](https://github.com/alejandroautalan/pygubu-designer): funciona tanto em sistemas Linux, quanto Windows (eu utilizei este para criar esta versão *demo*);

### Base de dados

Iremos utilizar um arquivo no formato `.csv`, que iremos ler utilizando a biblioteca Pandas e visualizaremos em nossa interface gráfica.
O arquivo encontra-se em: https://github.com/dunfrey/OOP_ProjectClass/blob/main/data.csv

O comando que deve ser executado para ler `data.csv` é:
```
df = pd.read_csv(<localizacao_e_nome_do_arquivo>)
```
em que `localizacao_e_nome_do_arquivo` é, como o próprio nome está sugerindo, a pasta em que o arquivo se encontra e o arquivo. Por exemplo `C:/Jose/data.csv`


## Para compreensão dos dados

As máquinas têm capacidade de processar dados e números, diferentemente dos humanos, que entendem muito melhor as informações visualmente. Por isso, para entender os dados é necessário transformá-los  de linguagem de máquina para a linguagem humana, tornando os dados **mais compreensiveis** e **facilitando o processo de realizar perguntas e hipoteses sobre os dados**.

Geralmente, a distribuição desses dados em uma tabela é muito dificil de observar a olho humano. Muitas linhas e colunas.

Para inicial, e melhor, compreensão os dados, 4 (quatro) gráficos podem ser utilizados:
- [**Gráfico de dipersão**](https://pt.wikipedia.org/wiki/Gr%C3%A1fico_de_dispers%C3%A3o): verifica se existe correlação. Coloca um ponto em plano cartesiano usando duas variáves;
- [**Histograma**](https://pt.wikipedia.org/wiki/Histograma): usado para entender a distribuição do conjunto de dados. Representa as variáveis em forma de barras;
- [**Dagrama de caixas**](https://pt.wikipedia.org/wiki/Diagrama_de_caixa): também usado para entender a distribuição dos dados, entendendo a concentração de valores de cada atributo;
- [**FDA**](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_distribui%C3%A7%C3%A3o_acumulada) (Função de distribuição acumulada): usado para saber qual a probabilidade de um valor ser igual ou superior a um determinado valor.

Estes quatro gráficos serão necessários e implementados neste trabalho.

Para gerar estes gráficos, vamos utilizar uma biblioteca chamada [Pandas](https://pandas.pydata.org/getting_started.html), através da chamada no nosso código da seguinte maneira:
```
# fazendo importe da biblioteca pandas na linguagem Python
import pandas
```

A seguir, um exmeplo de gráfico histograma gerado:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/fig2.png" width="400">
