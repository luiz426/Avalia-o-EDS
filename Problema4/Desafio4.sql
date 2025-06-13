WITH pacientes_ordenados AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY cpf
               ORDER BY dt_atualizacao DESC
           ) AS ordem
    FROM stg_prontuario.paciente
)
SELECT id, nome, dt_nascimento, cpf, nome_mae, dt_atualizacao
FROM pacientes_ordenados
WHERE ordem = 1;

