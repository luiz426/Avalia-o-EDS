SELECT 
    ROUND(AVG(qtd_prescricoes),2) AS media_medicamentos_urgencia
FROM (
    SELECT 
        a.id AS atendimento_id,
        COUNT(ap.id_prescricao) AS qtd_prescricoes
    FROM 
        ATENDIMENTO a
    JOIN 
        ATENDIMENTO_PRESCRICAO ap ON a.id = ap.id_atend
    WHERE 
        a.tp_atend = 'U'
    GROUP BY 
        a.id
) AS Teste;