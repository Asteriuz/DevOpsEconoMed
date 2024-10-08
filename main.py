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


# Rotas
@app.get("/")
def read_root():
    return {"message": "Bem-vindo a API da EconoMed"}


@app.get("/estados/")
def get_estados(db=Depends(get_db)):
    estados = db.query(Estado).all()
    return estados


@app.get("/estados/{estado_id}")
def get_estado(estado_id: int, db=Depends(get_db)):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    return estado


@app.post("/estados/")
def create_estado(estado: EstadoRequest, db=Depends(get_db)):
    novo_estado = Estado(nome=estado.nome)
    db.add(novo_estado)
    db.commit()
    db.refresh(novo_estado)
    return novo_estado


@app.put("/estados/{estado_id}")
def update_estado(estado_id: int, estado_request: EstadoRequest, db=Depends(get_db)):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    estado.nome = estado_request.nome
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


@app.get("/cidades/{cidade_id}")
def get_cidade(cidade_id: int, db=Depends(get_db)):
    cidade = db.query(Cidade).filter(Cidade.id == cidade_id).first()
    return cidade


@app.post("/cidades/")
def create_cidade(cidade: CidadeRequest, db=Depends(get_db)):
    nova_cidade = Cidade(nome=cidade.nome, estado_id=cidade.estado_id)
    db.add(nova_cidade)
    db.commit()
    db.refresh(nova_cidade)
    return


@app.put("/cidades/{cidade_id}")
def update_cidade(cidade_id: int, cidade_request: CidadeRequest, db=Depends(get_db)):
    cidade = db.query(Cidade).filter(Cidade.id == cidade_id).first()
    cidade.nome = cidade_request.nome
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


@app.get("/empresas/{empresa_id}")
def get_empresa(empresa_id: int, db=Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    return empresa


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


@app.put("/empresas/{empresa_id}")
def update_empresa(empresa_id: int, empresa_request: EmpresaRequest, db=Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    empresa.cnpj = empresa_request.cnpj
    empresa.nome = empresa_request.nome
    empresa.tipo = empresa_request.tipo
    empresa.telefone = empresa_request.telefone
    empresa.email = empresa_request.email
    db.commit()
    db.refresh(empresa)
    return empresa


@app.delete("/empresas/{empresa_id}")
def delete_empresa(empresa_id: int, db=Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    db.delete(empresa)
    db.commit()
    return {"message": "Empresa deletada com sucesso"}


@app.get("/convenios/")
def get_convenios(db=Depends(get_db)):
    convenios = db.query(Convenio).all()
    return convenios


@app.get("/convenios/{convenio_id}")
def get_convenio(convenio_id: int, db=Depends(get_db)):
    convenio = db.query(Convenio).filter(Convenio.id == convenio_id).first()
    return convenio


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


@app.put("/convenios/{convenio_id}")
def update_convenio(convenio_id: int, convenio_request: ConvenioRequest, db=Depends(get_db)):
    convenio = db.query(Convenio).filter(Convenio.id == convenio_id).first()
    convenio.empresa_id = convenio_request.empresa_id
    convenio.nome = convenio_request.nome
    convenio.valor = convenio_request.valor
    convenio.tipo_servico = convenio_request.tipo_servico
    convenio.cobertura = convenio_request.cobertura
    convenio.contato = convenio_request.contato
    convenio.validade = convenio_request.validade
    db.commit()
    db.refresh(convenio)
    return convenio


@app.delete("/convenios/{convenio_id}")
def delete_convenio(convenio_id: int, db=Depends(get_db)):
    convenio = db.query(Convenio).filter(Convenio.id == convenio_id).first()
    db.delete(convenio)
    db.commit()
    return {"message": "Convenio deletado com sucesso"}


@app.get("/areas_atuacao/")
def get_areas_atuacao(db=Depends(get_db)):
    areas_atuacao = db.query(AreaAtuacao).all()
    return areas_atuacao


@app.get("/areas_atuacao/{area_atuacao_id}")
def get_area_atuacao(area_atuacao_id: int, db=Depends(get_db)):
    area_atuacao = (
        db.query(AreaAtuacao).filter(AreaAtuacao.id == area_atuacao_id).first()
    )
    return area_atuacao


@app.post("/areas_atuacao/")
def create_area_atuacao(area_atuacao: AreaAtuacaoRequest, db=Depends(get_db)):
    nova_area_atuacao = AreaAtuacao(nome=area_atuacao.nome)
    db.add(nova_area_atuacao)
    db.commit()
    db.refresh(nova_area_atuacao)
    return nova_area_atuacao


@app.put("/areas_atuacao/{area_atuacao_id}")
def update_area_atuacao(
    area_atuacao_id: int, area_atuacao_request: AreaAtuacaoRequest, db=Depends(get_db)
):
    area_atuacao = (
        db.query(AreaAtuacao).filter(AreaAtuacao.id == area_atuacao_id).first()
    )
    area_atuacao.nome = area_atuacao_request.nome
    db.commit()
    db.refresh(area_atuacao)
    return area_atuacao


@app.delete("/areas_atuacao/{area_atuacao_id}")
def delete_area_atuacao(area_atuacao_id: int, db=Depends(get_db)):
    area_atuacao = (
        db.query(AreaAtuacao).filter(AreaAtuacao.id == area_atuacao_id).first()
    )
    db.delete(area_atuacao)
    db.commit()
    return {"message": "Area de atuacao deletada com sucesso"}


@app.get("/unidades/")
def get_unidades(db=Depends(get_db)):
    unidades = db.query(Unidade).all()
    return unidades


@app.get("/unidades/{unidade_id}")
def get_unidade(unidade_id: int, db=Depends(get_db)):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()
    return unidade


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


@app.put("/unidades/{unidade_id}")
def update_unidade(unidade_id: int, unidade_request: UnidadeRequest, db=Depends(get_db)):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()
    unidade.empresa_id = unidade_request.empresa_id
    unidade.area_atuacao_id = unidade_request.area_atuacao_id
    unidade.nome = unidade_request.nome
    unidade.telefone = unidade_request.telefone
    unidade.email = unidade_request.email
    unidade.tipo = unidade_request.tipo
    unidade.capacidade = unidade_request.capacidade
    db.commit()
    db.refresh(unidade)
    return unidade


@app.delete("/unidades/{unidade_id}")
def delete_unidade(unidade_id: int, db=Depends(get_db)):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()
    db.delete(unidade)
    db.commit()
    return {"message": "Unidade deletada com sucesso"}


@app.get("/enderecos_unidade/")
def get_enderecos_unidade(db=Depends(get_db)):
    enderecos_unidade = db.query(EnderecoUnidade).all()
    return enderecos_unidade


@app.get("/enderecos_unidade/{endereco_unidade_id}")
def get_endereco_unidade(endereco_unidade_id: int, db=Depends(get_db)):
    endereco_unidade = (
        db.query(EnderecoUnidade)
        .filter(EnderecoUnidade.id == endereco_unidade_id)
        .first()
    )
    return endereco_unidade


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


@app.put("/enderecos_unidade/{endereco_unidade_id}")
def update_endereco_unidade(
    endereco_unidade_id: int,
    endereco_unidade_request: EnderecoUnidadeRequest,
    db=Depends(get_db),
):
    endereco_unidade = (
        db.query(EnderecoUnidade)
        .filter(EnderecoUnidade.id == endereco_unidade_id)
        .first()
    )
    endereco_unidade.unidade_id = endereco_unidade_request.unidade_id
    endereco_unidade.rua = endereco_unidade_request.rua
    endereco_unidade.numero = endereco_unidade_request.numero
    endereco_unidade.cep = endereco_unidade_request.cep
    endereco_unidade.cidade_id = endereco_unidade_request.cidade_id
    db.commit()
    db.refresh(endereco_unidade)
    return endereco_unidade


@app.delete("/enderecos_unidade/{endereco_unidade_id}")
def delete_endereco_unidade(endereco_unidade_id: int, db=Depends(get_db)):
    endereco_unidade = (
        db.query(EnderecoUnidade)
        .filter(EnderecoUnidade.id == endereco_unidade_id)
        .first()
    )
    db.delete(endereco_unidade)
    db.commit()
    return {"message": "Endereco da unidade deletado com sucesso"}


@app.get("/medicos/")
def get_medicos(db=Depends(get_db)):
    medicos = db.query(Medico).all()
    return medicos


@app.get("/medicos/{medico_id}")
def get_medico(medico_id: int, db=Depends(get_db)):
    medico = db.query(Medico).filter(Medico.id == medico_id).first()
    return medico


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


@app.put("/medicos/{medico_id}")
def update_medico(medico_id: int, medico_request: MedicoRequest, db=Depends(get_db)):
    medico = db.query(Medico).filter(Medico.id == medico_id).first()
    medico.nome = medico_request.nome
    medico.telefone = medico_request.telefone
    medico.email = medico_request.email
    medico.especialidade = medico_request.especialidade
    medico.crm = medico_request.crm
    db.commit()
    db.refresh(medico)
    return medico


@app.delete("/medicos/{medico_id}")
def delete_medico(medico_id: int, db=Depends(get_db)):
    medico = db.query(Medico).filter(Medico.id == medico_id).first()
    db.delete(medico)
    db.commit()
    return {"message": "Medico deletado com sucesso"}


@app.get("/medicos_unidade/")
def get_medicos_unidade(db=Depends(get_db)):
    medicos_unidade = db.query(MedicoUnidade).all()
    return medicos_unidade


@app.get("/medicos_unidade/{medico_unidade_id}")
def get_medico_unidade(medico_unidade_id: int, db=Depends(get_db)):
    medico_unidade = (
        db.query(MedicoUnidade).filter(MedicoUnidade.id == medico_unidade_id).first()
    )
    return medico_unidade


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


@app.put("/medicos_unidade/{medico_unidade_id}")
def update_medico_unidade(
    medico_unidade_id: int, medico_unidade_request: MedicoUnidadeRequest, db=Depends(get_db)
):
    medico_unidade = (
        db.query(MedicoUnidade).filter(MedicoUnidade.id == medico_unidade_id).first()
    )
    medico_unidade.medico_id = medico_unidade_request.medico_id
    medico_unidade.unidade_id = medico_unidade_request.unidade_id
    medico_unidade.horario_atendimento = medico_unidade_request.horario_atendimento
    db.commit()
    db.refresh(medico_unidade)
    return medico_unidade


@app.delete("/medicos_unidade/{medico_unidade_id}")
def delete_medico_unidade(medico_unidade_id: int, db=Depends(get_db)):
    medico_unidade = (
        db.query(MedicoUnidade).filter(MedicoUnidade.id == medico_unidade_id).first()
    )
    db.delete(medico_unidade)
    db.commit()
    return {"message": "Medico da unidade deletado com sucesso"}


@app.get("/estados_civis/")
def get_estados_civis(db=Depends(get_db)):
    estados_civis = db.query(EstadoCivil).all()
    return estados_civis


@app.get("/estados_civis/{estado_civil_id}")
def get_estado_civil(estado_civil_id: int, db=Depends(get_db)):
    estado_civil = (
        db.query(EstadoCivil).filter(EstadoCivil.id == estado_civil_id).first()
    )
    return estado_civil


@app.post("/estados_civis/")
def create_estado_civil(estado_civil: EstadoCivilRequest, db=Depends(get_db)):
    novo_estado_civil = EstadoCivil(nome=estado_civil.nome)
    db.add(novo_estado_civil)
    db.commit()
    db.refresh(novo_estado_civil)
    return novo_estado_civil


@app.put("/estados_civis/{estado_civil_id}")
def update_estado_civil(
    estado_civil_id: int, estado_civil_request: EstadoCivilRequest, db=Depends(get_db)
):
    estado_civil = (
        db.query(EstadoCivil).filter(EstadoCivil.id == estado_civil_id).first()
    )
    estado_civil.nome = estado_civil_request.nome
    db.commit()
    db.refresh(estado_civil)
    return estado_civil


@app.delete("/estados_civis/{estado_civil_id}")
def delete_estado_civil(estado_civil_id: int, db=Depends(get_db)):
    estado_civil = (
        db.query(EstadoCivil).filter(EstadoCivil.id == estado_civil_id).first()
    )
    db.delete(estado_civil)
    db.commit()
    return {"message": "Estado civil deletado com sucesso"}


@app.get("/clientes/")
def get_clientes(db=Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes


@app.get("/clientes/{cliente_id}")
def get_cliente(cliente_id: int, db=Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    return cliente


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


@app.put("/clientes/{cliente_id}")
def update_cliente(cliente_id: int, cliente_request: ClienteRequest, db=Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    cliente.rg = cliente_request.rg
    cliente.nome = cliente_request.nome
    cliente.sexo = cliente_request.sexo
    cliente.telefone = cliente_request.telefone
    cliente.email = cliente_request.email
    cliente.data_nascimento = cliente_request.data_nascimento
    cliente.cpf = cliente_request.cpf
    cliente.convenio_id = cliente_request.convenio_id
    cliente.estado_civil_id = cliente_request.estado_civil_id
    db.commit()
    db.refresh(cliente)
    return cliente


@app.delete("/clientes/{cliente_id}")
def delete_cliente(cliente_id: int, db=Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    db.delete(cliente)
    db.commit()
    return {"message": "Cliente deletado com sucesso"}


@app.get("/enderecos_cliente/")
def get_enderecos_cliente(db=Depends(get_db)):
    enderecos_cliente = db.query(EnderecoCliente).all()
    return enderecos_cliente


@app.get("/enderecos_cliente/{endereco_cliente_id}")
def get_endereco_cliente(endereco_cliente_id: int, db=Depends(get_db)):
    endereco_cliente = (
        db.query(EnderecoCliente)
        .filter(EnderecoCliente.id == endereco_cliente_id)
        .first()
    )
    return endereco_cliente


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


@app.put("/enderecos_cliente/{endereco_cliente_id}")
def update_endereco_cliente(
    endereco_cliente_id: int,
    endereco_cliente_request: EnderecoClienteRequest,
    db=Depends(get_db),
):
    endereco_cliente = (
        db.query(EnderecoCliente)
        .filter(EnderecoCliente.id == endereco_cliente_id)
        .first()
    )
    endereco_cliente.cliente_id = endereco_cliente_request.cliente_id
    endereco_cliente.rua = endereco_cliente_request.rua
    endereco_cliente.numero = endereco_cliente_request.numero
    endereco_cliente.cep = endereco_cliente_request.cep
    endereco_cliente.cidade_id = endereco_cliente_request.cidade_id
    db.commit()
    db.refresh(endereco_cliente)
    return endereco_cliente


@app.delete("/enderecos_cliente/{endereco_cliente_id}")
def delete_endereco_cliente(endereco_cliente_id: int, db=Depends(get_db)):
    endereco_cliente = (
        db.query(EnderecoCliente)
        .filter(EnderecoCliente.id == endereco_cliente_id)
        .first()
    )
    db.delete(endereco_cliente)
    db.commit()
    return {"message": "Endereco do cliente deletado com sucesso"}


@app.get("/comorbidades/")
def get_comorbidades(db=Depends(get_db)):
    comorbidades = db.query(Comorbidade).all()
    return comorbidades


@app.get("/comorbidades/{comorbidade_id}")
def get_comorbidade(comorbidade_id: int, db=Depends(get_db)):
    comorbidade = db.query(Comorbidade).filter(Comorbidade.id == comorbidade_id).first()
    return comorbidade


@app.post("/comorbidades/")
def create_comorbidade(comorbidade: ComorbidadeRequest, db=Depends(get_db)):
    nova_comorbidade = Comorbidade(nome=comorbidade.nome)
    db.add(nova_comorbidade)
    db.commit()
    db.refresh(nova_comorbidade)
    return nova_comorbidade


@app.put("/comorbidades/{comorbidade_id}")
def update_comorbidade(
    comorbidade_id: int, comorbidade_request: ComorbidadeRequest, db=Depends(get_db)
):
    comorbidade = db.query(Comorbidade).filter(Comorbidade.id == comorbidade_id).first()
    comorbidade.nome = comorbidade_request.nome
    db.commit()
    db.refresh(comorbidade)
    return comorbidade


@app.delete("/comorbidades/{comorbidade_id}")
def delete_comorbidade(comorbidade_id: int, db=Depends(get_db)):
    comorbidade = db.query(Comorbidade).filter(Comorbidade.id == comorbidade_id).first()
    db.delete(comorbidade)
    db.commit()
    return {"message": "Comorbidade deletada com sucesso"}


@app.get("/historicos_saude_cliente/")
def get_historicos_saude_cliente(db=Depends(get_db)):
    historicos_saude_cliente = db.query(HistoricoSaudeCliente).all()
    return historicos_saude_cliente


@app.get("/historicos_saude_cliente/{historico_saude_cliente_id}")
def get_historico_saude_cliente(historico_saude_cliente_id: int, db=Depends(get_db)):
    historico_saude_cliente = (
        db.query(HistoricoSaudeCliente)
        .filter(HistoricoSaudeCliente.id == historico_saude_cliente_id)
        .first()
    )
    return historico_saude_cliente


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


@app.put("/historicos_saude_cliente/{historico_saude_cliente_id}")
def update_historico_saude_cliente(
    historico_saude_cliente_id: int,
    historico_saude_cliente_request: HistoricoSaudeClienteRequest,
    db=Depends(get_db),
):
    historico_saude_cliente = (
        db.query(HistoricoSaudeCliente)
        .filter(HistoricoSaudeCliente.id == historico_saude_cliente_id)
        .first()
    )
    historico_saude_cliente.cliente_id = historico_saude_cliente_request.cliente_id
    historico_saude_cliente.comorbidade_id = historico_saude_cliente_request.comorbidade_id
    historico_saude_cliente.data_registro = historico_saude_cliente_request.data_registro
    historico_saude_cliente.fuma = historico_saude_cliente_request.fuma
    historico_saude_cliente.observacoes = historico_saude_cliente_request.observacoes
    db.commit()
    db.refresh(historico_saude_cliente)
    return historico_saude_cliente


@app.delete("/historicos_saude_cliente/{historico_saude_cliente_id}")
def delete_historico_saude_cliente(historico_saude_cliente_id: int, db=Depends(get_db)):
    historico_saude_cliente = (
        db.query(HistoricoSaudeCliente)
        .filter(HistoricoSaudeCliente.id == historico_saude_cliente_id)
        .first()
    )
    db.delete(historico_saude_cliente)
    db.commit()
    return {"message": "Histórico de saúde do cliente deletado com sucesso"}


@app.get("/historicos_hospital_cliente/")
def get_historicos_hospital_cliente(db=Depends(get_db)):
    historicos_hospital_cliente = db.query(HistoricoHospitalCliente).all()
    return historicos_hospital_cliente


@app.get("/historicos_hospital_cliente/{historico_hospital_cliente_id}")
def get_historico_hospital_cliente(
    historico_hospital_cliente_id: int, db=Depends(get_db)
):
    historico_hospital_cliente = (
        db.query(HistoricoHospitalCliente)
        .filter(HistoricoHospitalCliente.id == historico_hospital_cliente_id)
        .first()
    )
    return historico_hospital_cliente


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


@app.put("/historicos_hospital_cliente/{historico_hospital_cliente_id}")
def update_historico_hospital_cliente(
    historico_hospital_cliente_id: int,
    historico_hospital_cliente_request: HistoricoHospitalClienteRequest,
    db=Depends(get_db),
):
    historico_hospital_cliente = (
        db.query(HistoricoHospitalCliente)
        .filter(HistoricoHospitalCliente.id == historico_hospital_cliente_id)
        .first()
    )
    historico_hospital_cliente.cliente_id = historico_hospital_cliente_request.cliente_id
    historico_hospital_cliente.data_registro = historico_hospital_cliente_request.data_registro
    historico_hospital_cliente.historico_medico = (
        historico_hospital_cliente_request.historico_medico
    )
    historico_hospital_cliente.exames_realizados = (
        historico_hospital_cliente_request.exames_realizados
    )
    historico_hospital_cliente.medicamentos_prescritos = (
        historico_hospital_cliente_request.medicamentos_prescritos
    )
    historico_hospital_cliente.observacoes = historico_hospital_cliente_request.observacoes
    db.commit()
    db.refresh(historico_hospital_cliente)
    return historico_hospital_cliente


@app.delete("/historicos_hospital_cliente/{historico_hospital_cliente_id}")
def delete_historico_hospital_cliente(
    historico_hospital_cliente_id: int, db=Depends(get_db)
):
    historico_hospital_cliente = (
        db.query(HistoricoHospitalCliente)
        .filter(HistoricoHospitalCliente.id == historico_hospital_cliente_id)
        .first()
    )
    db.delete(historico_hospital_cliente)
    db.commit()
    return {"message": "Histórico hospitalar do cliente deletado com sucesso"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
