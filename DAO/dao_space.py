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

class Space(Base):

    __tablename__ = 'SPACE'

    ID = Column(Integer, primary_key=True)
    NOME = Column(String(200))

def insert_update(space):
    Session = sessionmaker(bind=engine)
    session = Session()
    exists_id = session.query(Space.ID).filter(Space.ID == space.ID).first() is not None
    if exists_id is False:
        session.add(space)
        session.commit()    
    else:
        updated = session.query(Space.ID).filter(Space.ID == space.ID, Space.NOME != space.NOME).first() is not None
        if updated is True:
            upd =   update(Space).\
                    where(Space.ID == space.ID).\
                    values(NOME=space.NOME)
            session.execute(upd)
            session.commit()
    session.commit()