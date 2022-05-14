#impot packages
import sys
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP/')

import config

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, update, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

engine = config.conexao

Base = declarative_base()

class Task(Base):

    __tablename__ = 'TASK'
    
    ID = Column(String(255), primary_key=True)
    ID_PARENT = Column(String(255))
    ID_LIST = Column(Integer)
    ID_FOLDER = Column(Integer)
    ID_SPACE = Column(Integer)
    TITULO = Column(Text)
    SUBTITULO = Column(Text)
    DESCRICAO = Column(Text)
    TASK_STATUS = Column(String(30))
    DATA_CRIACAO = Column(DateTime)
    DATA_ATUALIZACAO = Column(DateTime)
    DATA_FECHAMENTO = Column(DateTime)
    ARQUIVADO = Column(String(10))
    CRIADO_POR = Column(String(100))
    DATA_VALIDADE = Column(DateTime)
    DATA_INICIO = Column(DateTime)
    TEMPO_ESTIMADO = Column(Numeric(29,2))
    TEMPO_GASTO = Column(Numeric(29,2))
    PRIORIDADE = Column(String(30))


def insert_update(task):
    Session = sessionmaker(bind=engine)
    session = Session()
    exists_id = session.query(Task.ID).filter(Task.ID == task.ID).first() is not None
    if exists_id is False:
        session.add(task)
        session.commit()    
    else:
        updated = session.query(Task.ID).filter(Task.ID == task.ID, Task.ID_LIST != task.ID_LIST, Task.ID_SPACE != task.ID_SPACE,\
                                                Task.TASK_STATUS != task.TASK_STATUS, Task.DATA_ATUALIZACAO != task.DATA_ATUALIZACAO,\
                                                Task.DATA_FECHAMENTO != task.DATA_FECHAMENTO, Task.ARQUIVADO != task.ARQUIVADO,\
                                                ).first() is not None
        #session.commit()
        if updated is True:
            upd =   update(Task).\
                    where(Task.ID == task.ID, Task.ID_LIST == task.ID_LIST, Task.ID_SPACE == task.ID_SPACE).\
                    values(ID_PARENT=task.ID_PARENT, ID_LIST=task.ID_LIST, ID_SPACE=task.ID_SPACE, TITULO=task.TITULO,\
                           SUBTITULO=task.SUBTITULO, DESCRICAO=task.DESCRICAO, TASK_STATUS=task.TASK_STATUS, DATA_ATUALIZACAO=task.DATA_ATUALIZACAO,\
                           DATA_FECHAMENTO=task.DATA_FECHAMENTO, ARQUIVADO=task.ARQUIVADO, DATA_VALIDADE=task.DATA_VALIDADE, DATA_INICIO=task.DATA_INICIO,\
                           TEMPO_ESTIMADO=task.TEMPO_ESTIMADO, TEMPO_GASTO=task.TEMPO_GASTO, PRIORIDADE=task.PRIORIDADE)
            session.execute(upd)
            session.commit()
    session.commit()
        
    