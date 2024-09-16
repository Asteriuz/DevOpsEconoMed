INSERT INTO
    CP1_ESTADO (NOME)
VALUES
    ('São Paulo');

INSERT INTO
    CP1_ESTADO (NOME)
VALUES
    ('Rio de Janeiro');

INSERT INTO
    CP1_ESTADO (NOME)
VALUES
    ('Minas Gerais');

INSERT INTO
    CP1_ESTADO (NOME)
VALUES
    ('Paraná');

INSERT INTO
    CP1_ESTADO (NOME)
VALUES
    ('Santa Catarina');

INSERT INTO
    CP1_CIDADE (NOME, ESTADO_ID)
VALUES
    ('São Paulo', 1);

INSERT INTO
    CP1_CIDADE (NOME, ESTADO_ID)
VALUES
    ('Rio de Janeiro', 2);

INSERT INTO
    CP1_CIDADE (NOME, ESTADO_ID)
VALUES
    ('Belo Horizonte', 3);

INSERT INTO
    CP1_CIDADE (NOME, ESTADO_ID)
VALUES
    ('Curitiba', 4);

INSERT INTO
    CP1_CIDADE (NOME, ESTADO_ID)
VALUES
    ('Florianópolis', 5);

INSERT INTO
    CP1_EMPRESA (CNPJ, NOME, TIPO, TELEFONE, EMAIL)
VALUES
    (
        '12345678901234',
        'Empresa X',
        'Saúde',
        '11223344',
        'empresa.x@email.com'
    );

INSERT INTO
    CP1_EMPRESA (CNPJ, NOME, TIPO, TELEFONE, EMAIL)
VALUES
    (
        '98765432109876',
        'Empresa Y',
        'Saúde',
        '55443322',
        'empresa.y@email.com'
    );

INSERT INTO
    CP1_EMPRESA (CNPJ, NOME, TIPO, TELEFONE, EMAIL)
VALUES
    (
        '98765432101234',
        'Empresa Z',
        'Saúde',
        '55443311',
        'empresa.y@email.com'
    );

INSERT INTO
    CP1_EMPRESA (CNPJ, NOME, TIPO, TELEFONE, EMAIL)
VALUES
    (
        '98765432101235',
        'Empresa G',
        'Saúde',
        '55444411',
        'empresa.y@email.com'
    );

INSERT INTO
    CP1_EMPRESA (CNPJ, NOME, TIPO, TELEFONE, EMAIL)
VALUES
    (
        '98765432102222',
        'Empresa H',
        'Saúde',
        '88443311',
        'empresa.y@email.com'
    );

INSERT INTO
    CP1_CONVENIO (
        EMPRESA_ID,
        NOME,
        VALOR,
        TIPO_SERVICO,
        COBERTURA,
        CONTATO,
        VALIDADE
    )
VALUES
    (
        1,
        'Convenio A',
        500.00,
        'Consulta Médica',
        'Consultas e exames básicos',
        'contato@convenioa.com',
        '2025-12-31'
    );

INSERT INTO
    CP1_CONVENIO (
        EMPRESA_ID,
        NOME,
        VALOR,
        TIPO_SERVICO,
        COBERTURA,
        CONTATO,
        VALIDADE
    )
VALUES
    (
        2,
        'Convenio B',
        800.00,
        'Consulta e Exames',
        'Consultas, exames básicos e especializados',
        'contato@conveniob.com',
        '2026-06-30'
    );

INSERT INTO
    CP1_CONVENIO (
        EMPRESA_ID,
        NOME,
        VALOR,
        TIPO_SERVICO,
        COBERTURA,
        CONTATO,
        VALIDADE
    )
VALUES
    (
        2,
        'Convenio B',
        600.00,
        'Consulta e Exames',
        'Consultas, exames básicos e especializados',
        'contato@conveniob.com',
        '2026-06-30'
    );

INSERT INTO
    CP1_CONVENIO (
        EMPRESA_ID,
        NOME,
        VALOR,
        TIPO_SERVICO,
        COBERTURA,
        CONTATO,
        VALIDADE
    )
VALUES
    (
        3,
        'Convenio C',
        700.00,
        'Cirurgia',
        'Procedimentos cirúrgicos e acompanhamento pós-operatório',
        'contato@convenioc.com',
        '2027-01-15'
    );

INSERT INTO
    CP1_CONVENIO (
        EMPRESA_ID,
        NOME,
        VALOR,
        TIPO_SERVICO,
        COBERTURA,
        CONTATO,
        VALIDADE
    )
VALUES
    (
        4,
        'Convenio D',
        800.00,
        'Fisioterapia',
        'Sessões de fisioterapia e acompanhamento especializado',
        'contato@conveniod.com',
        '2026-12-31'
    );

INSERT INTO
    CP1_AREA_ATUACAO (NOME)
VALUES
    ('Cardiologia');

INSERT INTO
    CP1_AREA_ATUACAO (NOME)
VALUES
    ('Clínica Geral');

INSERT INTO
    CP1_AREA_ATUACAO (NOME)
VALUES
    ('Pediatria');

INSERT INTO
    CP1_AREA_ATUACAO (NOME)
VALUES
    ('Ortopedia');

INSERT INTO
    CP1_AREA_ATUACAO (NOME)
VALUES
    ('Ginecologia');

INSERT INTO
    CP1_UNIDADE (
        EMPRESA_ID,
        NOME,
        TELEFONE,
        EMAIL,
        TIPO,
        CAPACIDADE,
        AREA_ATUACAO_ID
    )
VALUES
    (
        1,
        'Unidade A',
        '11223344',
        'unidade.a@email.com',
        'Hospital',
        100,
        1
    );

INSERT INTO
    CP1_UNIDADE (
        EMPRESA_ID,
        NOME,
        TELEFONE,
        EMAIL,
        TIPO,
        CAPACIDADE,
        AREA_ATUACAO_ID
    )
VALUES
    (
        2,
        'Unidade B',
        '55443322',
        'unidade.b@email.com',
        'Hospital',
        150,
        2
    );

INSERT INTO
    CP1_UNIDADE (
        EMPRESA_ID,
        NOME,
        TELEFONE,
        EMAIL,
        TIPO,
        CAPACIDADE,
        AREA_ATUACAO_ID
    )
VALUES
    (
        2,
        'Unidade B',
        '22334455',
        'unidade.b@email.com',
        'Clínica',
        50,
        3
    );

INSERT INTO
    CP1_UNIDADE (
        EMPRESA_ID,
        NOME,
        TELEFONE,
        EMAIL,
        TIPO,
        CAPACIDADE,
        AREA_ATUACAO_ID
    )
VALUES
    (
        3,
        'Unidade C',
        '33445566',
        'unidade.c@email.com',
        'Consultório',
        20,
        4
    );

INSERT INTO
    CP1_UNIDADE (
        EMPRESA_ID,
        NOME,
        TELEFONE,
        EMAIL,
        TIPO,
        CAPACIDADE,
        AREA_ATUACAO_ID
    )
VALUES
    (
        4,
        'Unidade D',
        '44556677',
        'unidade.d@email.com',
        'Laboratório',
        30,
        5
    );

INSERT INTO
    CP1_ENDERECO_UNIDADE (UNIDADE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (1, 'Rua da Unidade A', '789', '54321-098', 1);

INSERT INTO
    CP1_ENDERECO_UNIDADE (UNIDADE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (2, 'Rua da Unidade B', '101', '98765-432', 2);

INSERT INTO
    CP1_ENDERECO_UNIDADE (UNIDADE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (3, 'Avenida Principal', '200', '12345-678', 3);

INSERT INTO
    CP1_ENDERECO_UNIDADE (UNIDADE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (4, 'Rua da Unidade D', '50', '54321-876', 4);

INSERT INTO
    CP1_ENDERECO_UNIDADE (UNIDADE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (5, 'Avenida Central', '300', '13579-246', 5);

INSERT INTO
    CP1_MEDICO (NOME, TELEFONE, EMAIL, ESPECIALIDADE, CRM)
VALUES
    (
        'Dr. José Santos',
        '11223344',
        'jose.santos@email.com',
        'Cardiologia',
        '12345'
    );

INSERT INTO
    CP1_MEDICO (NOME, TELEFONE, EMAIL, ESPECIALIDADE, CRM)
VALUES
    (
        'Dra. Ana Oliveira',
        '55443322',
        'ana.oliveira@email.com',
        'Clínica Geral',
        '54321'
    );

INSERT INTO
    CP1_MEDICO (NOME, TELEFONE, EMAIL, ESPECIALIDADE, CRM)
VALUES
    (
        'Dr. Marcos Santos',
        '99887766',
        'marcos.santos@email.com',
        'Ortopedia',
        '12345'
    );

INSERT INTO
    CP1_MEDICO (NOME, TELEFONE, EMAIL, ESPECIALIDADE, CRM)
VALUES
    (
        'Dra. Carolina Mendes',
        '77665544',
        'carolina.mendes@email.com',
        'Pediatria',
        '54321'
    );

INSERT INTO
    CP1_MEDICO (NOME, TELEFONE, EMAIL, ESPECIALIDADE, CRM)
VALUES
    (
        'Dr. Pedro Alves',
        '33221100',
        'pedro.alves@email.com',
        'Cardiologia',
        '67890'
    );

INSERT INTO
    CP1_MEDICO_UNIDADE (MEDICO_ID, UNIDADE_ID, HORARIO_ATENDIMENTO)
VALUES
    (1, 1, 'Segunda a Sexta, 08:00 - 17:00');

INSERT INTO
    CP1_MEDICO_UNIDADE (MEDICO_ID, UNIDADE_ID, HORARIO_ATENDIMENTO)
VALUES
    (2, 2, 'Segunda a Sexta, 09:00 - 18:00');

INSERT INTO
    CP1_MEDICO_UNIDADE (MEDICO_ID, UNIDADE_ID, HORARIO_ATENDIMENTO)
VALUES
    (3, 3, 'Segunda a Sexta, 08:00 - 17:00');

INSERT INTO
    CP1_MEDICO_UNIDADE (MEDICO_ID, UNIDADE_ID, HORARIO_ATENDIMENTO)
VALUES
    (4, 4, 'Segunda a Sábado, 10:00 - 20:00');

INSERT INTO
    CP1_MEDICO_UNIDADE (MEDICO_ID, UNIDADE_ID, HORARIO_ATENDIMENTO)
VALUES
    (
        5,
        5,
        'Segunda a Quinta, 07:00 - 16:00; Sexta, 07:00 - 12:00'
    );

INSERT INTO
    CP1_ESTADO_CIVIL (NOME)
VALUES
    ('Solteiro');

INSERT INTO
    CP1_ESTADO_CIVIL (NOME)
VALUES
    ('Casado');

INSERT INTO
    CP1_ESTADO_CIVIL (NOME)
VALUES
    ('Divorciado');

INSERT INTO
    CP1_ESTADO_CIVIL (NOME)
VALUES
    ('Viúvo');

INSERT INTO
    CP1_CLIENTE (
        RG,
        NOME,
        SEXO,
        TELEFONE,
        EMAIL,
        DATA_NASCIMENTO,
        CPF,
        ESTADO_CIVIL_ID,
        CONVENIO_ID
    )
VALUES
    (
        '123456789',
        'João da Silva',
        'M',
        '11223344',
        'joao.silva@email.com',
        '1990-01-01',
        '123.456.789-00',
        1,
        1
    );

INSERT INTO
    CP1_CLIENTE (
        RG,
        NOME,
        SEXO,
        TELEFONE,
        EMAIL,
        DATA_NASCIMENTO,
        CPF,
        ESTADO_CIVIL_ID,
        CONVENIO_ID
    )
VALUES
    (
        '987654321',
        'Maria Souza',
        'F',
        '55443322',
        'maria.souza@email.com',
        '1985-05-10',
        '987.654.321-00',
        2,
        2
    );

INSERT INTO
    CP1_CLIENTE (
        RG,
        NOME,
        SEXO,
        TELEFONE,
        EMAIL,
        DATA_NASCIMENTO,
        CPF,
        ESTADO_CIVIL_ID,
        CONVENIO_ID
    )
VALUES
    (
        '123456789',
        'João Silva',
        'M',
        '99887766',
        'joao.silva@email.com',
        '1990-08-20',
        '123.456.789-00',
        3,
        1
    );

INSERT INTO
    CP1_CLIENTE (
        RG,
        NOME,
        SEXO,
        TELEFONE,
        EMAIL,
        DATA_NASCIMENTO,
        CPF,
        ESTADO_CIVIL_ID,
        CONVENIO_ID
    )
VALUES
    (
        '234567890',
        'Ana Oliveira',
        'F',
        '77665544',
        'ana.oliveira@email.com',
        '1980-03-15',
        '234.567.890-00',
        4,
        3
    );

INSERT INTO
    CP1_CLIENTE (
        RG,
        NOME,
        SEXO,
        TELEFONE,
        EMAIL,
        DATA_NASCIMENTO,
        CPF,
        ESTADO_CIVIL_ID,
        CONVENIO_ID
    )
VALUES
    (
        '345678901',
        'Carlos Pereira',
        'M',
        '33221100',
        'carlos.pereira@email.com',
        '1975-12-05',
        '345.678.901-00',
        4,
        4
    );

INSERT INTO
    CP1_ENDERECO_CLIENTE (CLIENTE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (1, 'Rua dos Clientes', '123', '12345-678', 1);

INSERT INTO
    CP1_ENDERECO_CLIENTE (CLIENTE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (2, 'Avenida das Flores', '456', '54321-098', 2);

INSERT INTO
    CP1_ENDERECO_CLIENTE (CLIENTE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (3, 'Rua das Palmeiras', '789', '12345-678', 3);

INSERT INTO
    CP1_ENDERECO_CLIENTE (CLIENTE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (4, 'Avenida Central', '101', '87654-321', 4);

INSERT INTO
    CP1_ENDERECO_CLIENTE (CLIENTE_ID, RUA, NUMERO, CEP, CIDADE_ID)
VALUES
    (5, 'Rua dos Girassóis', '222', '13579-246', 5);

INSERT INTO
    CP1_COMORBIDADE (NOME)
VALUES
    ('Hipertensão');

INSERT INTO
    CP1_COMORBIDADE (NOME)
VALUES
    ('Diabetes');

INSERT INTO
    CP1_COMORBIDADE (NOME)
VALUES
    ('Asma');

INSERT INTO
    CP1_COMORBIDADE (NOME)
VALUES
    ('Depressão');

INSERT INTO
    CP1_COMORBIDADE (NOME)
VALUES
    ('Obesidade');

INSERT INTO
    CP1_HISTORICO_SAUDE_CLIENTE (
        CLIENTE_ID,
        COMORBIDADE_ID,
        DATA_REGISTRO,
        FUMA,
        OBSERVACOES
    )
VALUES
    (1, 1, '2020-01-01', 0, 'Sem observações');

INSERT INTO
    CP1_HISTORICO_SAUDE_CLIENTE (
        CLIENTE_ID,
        COMORBIDADE_ID,
        DATA_REGISTRO,
        FUMA,
        OBSERVACOES
    )
VALUES
    (2, 2, '2021-03-15', 1, 'Sem observações');

INSERT INTO
    CP1_HISTORICO_SAUDE_CLIENTE (
        CLIENTE_ID,
        COMORBIDADE_ID,
        DATA_REGISTRO,
        FUMA,
        OBSERVACOES
    )
VALUES
    (
        3,
        3,
        '2022-01-10',
        0,
        'Cliente tem episódios ocasionais de asma'
    );

INSERT INTO
    CP1_HISTORICO_SAUDE_CLIENTE (
        CLIENTE_ID,
        COMORBIDADE_ID,
        DATA_REGISTRO,
        FUMA,
        OBSERVACOES
    )
VALUES
    (
        4,
        4,
        '2022-05-20',
        1,
        'Cliente está sob medicação para controle da pressão arterial'
    );

INSERT INTO
    CP1_HISTORICO_SAUDE_CLIENTE (
        CLIENTE_ID,
        COMORBIDADE_ID,
        DATA_REGISTRO,
        FUMA,
        OBSERVACOES
    )
VALUES
    (
        5,
        5,
        '2023-09-05',
        0,
        'Cliente está em acompanhamento psicológico regular'
    );

INSERT INTO
    CP1_HISTORICO_HOSPITAL_CLIENTE (
        CLIENTE_ID,
        DATA_REGISTRO,
        HISTORICO_MEDICO,
        EXAMES_REALIZADOS,
        MEDICAMENTOS_PRESCRITOS,
        OBSERVACOES
    )
VALUES
    (
        1,
        '2022-01-01',
        'Cirurgia de apendicite em 2015',
        'Exames de rotina',
        'Paracetamol',
        'Nenhuma observação'
    );

INSERT INTO
    CP1_HISTORICO_HOSPITAL_CLIENTE (
        CLIENTE_ID,
        DATA_REGISTRO,
        HISTORICO_MEDICO,
        EXAMES_REALIZADOS,
        MEDICAMENTOS_PRESCRITOS,
        OBSERVACOES
    )
VALUES
    (
        2,
        '2023-07-20',
        'Internação por pneumonia',
        'Exames de sangue',
        'Antibióticos',
        'Nenhuma observação'
    );

INSERT INTO
    CP1_HISTORICO_HOSPITAL_CLIENTE (
        CLIENTE_ID,
        DATA_REGISTRO,
        HISTORICO_MEDICO,
        EXAMES_REALIZADOS,
        MEDICAMENTOS_PRESCRITOS,
        OBSERVACOES
    )
VALUES
    (
        3,
        '2022-05-10',
        'Cirurgia de emergência de apendicite',
        'Tomografia computadorizada, exames de sangue',
        'Analgésicos, antibióticos',
        'Recuperação satisfatória'
    );

INSERT INTO
    CP1_HISTORICO_HOSPITAL_CLIENTE (
        CLIENTE_ID,
        DATA_REGISTRO,
        HISTORICO_MEDICO,
        EXAMES_REALIZADOS,
        MEDICAMENTOS_PRESCRITOS,
        OBSERVACOES
    )
VALUES
    (
        4,
        '2023-01-15',
        'Fratura de tornozelo',
        'Raio-X, ressonância magnética',
        'Analgésicos, anti-inflamatórios',
        'Cliente em reabilitação fisioterapêutica'
    );

INSERT INTO
    CP1_HISTORICO_HOSPITAL_CLIENTE (
        CLIENTE_ID,
        DATA_REGISTRO,
        HISTORICO_MEDICO,
        EXAMES_REALIZADOS,
        MEDICAMENTOS_PRESCRITOS,
        OBSERVACOES
    )
VALUES
    (
        5,
        '2023-09-30',
        'Infarto agudo do miocárdio',
        'Eletrocardiograma, angiografia coronariana',
        'Antiagregantes plaquetários, estatinas',
        'Cliente em monitoramento cardíaco regular'
    );

SELECT
    *
FROM
    CP1_CLIENTE;

SELECT
    C.NOME,
    CO.NOME
FROM
    CP1_CLIENTE C
    JOIN CP1_CONVENIO CO ON C.CONVENIO_ID = CO.ID;