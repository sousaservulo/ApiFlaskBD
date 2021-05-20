from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///clientes.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#cria a tabela CLientes
class Clientes(Base):
    __tablename__='clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    contato = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

