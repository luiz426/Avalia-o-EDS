# Avaliação dos Desafios – EDS

Comentários pertinentes aos desafios realizados

## Problema 1

Realizei a criação da tabela `stg_prontuario.paciente` de forma que sua estrutura permanecesse compatível com os dados originais, evitando possíveis conflitos durante a integração dos dados solicitados. Após a criação da tabela, executei os comandos de inserção dos dados a partir dos schemas dos hospitais mencionados, inserindo os dados dos três hospitais na tabela `paciente`, conforme solicitado.

**Observação:** Foi feita uma pequena alteração na estrutura da tabela de pacientes, pois o tipo `INT` utilizado para armazenar o CPF limitava sua inserção. Considerando que o CPF possui 11 dígitos, o `INT` não comportava esse valor adequadamente. Por isso, alterei o tipo para `CHAR`, que é uma abordagem mais apropriada, já que os números possuem tamanho fixo.

## Problema 2

Desenvolvi os comandos de inserção dos múltiplos dados dos schemas hospitalares para a tabela `paciente`, utilizando os comandos `INSERT INTO` e `SELECT`. Realizei a inserção de forma separada para cada schema hospitalar, a fim de proporcionar maior clareza e controle. Essa abordagem, simples e eficiente, resolve corretamente o problema 2.

## Problema 3

A solução que desenvolvi para o problema 3 utilizou o comando `SELECT` em conjunto com a função de agregação `COUNT(*)` para realizar a contagem das ocorrências, identificando os CPFs duplicados. Utilizei a cláusula `HAVING` para aplicar os filtros de forma correta após o uso do `GROUP BY`. Vale mencionar que nomeei o `COUNT(*)` como `quantidade`, para facilitar a compreensão do resultado.

## Problema 4

No problema 4, utilizei a função `ROW_NUMBER()` combinada com `PARTITION BY` para enumerar os registros de cada CPF. Em seguida, o `ORDER BY` garantiu que os registros mais recentes fossem atribuídos com o número 1. Por fim, a cláusula `WHERE` foi utilizada para filtrar apenas o registro mais recente de cada CPF. Esse comando torna a solução eficiente e compreensível, atendendo ao que foi proposto.

## Problema 5

O código Python que desenvolvi para a resolução do problema 5 realiza a leitura dos arquivos `_layout.txt`, que definem as colunas (posição inicial, posição final e tipos de dados). Isso torna o script adaptável a futuras alterações, garantindo que os campos das tabelas sejam interpretados conforme o layout oficial.

A função `create_table` cria tabelas de forma dinâmica a partir dos metadados do layout, eliminando a necessidade de criação manual.

Utilizei também a função `load_data`, que assegura que apenas os registros válidos sejam inseridos, evitando problemas de consistência.

Defini uma ordem de prioridade na carga dos dados para as tabelas do banco, a fim de evitar erros de chave estrangeira (`foreign key`), garantindo o respeito às dependências entre elas.

O código, portanto:

* Lê corretamente os layouts do SIGTAP,
* Cria as tabelas dinamicamente seguindo o padrão do DATASUS,
* Realiza a leitura dos arquivos de dados corretamente,
* Mantém a integridade referencial entre as tabelas,
* Automatiza todo o processo de carga para o schema `staging`.

**Observação:** Todo o processo foi realizado utilizando o banco de dados MySQL como referência para criação, testes e carga de dados.

## Problema 6

A solução para o problema 6 foi focada no objetivo proposto. Defini as coordenadas exatas (latitude e longitude) da cidade do Rio de Janeiro e montei a URL da API com os parâmetros necessários para trazer os dados de pressão atmosférica por hora, utilizando `hourly=surface_pressure`. Após isso, extraí os dados solicitados e realizei a inserção em um banco de dados MySQL local.

## Problema 7

Para a resolução do problema 7, modelei as tabelas `stg_atendimentos` e `stg_exames_solicitados`, estruturando-as de forma que a tabela `stg_exames_solicitados` estivesse corretamente relacionada à tabela principal `stg_atendimentos`, por meio de chaves estrangeiras. Isso garantiu a relação de 1\:N conforme solicitado, assegurando a integridade e a estrutura correta dos dados.

## Problema 8

No problema 8, desenvolvi uma consulta utilizando subconsulta para contar quantas prescrições cada atendimento do tipo urgência (`U`) possui. A consulta principal calcula a média dessas contagens e utiliza a função `ROUND` para arredondar o resultado para duas casas decimais.

## Problema 9

Para solucionar o problema 9, utilizei a classe `Counter`, que tem a função de contar quantas vezes cada elemento aparece em uma sequência. Após isso, comparei diretamente os medicamentos das prescrições, seguido da inclusão de exemplos de teste.

## Problema 10

Neste problema, desenvolvi a função `gerar_grafico(lista_datas, nome_arquivo)`, estruturando-a com parâmetros reutilizáveis que permitem aplicá-la a diferentes conjuntos de dados, promovendo melhor organização. Novamente utilizei `Counter` para processar os dados e contar as ocorrências de cada data. Implementei também `tight_layout()` para evitar sobreposição de elementos no gráfico e utilizei `savefig()` como medida importante para evitar acúmulo de memória em aplicações que geram múltiplos gráficos.
