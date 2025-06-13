# Avaliação-desafios-EDS

Comentários pertinentes aos desafios realizados

## Problema 1 

Realizei a criação da tabela ```stg_prontuario.paciente``` de forma sua estrutura se mantivesse compatível com os dados originais, evitando possiveis conflitos durante a integração dos dados solicitados. Depois de realizar a criação da tabela executei os comandos de inserção dos dados a partir dos schemas dos hospitais solicitados, fazendo assim a inserção dos dados dos três hospitais na tabela paciente como solicitado.

Obs: Foi feito uma pequena mudança na estrutura da tabela de pacientes, visto que o ```int``` da estrutura da tabela usado para a inserção do cpf estava limitando sua introdução, visto que o cpf possui 11 números e o ```int``` estava bloqueando a entrada dos dados, realizei a mudança do ```int``` para o ```char``` que é a melhor abordagem para o uso do cpf já que os números terão tamanho fixo.

## Problema 2

Desenvolvi os comandos de inserção dos multiplos dados dos schemas dos hospitais para a tabela paciente, utilizei os comandos ``` INSERT INTO ``` e ```SELECT``` para a realização da inserção, executei os comandos de maneira distinta para cada schema hospitalar, isso para uma maior clareza e controle. Esse é um comando simples e eficiente que resolve o problema 2.

## Problema 3 

A solução que desenvolvi para o problema 3 foi utilizando o uso do ```select``` juntamente com a função de agregação ```count(*)``` para realizar a contagem das ocorreências fazendo a identificação dos cpfs repetidos, foi utulizado a cláusula ```having``` para aplicar de forma correta os os filtros após o uso do ```group by```, vale mencionar realizei a nomeação dos ```count(*)```para 'quantidade' para um melhor entendimento do que foi solicitado.

## Problema 4

O código para a resolução do problema 4 foi utilizado a função ```row_number``` juntamente com o ```partition by``` para realizar a enumeração dos registros de cada cpf, após isso o ```order by``` faz com que os registros recentes tenham o número 1, a cláusula ```where``` filtra apenas o mais recente de cada cpf. Todo esse comando faz com que a solução seja eficiente e entendível resolvendo o problema proposto.

## Problema 5

O código python que desenvolvi para a resolução do problema 5 solicitado realiza leitura dos arquivos ```_layout.txt``` que faz a definição das colunas como posição final, inicial e os tipos de dados. permitindo que script feito seja adaptável a mudanças futuras, com isso é garantido que os campos das tabelas sejam interpretados de acordo com o layout oficial. 

A função ```create_table``` realiza a criação de tabelas dinâmicas usando os metadados do layout, isso elimina a necessidade de criar as tabelas manualmente. 

Utilizei função ```load_data``` que garente com que apenas os registros validos sejam inseridos evitando problemas de consistência. 

Defini uma ordem de prioridade no envio dos dados para as tabelas do banco de dados utilizado, isso foi feito devido a erros e falhas de ```foreign key``` garantindo que as dependências sejam respeitadas.

O código realiza a leitura dos layouts SIGTAP, cria as tabelas de forma dinâmica utilizando como referência o padrão DATASUS fornecido, lê os arquivos de dados corretamente, mantém a integrdade referêncial entre as tabelas e realiza a automatização de todo o processo de carga para o schema staging solicitado pelo problema 5.

Obs: Para todo o processo de realização do problema 5, foi utilizado o banco de dados ```mysql``` como referência para a criação de tabelas, envio dos dados e realização de testes.

## Problema 6

O código para a realização do problema 6 foca no objetivo do problema proposto, defini a latitude e longitude exata das coordenadas do rio de janeiro, realizei a montagem da URL da api com os parâmetros necessários para trazer a pressão atmosférica por hora utilizando ```hourly=surface_pressure```. Após isso realizei a extração dos dados solicitados e atráves disso fiz a inserção desses dados em um banco de dados mysql local. 

## Problema 7

Para a resolução do problema 7 realizei a modelagem da estrutura das tabelas ```stg_atendimentos``` e ```stg_exames_solicitados```, fiz a estruturação das tabelas interligado a tabela principal ```stg_atendimento``` com a tabela dependente ```stg_exames_solicitados```, criando assim as foreign com referências corretas respeitando a relação de 1:N solicitada, garantido a integridade e o correta estruturação dos dados.

## Problema 8 

Para o problema 8 fiz uma consulta utilizando uma subconsulta para realizar a contagem de quantas prescrições cada atendimento do tipo de urgência (U) possui, a consulta principal faz o calculo da média das contagens e arrendonda com o uso do ```ROUND``` para 2 casas decimais.

## Problema 9 

Para solucionar o problema nove utilizei a classe ```counter``` que tem a função de realizar a contagem de quantas vezes cada elemento aparece em uma sequência, após isso fiz a comparação direta para cada medicamento da prescrição e logo depois os exemplos de teste.

## Problema 10 







