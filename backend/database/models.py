from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.base import Base

class DadosClinica(Base):
    __tablename__ = "clinicas_familia"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    bairro = Column(String, nullable=False)
    area_programatica = Column(String, index=True)

    dados_climaticos = relationship("DadoClimatico", back_populates="clinica")
    registros_epidemiologicos = relationship("RegistroEpidemiologico", back_populates="clinica")

class DadosClimaticos(Base):
    __tablename__ = "dados_climaticos"

    id = Column(Integer, primary_key=True, index=True)
    data_registro = Column(Date, index=True, nullable=False)
    
    # Variáveis meteorológicas do INMET
    temperatura_media = Column(Float)
    temperatura_maxima = Column(Float)
    temperatura_minima = Column(Float)
    precipitacao = Column(Float) # Medido em mm
    estacao_inmet = Column(String) # Nome ou código da estação meteorológica
    
    # Aponta para o ID da tabela clinicas_familia
    clinica_id = Column(Integer, ForeignKey("clinicas_familia.id"))
    clinica = relationship("Clinica", back_populates="dados_climaticos")

class RegistroEpidemiologico(Base):
    __tablename__ = "registros_epidemiologicos"

    id = Column(Integer, primary_key=True, index=True)
    
    # Doença monitorada
    doenca = Column(String, index=True, nullable=False) 
    
    # Agrupamento temporal padrão do Ministério da Saúde
    semana_epidemiologica = Column(Integer, index=True, nullable=False) 
    ano = Column(Integer, index=True, nullable=False)
    
    # Quantidade de casos detectados pela vigilância epidemiológica
    casos_notificados = Column(Integer, default=0)
    
    # Aponta de qual Clínica/Região são esses casos
    clinica_id = Column(Integer, ForeignKey("clinicas_familia.id"))
    clinica = relationship("Clinica", back_populates="registros_epidemiologicos")