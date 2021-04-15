> 📝 *Portuguese version*

# Projeto Final - ECT2540

## Finalidade do repositório

Esta repositório dispõe de um projeto para abordar os conhecimentos obtidos no curso de **Programação Orientada à Objeto em Python** (UFRN/ECT2540).

## Conteúdo abordado

Neste projeto iremos abordar os conhecimentos de Python, POO e um pouco dos métodos de ciência de dados para compreender os dados, ou seja, vamos fazer algumas explotações (gerar figuras e levantamentos de informações) que, caso queira, permitirá fazer análises mais profunda dos dados.

## Origem do trabalho

A plataforma africana [Zindi](https://zindi.africa/) é um ambiente em que profissionais e pesquisadores podem participar de desafios científicos e, em muitos casos, ganhar premiações em dinheiro, dependendo dos resultados.

Em 2019, a empresa Xente, que trabalha com pagamentos online, e-commerce e serviços financeiros em Uganda, propôs um [desafio no Zindi](https://zindi.africa/competitions/xente-fraud-detection-challenge), com finalidade de identificar transações verdadeiras ou fraudulentas usando **Ciência de Dados**.

# Projeto 

O projeto possui duas etapas, que consiste em:
> - Simular o cadastro de transações, abordando os pilares de POO apresentados no curso;
> - Fazer uso de interface gráfica para leitura, projeção e inserção de novos dados.

Ao final, teremos uma interface que apresentada todas as transações de compras registradas, resumidas em uma tabela, similar a figura abaixo:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/fig1.png" width="700">

**Cada transação, ou seja, cada linha da tabela**, contém as seguintes informações:
- Transacao: id da transacao realizada
- Usuario: id do cliente comprador
- Provedor: id do provedor, ou seja, pode ser master, elo, visa, picpay, paypal, alipay, etc
  - Neste projeto, iremos ocultar a informação que associa um número a um determnado provedor, ou seja, usaremos apenas números
- Produto: id do produto comprado naquela transação
- ProdutoCategoria: uma representação de qual categoria o produto comprado está classificado
  - algumas categorias são: netflix, globoplay, ticket de museu, ticket de estádio, pagamento de boleto, varejo, etc
- Canal: id do provedor, ou seja, pode ser um computador, ou um smartphone, ou um tablet, etc
  - Neste projeto, iremos ocultar a informação sobre qual número representa qual canal, ou seja, usaremos apenas números
- ValorEmConta: valor que o cliente tem em conta no momento da compra do item
- ValorServico: valor do produto/serviço comprado
- DataHora: data e hora realizado pelo cliente
- EstrategiaPreco: todo produto possui uma estratégia de preço
  - Por exemplo, se estratégia é a n⁰ 1 então deve ser dado um desconto de 10%, se estratégia é 2, 15% de desconto
- Fraude: 1 ou 0. Valor 1 representa que a transacao é uma fraude, se 0, é uma operação válida

## Parte 1: Escrita dos dados

Primeiro, iremos simular um sistema que registra transações financeiras sem fazer uso de interface gráfica. 

Como observamos, uma transação precisa de informações de: 
> 1) Um cliente; 
> 2) Um produto; 
> 3) Um hardware (computador) pra efetuar a transação, e;
> 4) Informações da transação como data e hora.

Com posse desses requisitos, devemos considerar que seu código deve conter, **pelo menos**, as seguintes classes:

- Classe `Util`
  - contém um método publico que vai gerar um número inteiro aleatório
    - este método precisa receber uma lista como parâmetro para que, na geração do número, verifique se o número já não existe previamente na lista.
- Classe `Pessoa`
  - é classe abstrata
  - contém 1 (uma) lista de classe protegida
    - use decorador para *set* e *get*
    - a função da lista deve ser a de armazenar todos os *ids* das pessoas já registradas
  - contém 1 (um) atributo de instância que pode ser acessado, que armazena o id do objeto instanciado (use o método `genId()` da classe `Util` para gerar este *id*)
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
- Classe `SistemaProvedorCanal`
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
  - contém um método público `getData()` que formata todos dados em uma única lista
    - ex.: `lista = [id_transacao, 
            cliente.id_pessoa,
            sistema_pc.id_provedor,
            produto.id_produto,
            produto.categ_produto,
            sistema_pc.id_canal,
            cliente.valor_conta_cliente,
            produto.valor_produto,
            data/hora_transacao (`YYYY/mm/ddTHH:mm:ssZ`),
            produto.estrategia_preco_produto,
            fraude (1 ou 0)]`
  - use `Datetime` com formatação &#8594; `YYYY/mm/ddTHH:mm:ssZ`
  - método `__str__` &#8594; `Cliente: cliente \n Produto: produto \n Hardware: hardware`

> Lembre-se que a classe `Transacao` deve ser uma composição de elementos, ou seja, será "alimentada por intâncias" de outras classes. 

Uma visão macro é a seguinte:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/projeto_parte1.png" width="700">

### Alguns exemplos de resultado esperado:
criando Produtos:
```
pd1 = Produto(13, 2, 'Ticket - Museu', 152.2)
pd2 = Produto(8, 2, 'Netflix', 69.52)
pd3 = Produto(3, 1, 'Netflix', 75.68)
pd4 = Produto(456, 2, 'GloboPlay', 789.25)
pd5 = Produto(48, 1, 'GloboPlay', 853.99)
```
imprimindo cada Produto:
```
id Produto: 3 - Valor: $75.68 - Estrategia de Preco: 1 - Categoria: Netflix 
id Produto: 8 - Valor: $69.52 - Estrategia de Preco: 2 - Categoria: Netflix 
id Produto: 13 - Valor: $152.2 - Estrategia de Preco: 2 - Categoria: Ticket - Museu 
id Produto: 48 - Valor: $853.99 - Estrategia de Preco: 1 - Categoria: GloboPlay 
id Produto: 456 - Valor: $789.25 - Estrategia de Preco: 2 - Categoria: GloboPlay
```

criando uma Transação:
```
transacao_1 = Transacao(c1, pd2, sistema_pc, hora_transacao)
```
imprimindo a Transação:
```
Cliente:
Id: 9581 - Nome: Claus - Valor em Conta: 100.25

Produto:
id: 8 - Valor: $69.52 - Estrategia de Preco: 2 - Categoria: Netflix

Hardware:
Provedor: 2 - canal: 3
```
Ao final, usaremos o método `getData()` (que vai retornar todos as transações e suas informações) da classe `Transacao` como método formatador dos dados.

Estas listas serão utilizadas para criar um tabela, similar a uma tabela excel, chamada *dataframe*.

### Dataframe e Pandas

Um *dataframe* é semelhante a uma matriz, contudo as suas colunas possuem significado, ou seja, têm nomes, e cada coluna pode ser um tipo de dado diferente. Em outras palavras, um *dataframe* pode ser visto como uma tabela de uma base de dados, em que cada linha corresponde a um registo (linha) da tabela.

Para criar um *dataframe* vamos utilizar uma framework chamado [**Pandas**](https://pt.wikipedia.org/wiki/Pandas_(software)), que "é uma biblioteca de software criada para a linguagem Python para manipulação e análise de dados". Com a ferramenta, conseguiremos usar estruturas e operações para manipular tabelas numéricas e séries temporais.

Para **criar um dataframe e inserir estes dados** com Pandas podemos usar este [arquivo](https://github.com/dunfrey/Project_OOPClass/blob/main/comandos_pandas.py) como referência, mas é possível encontrar vários outros tutoriais e manuais sobre como usar o Pandas. No arquivo, as linhas 6~23 mostram como podemos criar o dataframe e inserir dados:
1. obtemos as colunas da tabela (linha 6), que são as informações de uma única transacao
```
lista_de_colunas= ['Transacao', 'Usuario', 'Provedor', 'Produto', 'Categoria do Produto', 'Canal', 'Valor Conta Cliente', 'Valor do Servico', 'Data/Hora', 'Estrategia Preco Produto', 'Fraude']
```
2. criamos uma nova lista, que irá agrupar todas as transações (linha 19), e inserimos todos os registros na nova lista criada (linha 20)
```
pacote_de_transacoes = list()
pacote_de_transacoes.append(transacao_1.getData())
```
3. Executamos o comando para criar um dataframe vazio e inserir a lista de transações como dados do *dataframe* (linha 23)
```
df = pd.DataFrame(pacote_de_transacoes, columns = lista_de_colunas) 
```

> ### IMPORTANTE
> Para entrega desta primeira etapa, além do código, também deve ser entregue o diagrama de classes.

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

Geralmente, a distribuição desses dados em uma tabela é muito dificil de observar a olho humano, porque são muitos dados, distribuídos em  linhas e muitas colunas.

Para melhor compreensão os dados, 4 (quatro) gráficos podem ser utilizados:
- [**Gráfico de dipersão**](https://pt.wikipedia.org/wiki/Gr%C3%A1fico_de_dispers%C3%A3o): verifica se existe correlação. Coloca um ponto em plano cartesiano usando duas variáves;
- [**Histograma**](https://pt.wikipedia.org/wiki/Histograma): usado para entender a distribuição do conjunto de dados. Representa as variáveis em forma de barras;
- [**Dagrama de caixas**](https://pt.wikipedia.org/wiki/Diagrama_de_caixa): também usado para entender a distribuição dos dados, entendendo a concentração de valores de cada atributo;
- [**FDA**](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_distribui%C3%A7%C3%A3o_acumulada) (Função de distribuição acumulada): usado para saber qual a probabilidade de um valor ser igual ou superior a um determinado valor.

Estes quatro gráficos devem implementados neste trabalho, e deve ser permitido a seleção de quais atributos queremos analisar.

Você pode verificar alguns comandos de manipulação de dataframe  e gerar os gráficos [neste arquivo](https://github.com/dunfrey/OOP_ProjectClass/blob/main/comandos_pandas.py) ou acessar o site [Pandas](https://pandas.pydata.org/docs/index.html).

A seguir, um exemplo de gráfico histograma gerado:

<img src="https://github.com/dunfrey/OOP_ProjectClass/blob/main/fig2.png" width="700">




**Reaproveite código!!! Não escreva um mesmo bloco de código em diferente partes do artefato**

Essa abordagem mantém o tamanho reduzido e facilita a leitura e manutenção do código.
