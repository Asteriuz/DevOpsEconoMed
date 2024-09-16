# Sistema de Gestão de Clínicas - API

Este projeto é uma API desenvolvida em Python usando o framework FastAPI. A API gerencia informações de unidades de saúde, médicos, clientes e seus respectivos dados, como endereços, históricos de saúde, e comorbidades.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Asteriuz/DevOpsEconoMed
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para sistemas Linux/MacOS
   .\venv\Scripts\activate  # Para sistemas Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie a aplicação:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints

### Cidades

- `GET /cidades/`: Retorna todas as cidades cadastradas.
- `GET /cidades/{cidade_id}`: Retorna uma cidade específica pelo ID.
- `GET /cidades/estado/{estado_id/`: Retorna todas as cidades de um estado específico.
- `POST /cidades/`: Cria uma nova cidade.
- `PUT /cidades/{cidade_id}`: Atualiza os dados de uma cidade existente.
- `DELETE /cidades/{cidade_id}`: Deleta uma cidade.

### Estados

- `GET /estados/`: Retorna todos os estados cadastrados.
- `GET /estados/{estado_id}`: Retorna um estado específico pelo ID.
- `POST /estados/`: Cria um novo estado.
- `PUT /estados/{estado_id}`: Atualiza os dados de um estado existente.
- `DELETE /estados/{estado_id}`: Deleta um estado.

### Unidades

- `GET /unidades/`: Retorna todas as unidades cadastradas.
- `GET /unidades/{unidade_id}`: Retorna uma unidade específica pelo ID.
- `POST /unidades/`: Cria uma nova unidade.
- `PUT /unidades/{unidade_id}`: Atualiza os dados de uma unidade existente.
- `DELETE /unidades/{unidade_id}`: Deleta uma unidade.

### Endereços de Unidades

- `GET /enderecos_unidade/`: Retorna todos os endereços de unidades.
- `GET /enderecos_unidade/{endereco_unidade_id}`: Retorna um endereço de unidade específico pelo ID.
- `POST /enderecos_unidade/`: Cria um novo endereço de unidade.
- `PUT /enderecos_unidade/{endereco_unidade_id}`: Atualiza os dados de um endereço de unidade existente.
- `DELETE /enderecos_unidade/{endereco_unidade_id}`: Deleta um endereço de unidade.

### Médicos

- `GET /medicos/`: Retorna todos os médicos cadastrados.
- `GET /medicos/{medico_id}`: Retorna um médico específico pelo ID.
- `POST /medicos/`: Cria um novo médico.
- `PUT /medicos/{medico_id}`: Atualiza os dados de um médico existente.
- `DELETE /medicos/{medico_id}`: Deleta um médico.

### Clientes

- `GET /clientes/`: Retorna todos os clientes cadastrados.
- `GET /clientes/{cliente_id}`: Retorna um cliente específico pelo ID.
- `POST /clientes/`: Cria um novo cliente.
- `PUT /clientes/{cliente_id}`: Atualiza os dados de um cliente existente.
- `DELETE /clientes/{cliente_id}`: Deleta um cliente.

### Endereços de Clientes

- `GET /enderecos_cliente/`: Retorna todos os endereços dos clientes.
- `GET /enderecos_cliente/{endereco_cliente_id}`: Retorna um endereço específico pelo ID.
- `POST /enderecos_cliente/`: Cria um novo endereço de cliente.
- `PUT /enderecos_cliente/{endereco_cliente_id}`: Atualiza os dados de um endereço de cliente existente.
- `DELETE /enderecos_cliente/{endereco_cliente_id}`: Deleta um endereço de cliente.

### Comorbidades

- `GET /comorbidades/`: Retorna todas as comorbidades cadastradas.
- `GET /comorbidades/{comorbidade_id}`: Retorna uma comorbidade específica pelo ID.
- `POST /comorbidades/`: Cria uma nova comorbidade.
- `PUT /comorbidades/{comorbidade_id}`: Atualiza os dados de uma comorbidade existente.
- `DELETE /comorbidades/{comorbidade_id}`: Deleta uma comorbidade.

### Históricos de Saúde dos Clientes

- `GET /historicos_saude_cliente/`: Retorna todos os históricos de saúde dos clientes.
- `GET /historicos_saude_cliente/{historico_saude_cliente_id}`: Retorna um histórico de saúde específico pelo ID.
- `POST /historicos_saude_cliente/`: Cria um novo histórico de saúde de cliente.
- `PUT /historicos_saude_cliente/{historico_saude_cliente_id}`: Atualiza os dados de um histórico de saúde existente.
- `DELETE /historicos_saude_cliente/{historico_saude_cliente_id}`: Deleta um histórico de saúde.

### Históricos Hospitalares dos Clientes

- `GET /historicos_hospital_cliente/`: Retorna todos os históricos hospitalares dos clientes.
- `GET /historicos_hospital_cliente/{historico_hospital_cliente_id}`: Retorna um histórico hospitalar específico pelo ID.
- `POST /historicos_hospital_cliente/`: Cria um novo histórico hospitalar de cliente.
- `PUT /historicos_hospital_cliente/{historico_hospital_cliente_id}`: Atualiza os dados de um histórico hospitalar existente.
- `DELETE /historicos_hospital_cliente/{historico_hospital_cliente_id}`: Deleta um histórico hospitalar.

## Estrutura do Projeto

```bash
.
├── requests
│   ├── EconomedAzurePostman.json  # Importar para o Postman
│   └── EconomedAzureThunderCliente.json  # Importar para o Thunder Client
├── .env     # Arquivo de configuração do ambiente
├── Documentação DevOps - Sprint 3   # Documentação do DevOps
├── main.py         # Arquivo principal da aplicação FastAPI
├── requirements.txt    # Arquivo com as dependências do projeto
└── README.md           # Este arquivo
```
