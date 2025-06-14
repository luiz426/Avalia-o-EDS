# Avaliação dos Desafios – EDS

Comentários pertinentes aos desafios realizados

**Observação:** Todo o processo foi realizado utilizando o banco de dados MySQL como referência para criação, testes e carga de dados.

## Problema 1

Realizei a criação da tabela `stg_prontuario.paciente` de forma que sua estrutura permanecesse compatível com os dados originais, evitando possíveis conflitos durante a integração dos dados solicitados. Após a criação da tabela, executei os comandos de inserção dos dados a partir dos schemas dos hospitais mencionados, inserindo os dados dos três hospitais na tabela `paciente`, conforme solicitado.

**Observação:** Foi feita uma pequena alteração na estrutura da tabela de pacientes, pois o tipo `INT` utilizado para armazenar o CPF limitava sua inserção. Considerando que o CPF possui 11 dígitos, o `INT` não comportava esse valor adequadamente. Por isso, alterei o tipo para `CHAR`, que é uma abordagem mais apropriada, já que os números possuem tamanho fixo.

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

## Problema 6

Defini as coordenadas exatas (latitude e longitude) da cidade do Rio de Janeiro e montei a URL da API com os parâmetros necessários para trazer os dados de pressão atmosférica por hora, utilizando `hourly=surface_pressure`. Após isso, extraí os dados solicitados e realizei a inserção em um banco de dados MySQL local.

## Problema 9

Para solucionar o problema 9, utilizei a classe `Counter`, que tem a função de contar quantas vezes cada elemento aparece em uma sequência. Após isso, comparei diretamente os medicamentos das prescrições, seguido da inclusão de exemplos de teste.

## Problema 10

Neste problema, desenvolvi a função `gerar_grafico(lista_datas, nome_arquivo)`, estruturando-a com parâmetros reutilizáveis que permitem aplicá-la a diferentes conjuntos de dados, promovendo melhor organização. Novamente utilizei `Counter` para processar os dados e contar as ocorrências de cada data. Implementei também `tight_layout()` para evitar sobreposição de elementos no gráfico e utilizei `savefig()` como medida importante para evitar acúmulo de memória em aplicações que geram múltiplos gráficos.
