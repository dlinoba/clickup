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

class Folder(Base):

    __tablename__ = 'FOLDER'

    ID = Column(Integer, primary_key=True)
    ID_SPACE = Column(Integer)
    NOME = Column(String(255))

def insert_update(folder):
    Session = sessionmaker(bind=engine)
    session = Session()
    exists_id = session.query(Folder.ID).filter(Folder.ID == folder.ID, Folder.ID_SPACE == folder.ID_SPACE).first() is not None
    if exists_id is False:
        session.add(folder)
        session.commit()    
    else:
        updated = session.query(Folder.ID).filter(Folder.ID == folder.ID, Folder.ID_SPACE == folder.ID_SPACE, Folder.NOME != folder.NOME).first() is not None
        if updated is True:
            upd =   update(Folder).\
                    where(Folder.ID == folder.ID, Folder.ID_SPACE == folder.ID_SPACE).\
                    values(NOME = folder.NOME)
            session.execute(upd)
            session.commit()
    session.commit()