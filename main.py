# main.py
from fastapi import FastAPI, Depends
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
    CHAR,
)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from decouple import config
from pydantic import BaseModel

# Configuração do banco de dados usando credenciais do .env
DATABASE_URL = f"mssql+pyodbc://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_SERVER')}/{config('DB_NAME')}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()


# Modelos de Tabelas
class Estado(Base):
    __tablename__ = "CP1_ESTADO"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(20))


class EstadoRequest(BaseModel):
    nome: str


class Cidade(Base):
    __tablename__ = "CP1_CIDADE"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(20))
    estado_id = Column(Integer, ForeignKey("CP1_ESTADO.id"))
    estado = relationship("Estado")


class CidadeRequest(BaseModel):
    nome: str
    estado_id: int


class Empresa(Base):
    __tablename__ = "CP1_EMPRESA"
    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(20), unique=True)
    nome = Column(String(100))
    tipo = Column(String(100))
    telefone = Column(String(20))
    email = Column(String(100))


class EmpresaRequest(BaseModel):
    cnpj: str
    nome: str
    tipo: str
    telefone: str
    email: str


class Convenio(Base):
    __tablename__ = "CP1_CONVENIO"
    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("CP1_EMPRESA.id"))
    nome = Column(String(100))
    valor = Column(Float)
    tipo_servico = Column(String(100))
    cobertura = Column(String(100))
    contato = Column(String(100))
    validade = Column(Date)
    empresa = relationship("Empresa")


class ConvenioRequest(BaseModel):
    empresa_id: int
    nome: str
    valor: float
    tipo_servico: str
    cobertura: str
    contato: str
    validade: str


class AreaAtuacao(Base):
    __tablename__ = "CP1_AREA_ATUACAO"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))


class AreaAtuacaoRequest(BaseModel):
    nome: str


class Unidade(Base):
    __tablename__ = "CP1_UNIDADE"
    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("CP1_EMPRESA.id"))
    area_atuacao_id = Column(Integer, ForeignKey("CP1_AREA_ATUACAO.id"))
    nome = Column(String(100))
    telefone = Column(String(20))
    email = Column(String(100))
    tipo = Column(String(100))
    capacidade = Column(Integer)
    empresa = relationship("Empresa")
    area_atuacao = relationship("AreaAtuacao")


class UnidadeRequest(BaseModel):
    empresa_id: int
    area_atuacao_id: int
    nome: str
    telefone: str
    email: str
    tipo: str
    capacidade: int


class EnderecoUnidade(Base):
    __tablename__ = "CP1_ENDERECO_UNIDADE"
    id = Column(Integer, primary_key=True, index=True)
    unidade_id = Column(Integer, ForeignKey("CP1_UNIDADE.id"), unique=True)
    rua = Column(String(100))
    numero = Column(String(10))
    cep = Column(String(20))
    cidade_id = Column(Integer, ForeignKey("CP1_CIDADE.id"))
    unidade = relationship("Unidade")
    cidade = relationship("Cidade")


class EnderecoUnidadeRequest(BaseModel):
    unidade_id: int
    rua: str
    numero: str
    cep: str
    cidade_id: int


class Medico(Base):
    __tablename__ = "CP1_MEDICO"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    telefone = Column(String(20))
    email = Column(String(100))
    especialidade = Column(String(100))
    crm = Column(String(20))


class MedicoRequest(BaseModel):
    nome: str
    telefone: str
    email: str
    especialidade: str
    crm: str


class MedicoUnidade(Base):
    __tablename__ = "CP1_MEDICO_UNIDADE"
    id = Column(Integer, primary_key=True, index=True)
    medico_id = Column(Integer, ForeignKey("CP1_MEDICO.id"), nullable=False)
    unidade_id = Column(Integer, ForeignKey("CP1_UNIDADE.id"), nullable=False)
    horario_atendimento = Column(String(100))
    medico = relationship("Medico")
    unidade = relationship("Unidade")


class MedicoUnidadeRequest(BaseModel):
    medico_id: int
    unidade_id: int
    horario_atendimento: str


class EstadoCivil(Base):
    __tablename__ = "CP1_ESTADO_CIVIL"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(20))


class EstadoCivilRequest(BaseModel):
    nome: str


class Cliente(Base):
    __tablename__ = "CP1_CLIENTE"
    id = Column(Integer, primary_key=True, index=True)
    rg = Column(String(20))
    nome = Column(String(100))
    sexo = Column(CHAR(1))
    telefone = Column(String(20))
    email = Column(String(100))
    data_nascimento = Column(Date)
    cpf = Column(String(20))
    convenio_id = Column(Integer, ForeignKey("CP1_CONVENIO.id"))
    estado_civil_id = Column(Integer, ForeignKey("CP1_ESTADO_CIVIL.id"))
    convenio = relationship("Convenio")
    estado_civil = relationship("EstadoCivil")


class ClienteRequest(BaseModel):
    rg: str
    nome: str
    sexo: str
    telefone: str
    email: str
    data_nascimento: str
    cpf: str
    convenio_id: int
    estado_civil_id: int


class EnderecoCliente(Base):
    __tablename__ = "CP1_ENDERECO_CLIENTE"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("CP1_CLIENTE.id"), unique=True)
    rua = Column(String(100))
    numero = Column(String(10))
    cep = Column(String(20))
    cidade_id = Column(Integer, ForeignKey("CP1_CIDADE.id"))
    cliente = relationship("Cliente")
    cidade = relationship("Cidade")


class EnderecoClienteRequest(BaseModel):
    cliente_id: int
    rua: str
    numero: str
    cep: str
    cidade_id: int


class Comorbidade(Base):
    __tablename__ = "CP1_COMORBIDADE"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))


class ComorbidadeRequest(BaseModel):
    nome: str


class HistoricoSaudeCliente(Base):
    __tablename__ = "CP1_HISTORICO_SAUDE_CLIENTE"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("CP1_CLIENTE.id"), unique=True)
    comorbidade_id = Column(Integer, ForeignKey("CP1_COMORBIDADE.id"))
    data_registro = Column(Date)
    fuma = Column(Integer)
    observacoes = Column(String(100))
    cliente = relationship("Cliente")
    comorbidade = relationship("Comorbidade")


class HistoricoSaudeClienteRequest(BaseModel):
    cliente_id: int
    comorbidade_id: int
    data_registro: str
    fuma: int
    observacoes: str


class HistoricoHospitalCliente(Base):
    __tablename__ = "CP1_HISTORICO_HOSPITAL_CLIENTE"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("CP1_CLIENTE.id"), unique=True)
    data_registro = Column(Date)
    historico_medico = Column(String(100))
    exames_realizados = Column(String(100))
    medicamentos_prescritos = Column(String(100))
    observacoes = Column(String(100))
    cliente = relationship("Cliente")


class HistoricoHospitalClienteRequest(BaseModel):
    cliente_id: int
    data_registro: str
    historico_medico: str
    exames_realizados: str
    medicamentos_prescritos: str
    observacoes: str


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/estados/")
def get_estados(db=Depends(get_db)):
    estados = db.query(Estado).all()
    return estados


@app.post("/estados/")
def create_estado(estado: EstadoRequest, db=Depends(get_db)):
    novo_estado = Estado(nome=estado.nome)
    db.add(novo_estado)
    db.commit()
    db.refresh(novo_estado)
    return novo_estado


@app.get("/estados/{estado_id}")
def get_estado(estado_id: int, db=Depends(get_db)):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    return estado


@app.put("/estados/{estado_id}")
def update_estado(estado_id: int, estado: EstadoRequest, db=Depends(get_db)):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    estado.nome = estado.nome
    db.commit()
    db.refresh(estado)
    return estado


@app.delete("/estados/{estado_id}")
def delete_estado(estado_id: int, db=Depends(get_db)):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    db.delete(estado)
    db.commit()
    return {"message": "Estado deletado com sucesso"}


@app.get("/cidades/")
def get_cidades(db=Depends(get_db)):
    cidades = db.query(Cidade).all()
    return cidades


@app.post("/cidades/")
def create_cidade(cidade: CidadeRequest, db=Depends(get_db)):
    nova_cidade = Cidade(nome=cidade.nome, estado_id=cidade.estado_id)
    db.add(nova_cidade)
    db.commit()
    db.refresh(nova_cidade)
    return


@app.get("/cidades/{cidade_id}")
def get_cidade(cidade_id: int, db=Depends(get_db)):
    cidade = db.query(Cidade).filter(Cidade.id == cidade_id).first()
    return cidade


@app.put("/cidades/{cidade_id}")
def update_cidade(cidade_id: int, cidade: CidadeRequest, db=Depends(get_db)):
    cidade = db.query(Cidade).filter(Cidade.id == cidade_id).first()
    cidade.nome = cidade.nome
    db.commit()
    db.refresh(cidade)
    return cidade


@app.delete("/cidades/{cidade_id}")
def delete_cidade(cidade_id: int, db=Depends(get_db)):
    cidade = db.query(Cidade).filter(Cidade.id == cidade_id).first()
    db.delete(cidade)
    db.commit()
    return {"message": "Cidade deletada com sucesso"}

@app.get("/cidades/estado/{estado_id}")
def get_cidades_estado(estado_id: int, db=Depends(get_db)):
    cidades = db.query(Cidade).filter(Cidade.estado_id == estado_id).all()
    return cidades


@app.get("/empresas/")
def get_empresas(db=Depends(get_db)):
    empresas = db.query(Empresa).all()
    return empresas


@app.post("/empresas/")
def create_empresa(empresa: EmpresaRequest, db=Depends(get_db)):
    nova_empresa = Empresa(
        cnpj=empresa.cnpj,
        nome=empresa.nome,
        tipo=empresa.tipo,
        telefone=empresa.telefone,
        email=empresa.email,
    )
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa


@app.get("/convenios/")
def get_convenios(db=Depends(get_db)):
    convenios = db.query(Convenio).all()
    return convenios


@app.post("/convenios/")
def create_convenio(convenio: ConvenioRequest, db=Depends(get_db)):
    novo_convenio = Convenio(
        empresa_id=convenio.empresa_id,
        nome=convenio.nome,
        valor=convenio.valor,
        tipo_servico=convenio.tipo_servico,
        cobertura=convenio.cobertura,
        contato=convenio.contato,
        validade=convenio.validade,
    )
    db.add(novo_convenio)
    db.commit()
    db.refresh(novo_convenio)
    return novo_convenio


@app.get("/areas_atuacao/")
def get_areas_atuacao(db=Depends(get_db)):
    areas_atuacao = db.query(AreaAtuacao).all()
    return areas_atuacao


@app.post("/areas_atuacao/")
def create_area_atuacao(area_atuacao: AreaAtuacaoRequest, db=Depends(get_db)):
    nova_area_atuacao = AreaAtuacao(nome=area_atuacao.nome)
    db.add(nova_area_atuacao)
    db.commit()
    db.refresh(nova_area_atuacao)
    return nova_area_atuacao


@app.get("/unidades/")
def get_unidades(db=Depends(get_db)):
    unidades = db.query(Unidade).all()
    return unidades


@app.post("/unidades/")
def create_unidade(unidade: UnidadeRequest, db=Depends(get_db)):
    nova_unidade = Unidade(
        empresa_id=unidade.empresa_id,
        area_atuacao_id=unidade.area_atuacao_id,
        nome=unidade.nome,
        telefone=unidade.telefone,
        email=unidade.email,
        tipo=unidade.tipo,
        capacidade=unidade.capacidade,
    )
    db.add(nova_unidade)
    db.commit()
    db.refresh(nova_unidade)
    return nova_unidade


@app.get("/enderecos_unidade/")
def get_enderecos_unidade(db=Depends(get_db)):
    enderecos_unidade = db.query(EnderecoUnidade).all()
    return enderecos_unidade


@app.post("/enderecos_unidade/")
def create_endereco_unidade(
    endereco_unidade: EnderecoUnidadeRequest, db=Depends(get_db)
):
    novo_endereco_unidade = EnderecoUnidade(
        unidade_id=endereco_unidade.unidade_id,
        rua=endereco_unidade.rua,
        numero=endereco_unidade.numero,
        cep=endereco_unidade.cep,
        cidade_id=endereco_unidade.cidade_id,
    )
    db.add(novo_endereco_unidade)
    db.commit()
    db.refresh(novo_endereco_unidade)
    return novo_endereco_unidade


@app.get("/medicos/")
def get_medicos(db=Depends(get_db)):
    medicos = db.query(Medico).all()
    return medicos


@app.post("/medicos/")
def create_medico(medico: MedicoRequest, db=Depends(get_db)):
    novo_medico = Medico(
        nome=medico.nome,
        telefone=medico.telefone,
        email=medico.email,
        especialidade=medico.especialidade,
        crm=medico.crm,
    )
    db.add(novo_medico)
    db.commit()
    db.refresh(novo_medico)
    return novo_medico


@app.get("/medicos_unidade/")
def get_medicos_unidade(db=Depends(get_db)):
    medicos_unidade = db.query(MedicoUnidade).all()
    return medicos_unidade


@app.post("/medicos_unidade/")
def create_medico_unidade(medico_unidade: MedicoUnidadeRequest, db=Depends(get_db)):
    novo_medico_unidade = MedicoUnidade(
        medico_id=medico_unidade.medico_id,
        unidade_id=medico_unidade.unidade_id,
        horario_atendimento=medico_unidade.horario_atendimento,
    )
    db.add(novo_medico_unidade)
    db.commit()
    db.refresh(novo_medico_unidade)
    return novo_medico_unidade


@app.get("/estados_civis/")
def get_estados_civis(db=Depends(get_db)):
    estados_civis = db.query(EstadoCivil).all()
    return estados_civis


@app.post("/estados_civis/")
def create_estado_civil(estado_civil: EstadoCivilRequest, db=Depends(get_db)):
    novo_estado_civil = EstadoCivil(nome=estado_civil.nome)
    db.add(novo_estado_civil)
    db.commit()
    db.refresh(novo_estado_civil)
    return novo_estado_civil


@app.get("/clientes/")
def get_clientes(db=Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes


@app.post("/clientes/")
def create_cliente(cliente: ClienteRequest, db=Depends(get_db)):
    novo_cliente = Cliente(
        rg=cliente.rg,
        nome=cliente.nome,
        sexo=cliente.sexo,
        telefone=cliente.telefone,
        email=cliente.email,
        data_nascimento=cliente.data_nascimento,
        cpf=cliente.cpf,
        convenio_id=cliente.convenio_id,
        estado_civil_id=cliente.estado_civil_id,
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente


@app.get("/enderecos_cliente/")
def get_enderecos_cliente(db=Depends(get_db)):
    enderecos_cliente = db.query(EnderecoCliente).all()
    return enderecos_cliente


@app.post("/enderecos_cliente/")
def create_endereco_cliente(
    endereco_cliente: EnderecoClienteRequest, db=Depends(get_db)
):
    novo_endereco_cliente = EnderecoCliente(
        cliente_id=endereco_cliente.cliente_id,
        rua=endereco_cliente.rua,
        numero=endereco_cliente.numero,
        cep=endereco_cliente.cep,
        cidade_id=endereco_cliente.cidade_id,
    )
    db.add(novo_endereco_cliente)
    db.commit()
    db.refresh(novo_endereco_cliente)
    return novo_endereco_cliente


@app.get("/comorbidades/")
def get_comorbidades(db=Depends(get_db)):
    comorbidades = db.query(Comorbidade).all()
    return comorbidades


@app.post("/comorbidades/")
def create_comorbidade(comorbidade: ComorbidadeRequest, db=Depends(get_db)):
    nova_comorbidade = Comorbidade(nome=comorbidade.nome)
    db.add(nova_comorbidade)
    db.commit()
    db.refresh(nova_comorbidade)
    return nova_comorbidade


@app.get("/historicos_saude_cliente/")
def get_historicos_saude_cliente(db=Depends(get_db)):
    historicos_saude_cliente = db.query(HistoricoSaudeCliente).all()
    return historicos_saude_cliente


@app.post("/historicos_saude_cliente/")
def create_historico_saude_cliente(
    historico_saude_cliente: HistoricoSaudeClienteRequest, db=Depends(get_db)
):
    novo_historico_saude_cliente = HistoricoSaudeCliente(
        cliente_id=historico_saude_cliente.cliente_id,
        comorbidade_id=historico_saude_cliente.comorbidade_id,
        data_registro=historico_saude_cliente.data_registro,
        fuma=historico_saude_cliente.fuma,
        observacoes=historico_saude_cliente.observacoes,
    )
    db.add(novo_historico_saude_cliente)
    db.commit()
    db.refresh(novo_historico_saude_cliente)
    return novo_historico_saude_cliente


@app.get("/historicos_hospital_cliente/")
def get_historicos_hospital_cliente(db=Depends(get_db)):
    historicos_hospital_cliente = db.query(HistoricoHospitalCliente).all()
    return historicos_hospital_cliente


@app.post("/historicos_hospital_cliente/")
def create_historico_hospital_cliente(
    historico_hospital_cliente: HistoricoHospitalClienteRequest, db=Depends(get_db)
):
    novo_historico_hospital_cliente = HistoricoHospitalCliente(
        cliente_id=historico_hospital_cliente.cliente_id,
        data_registro=historico_hospital_cliente.data_registro,
        historico_medico=historico_hospital_cliente.historico_medico,
        exames_realizados=historico_hospital_cliente.exames_realizados,
        medicamentos_prescritos=historico_hospital_cliente.medicamentos_prescritos,
        observacoes=historico_hospital_cliente.observacoes,
    )
    db.add(novo_historico_hospital_cliente)
    db.commit()
    db.refresh(novo_historico_hospital_cliente)
    return novo_historico_hospital_cliente


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
