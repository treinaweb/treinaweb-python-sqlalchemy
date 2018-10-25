from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from fabricas import fabrica_conexao

fabrica = fabrica_conexao.FabricaConexao()

engine = fabrica.conectar()

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    idade = Column(Integer, nullable=False)

    def __repr__(self):
        return "Cliente %s ('%s', '%s')" % (self.id, self.nome, self.idade)

Base.metadata.create_all(engine)