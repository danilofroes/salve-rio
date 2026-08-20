from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# postgresql://usuario:senha@host:porta/banco
SQLALCHEMY_DATABASE_URL = "postgresql://salve:salve_dev_password@localhost:5432/salve"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    '''
    Função para pegar a sessão do banco e fechar depois do uso
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()