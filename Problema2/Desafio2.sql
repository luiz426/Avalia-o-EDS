INSERT INTO stg_prontuario.paciente
SELECT * FROM stg_hospital_a.paciente;

INSERT INTO stg_prontuario.paciente
SELECT * FROM stg_hospital_b.paciente
WHERE CPF != NOT NULL;

INSERT INTO stg_prontuario.paciente
SELECT * FROM stg_hospital_c.paciente;
