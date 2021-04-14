> 📝 *Portuguese version*

# Projeto Final - ECT2540

## Finalidade do repositório

Esta repositório dispõe de um projeto para abordar os conhecimentos obtidos no curso de **Programação Orientada à Objeto em Python** (UFRN/ECT2540).

## Conteúdo abordado

Neste projeto iremos abordar os conhecimentos de Python, POO e um pouco dos métodos de ciência de dados para compreender os dados.

## Origem do trabalho

A plataforma africana [Zindi](https://zindi.africa/) é um ambiente em que profissionais e pesquisadores podem participar de desafios científicos e, em muitos casos, ganhar premiações em dinheiro, dependendo dos resultados.

Em 2019, a empresa Xente, que trabalha com pagamentos online, e-commerce e serviços financeiros em Uganda, propôs um [desafio no Zindi](https://zindi.africa/competitions/xente-fraud-detection-challenge), com finalidade de identificar transações verdadeiras ou fraudulentas usando **Ciência de Dados**.

# Projeto 

O projeto possui duas etapas, que consiste em:
> - Simular o cadastro de transações, abordando os pilares de POO apresentados no curso;
> - Fazer uso de interface gráfica para leitura, projeção e inserção de novos dados.

**Reaproveite código!!! Não escreva um mesmo bloco de código em diferente partes do artefato**

Essa abordagem mantém o tamanho reduzido e facilita a leitura e manutenção do código.

## Parte 1: Escrita dos dados

Primeiro, iremos simular um sistema que registra transações financeiras, sem fazer uso de interface gráfica. 

Para que uma transação ocorra iremos precisar fazer uso de informações de: 
> 1) Um cliente; 
> 2) Um produto, e; 
> 3) Um hardware (computador) pra efetuar a transação.
> 4) Data e hora

Com posse de informações desses três componentes, podemos "gerar" uma transação.

Portanto, para isso devemos considerar que seu código deve conter, **pelo menos**, as seguintes classes:

- Classe `Util`
  - contém um método publico que vai gerar um número inteiro aleatório
    - este método precisa receber uma lista como parâmetro para que, na geração do número, este não existe previamente na lista.
- Classe `Datetime`
  - método `__str__` &#8594; `YYYY/mm/ddTHH:mm:ssZ`
- Classe `PessoaEntidade`
  - é classe abstrata
  - contém 1 (uma) lista de classe protegida
    - use decorador para *set* e *get*
    - a função da lista deve ser a de armazenar todos os *ids* das pessoas já registradas
  - contém 1 (um) atributo de instância que pode ser acessado, que armazena o id do objeto instanciado (use o método `genId()` da classe `Util` para gerar este *id*)
- Classe `Pessoa`
  - é subclasse de `PessoaEntidade`
  - possui 2 (dois) atributos de instância que são por guardar o nome da pessoa e o seu id (use o método `genId()` da classe `Util` para gerar este *id*)
- Classe `Cliente`
  - `Cliente` é uma `Pessoa`
  - possui 1 (um) atributo de instância que armazena o montante de dinheiro do cliente
  - método `__str__` &#8594; `nome - id - montante em conta`
- Classe `Produto`
  > **sobre esta classe:** deve conter todas as informações de um produto. Para entender quas são, use os cabeçalhos de cada coluna do arquivo [data.csv](https://github.com/dunfrey/OOP_ProjectClass/blob/main/data.csv)
  - contém um método estático para acessar uma lista de todos os itens instânciados
  - contém os seguintes atributos: id, a estratégia de preco adotado, a categoria e o valor do produto
  - contém uma dicionário privado que armazena todos os itens e que pode ser acessado pelo método estático 
    - Use o id como chave no dicionário
  - método `__str__` &#8594; `id - valor - estrategia de preco - categoria`
- Classe `HardwareConfig`
  - contém 2 (dois) atributos de classe protegidos: id de provedor e id de canal
    - use decorador para inserir e obter o valor dos atributos
    - use valor padrão 1, para os dois atributos
  > **sobre esta classe:** um canal seria um computador (valor 1), smartphone (valor 2), etc. Um provedor é o fornecedor de internet (vamos manter esta informação apenas por detalhamento, mas a informação em si não será importante neste trabalho)
  - método `__str__` &#8594; `id provedor - id canal`
- Classe `Transacao`
  - deve conter todas as informações de uma transacao, ou seja, dados como informacoes do cliente, do produto, o hardware que foi utilizado para fazer a transacao, dia e hora da transacao
  - toda transação contém seu próprio id, pra isso use o método `genId()` da classe `Util` para gerar este *id*
  - contém 1 (uma) lista de classe privada
    - use decorador para inserir e obter os valores
    - armazenará todos os id de clientes
  - contém um método público `getData()` que formata os dados (gera uma lista)
    - ex.: `[1,2,1,"produto 2", "2021/03/05T03:46:s57Z"]`
  - método `__str__` &#8594; `Cliente: cliente \n Produto: produto \n Hardware: hardware`

> Lembre-se que a classe `Transacao` deve ser uma composição de elementos, ou seja, será "alimentada por intâncias" de outras classes. 

Uma visão macro é a seguinte:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/parte1.png" width="700">

### Alguns exemplos de resultado esperado:
criando Produtos:
```
pd1 = Produto(13, 2, 'airtime', 152.2)
pd2 = Produto(8, 2, 'utility_bill', 69.52)
pd3 = Produto(3, 1, 'utility_bill', 75.68)
```
imprimindo cada Produto:
```
id: 3 - Valor: $75.68 - Estrategia de Preco: 1 - Categoria: utility_bill 
id: 8 - Valor: $69.52 - Estrategia de Preco: 2 - Categoria: utility_bill 
id: 13 - Valor: $152.2 - Estrategia de Preco: 2 - Categoria: airtime 
```

criando uma Transação:
```
transacao_1 = Transacao(c1, pd2, hd_config, hora_transacao)
```
imprimindo a Transação:
```
Cliente:
Nome: Claus - Id: 9882 - Valor em Conta: 100.25
Produto:
id: 8 - Valor: $69.52 - Estrategia de Preco:: 2 - Categoria: utility_bill
Hardware:
1 - 1
```

Para **criar um dataframe e inserir estes dados** usando Pandas, veja este [arquivo](https://github.com/dunfrey/Project_OOPClass/blob/main/comandos_pandas.py).

> ### IMPORTANTE
> Além do código, também deve ser entregue o diagrama de classes.

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


### Para compreensão dos dados

As máquinas têm capacidade de processar dados e números, diferentemente dos humanos, que entendem muito melhor as informações visualmente. Por isso, para entender os dados é necessário transformá-los  de linguagem de máquina para a linguagem humana, tornando os dados **mais compreensiveis** e **facilitando o processo de realizar perguntas e hipoteses sobre os dados**.

Geralmente, a distribuição desses dados em uma tabela é muito dificil de observar a olho humano. Muitas linhas e colunas.

Para melhor compreensão os dados, 4 (quatro) gráficos podem ser utilizados:
- [**Gráfico de dipersão**](https://pt.wikipedia.org/wiki/Gr%C3%A1fico_de_dispers%C3%A3o): verifica se existe correlação. Coloca um ponto em plano cartesiano usando duas variáves;
- [**Histograma**](https://pt.wikipedia.org/wiki/Histograma): usado para entender a distribuição do conjunto de dados. Representa as variáveis em forma de barras;
- [**Dagrama de caixas**](https://pt.wikipedia.org/wiki/Diagrama_de_caixa): também usado para entender a distribuição dos dados, entendendo a concentração de valores de cada atributo;
- [**FDA**](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_distribui%C3%A7%C3%A3o_acumulada) (Função de distribuição acumulada): usado para saber qual a probabilidade de um valor ser igual ou superior a um determinado valor.

Estes quatro gráficos devem implementados neste trabalho, e deve ser permitido a seleção de quais atributos queremos analisar.

Você pode verificar alguns comandos de manipulação de dataframe  e gerar os gráficos [neste arquivo](https://github.com/dunfrey/OOP_ProjectClass/blob/main/comandos_pandas.py) ou acessar o site [Pandas](https://pandas.pydata.org/docs/index.html).

A seguir, um exemplo de gráfico histograma gerado:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/fig2.png" width="700">
