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

Esta primeira parte do projeto iremos fazer simulações, sem interface gráfica, apenas em código, de transações financeiras.

3 componentes principais devem existir: 1) Um cliente; 2) Um produto, e; 3) Um hardware pra efetuar a compra.

E, ao final, iremos "gerar" um último componente:
- Uma transação

Para isso, devemos considerar que seu código deve conter as seguintes classes:

- Classe `Util`
  - um método que recebe uma lista e retorne um número aeatório ainda não contido na lista
- Classe `Relogio` e Classe `Calendario`
- Classe `RelogioCalendario`
  - deve ser uma subclasse de `Relogio` e `Calendario`
  - formatação de saída `__str__`: `YYYY/mm/ddTHH:mm:ssZ`
- Classe `ClienteEntity`
  - Abstrata
  - contém 1 (um) atributo de classe privado
    - use decorador para inserir e obter o valor do atributo
    - armazena todos os id de clientes
  - contém 1 (um) atributo de instância, que armazena o id do objeto instanciado
- Classe `Pessoa`
  - é subclasse de `ClienteEntity`
  - possui 2 (dois) atributos de instância: nome da pessoa e id da pessoa
- Classe `Cliente`
  - é subclasse de `Pessoa`
  - possui 1 (um) atributo de instância. Armazena o montante de dinheiro do objeto
- Classe `Produto`
  - deve conter todas as informações de um produto, que os cabeçalhos de cada coluna do arquivo [data.csv](https://github.com/dunfrey/OOP_ProjectClass/blob/main/data.csv)
  - deve também conter pelo menos um método estático, no qual seja possível acessar uma lista de todos os itens instânciados
- Classe `HardwareConfig`
  - contém 2 (dois) atributos de classe privado: id de provedor e id de canal
    - use decorador para inserir e obter o valor do atributo
    - use valor padrão 1, para os dois casos
- Classe `Transacao`
  - deve conter todas as informações de uma transacao, ou seja, dados como informacoes do cliente, do produto, o hardware que foi utilizado para fazer a transacao, dia e hora da transacao 
  - contém 1 (um) atributo de classe privado
    - use decorador para inserir e obter o valor do atributo
    - armazena todos os id de clientes

Lembre-se que a classe Transacao deve ser uma composição de elementos, ou seja, será "alimentada por intâncias" de outras classes. 

Uma visão macro é a seguinte:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/parte1.png" width="700">

### Alguns exemplos de resultado esperado:
código Produto:
```
pd1 = Produto(13, 2, 'airtime', 152.2)
pd2 = Produto(8, 2, 'utility_bill', 69.52)
pd3 = Produto(3, 1, 'utility_bill', 75.68)
```
saída Produto:
```
id: 3 - Valor: $75.68 - Estrategia de Preco: 1 - Categoria: utility_bill 
id: 8 - Valor: $69.52 - Estrategia de Preco: 2 - Categoria: utility_bill 
id: 13 - Valor: $152.2 - Estrategia de Preco: 2 - Categoria: airtime 
```

código Transacao:
```
transacao_1 = Transacao(c1, pd2, hd_config, hora_transacao)
```
saída Transacao:
```
Cliente:
Nome: Claus - Id: 9882 - Valor em Conta: 100.25
Produto:
id: 8 - Valor: $69.52 - Estrategia de Preco:: 2 - Categoria: utility_bill
Hardware:
1 - 1
```

### IMPORTANTE
Além do código, também deve ser entregue o diagrama de classes.

## Parte 2: Leitura dos dados

Concluída a primeira etapa do projeto, vamos a parte visual do trabalho.

Devemos ter um sistema feito em Tkinter que nos possibilite:
- ler um tabela excel ou arquivo .csv e nos mostre em tela;
- adicionar novos itens a essa tabela;
- gerar gráficos sobre os dados.


A seguir, um exemplo de como iremos visualizar:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/fig1.png" width="700">

Uma sugestão de GUI para criação suas janelas gráficas é [Pygubu](https://github.com/alejandroautalan/pygubu-designer):
- funciona tanto em sistemas Linux, quanto Windows (eu utilizei este para criar esta versão *demo*);

### Base de dados

Iremos utilizar um arquivo no formato `.csv`, que iremos ler utilizando a biblioteca Pandas e visualizaremos em nossa interface gráfica.
O arquivo encontra-se em: https://github.com/dunfrey/OOP_ProjectClass/blob/main/data.csv

A leitura do arquivo será utilizando a biblioteca [Pandas](https://pandas.pydata.org/getting_started.html). Use o seguinte comando para ler `data.csv`:
```
# fazendo importe da biblioteca pandas na linguagem Python
import pandas

df = pd.read_csv(<localizacao_e_nome_do_arquivo>)
```
em que `localizacao_e_nome_do_arquivo` é, como o próprio nome está sugerindo, a pasta em que o arquivo se encontra e o arquivo. Por exemplo `C:/Aluno/data.csv`


## Para compreensão dos dados

As máquinas têm capacidade de processar dados e números, diferentemente dos humanos, que entendem muito melhor as informações visualmente. Por isso, para entender os dados é necessário transformá-los  de linguagem de máquina para a linguagem humana, tornando os dados **mais compreensiveis** e **facilitando o processo de realizar perguntas e hipoteses sobre os dados**.

Geralmente, a distribuição desses dados em uma tabela é muito dificil de observar a olho humano. Muitas linhas e colunas.

Para melhor compreensão os dados, 4 (quatro) gráficos podem ser utilizados:
- [**Gráfico de dipersão**](https://pt.wikipedia.org/wiki/Gr%C3%A1fico_de_dispers%C3%A3o): verifica se existe correlação. Coloca um ponto em plano cartesiano usando duas variáves;
- [**Histograma**](https://pt.wikipedia.org/wiki/Histograma): usado para entender a distribuição do conjunto de dados. Representa as variáveis em forma de barras;
- [**Dagrama de caixas**](https://pt.wikipedia.org/wiki/Diagrama_de_caixa): também usado para entender a distribuição dos dados, entendendo a concentração de valores de cada atributo;
- [**FDA**](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_distribui%C3%A7%C3%A3o_acumulada) (Função de distribuição acumulada): usado para saber qual a probabilidade de um valor ser igual ou superior a um determinado valor.

Estes quatro gráficos devem implementados neste trabalho.

Você pode verificar alguns comandos de manipulação de dataframe  e gerar os gráficos [neste arquivo](https://github.com/dunfrey/OOP_ProjectClass/blob/main/comandos_pandas.py) ou acessar o site [Pandas](https://pandas.pydata.org/docs/index.html).

A seguir, um exemplo de gráfico histograma gerado:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/fig2.png" width="700">
