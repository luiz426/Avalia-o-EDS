SELECT cpf, COUNT(*) AS quantidade FROM stg_prontuario.paciente
GROUP BY cpf
HAVING COUNT(*) > 1;
