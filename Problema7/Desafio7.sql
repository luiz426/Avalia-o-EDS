CREATE TABLE stg_atendimentos (
    atendimento_id INT PRIMARY KEY,
    paciente_id INT,
    data_atendimento DATE,
    medico_id INT
);

CREATE TABLE stg_exames_solicitados (
    exame_id INT PRIMARY KEY,
    atendimento_id INT,
    tipo_exame VARCHAR(255),
    data_solicitacao DATE,
    FOREIGN KEY (atendimento_id) REFERENCES stg_atendimentos(atendimento_id)
);
