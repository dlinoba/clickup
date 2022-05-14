#impot packages
import sys
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP/')

import config

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, update, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

engine = config.conexao

Base = declarative_base()

class Lista(Base):

    __tablename__ = 'LIST'

    ID = Column(Integer, primary_key=True)
    ID_FOLDER = Column(Integer)
    NOME = Column(String(255))

def insert_update(lista):
    Session = sessionmaker(bind=engine)
    session = Session()
    exists_id = session.query(Lista.ID).filter(Lista.ID == lista.ID, Lista.ID_FOLDER == lista.ID_FOLDER).first() is not None
    if exists_id is False:
        session.add(lista)
        session.commit()    
    else:
        updated = session.query(Lista.ID).filter(Lista.ID == lista.ID, Lista.ID_FOLDER == lista.ID_FOLDER, Lista.NOME != lista.NOME).first() is not None
        if updated is True:
            upd =   update(Lista).\
                    where(Lista.ID == lista.ID, Lista.ID_FOLDER == lista.ID_FOLDER).\
                    values(NOME = lista.NOME)
            session.execute(upd)
            session.commit()
    session.commit()