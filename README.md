# Avalição-desafios-EDS

Comentários pertinentes aos desafios realizados

## Problema 1 

Realizei a criação da tabela 'stg_prontuario.paciente' de forma sua estrutura se mantivesse compatível com os dados originais, evitando possiveis conflitos durante a integração dos dados solicitados. Depois de realizar a criação da tabela executei os comandos de inserção dos dados a partir dos schemas dos hospitais solicitados, fazendo assim a inserção dos dados dos três hospitais na tabela paciente como solicitado.

Obs: Foi feito uma pequena mudança na estrutura da tabela de pacientes, visto que o ```int``` da estrutura da tabela usado para a inserção do cpf estava limitando sua introdução, visto que o cpf possui 11 números e o ```int``` estava bloqueando a entrada dos dados, realizei a mudança do ```int``` para o ```char``` que é a melhor abordagem para o uso do cpf já que os números terão tamanho fixo.

## Problema 2

Desenvolvi os comandos de inserção dos multiplos dados dos schemas dos hospitais para a tabela paciente, utilizei os comandos ``` INSERT INTO ``` e ```SELECT``` para a realização da inserção, executei os comandos de maneira distinta para cada schema hospitalar, isso para uma maior clareza e controle. Esse é um comando simples e eficiente que resolve o problema 2.

## Problema 3 

A solução que desenvolvi para o problema 3 foi utilizando o uso do ```select``` juntamente com a função de agregação ```count(*)``` para realizar a contagem das ocorreências fazendo a identificação dos cpfs repetidos, foi utulizado a cláusula ```having``` para aplicar de forma correta os os filtros após o uso do ```group by```, vale mencionar realizei a nomeação dos ```count(*)```para 'quantidade' para um melhor entendimento do que foi solicitado.

## Problema 4
