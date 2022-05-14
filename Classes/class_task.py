#impot packages
import sys
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP')
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP/DAO')
import config as cf
import requests
import insert_banco as db
from datetime import datetime
import dao_task
import time

#defining default values
class Task:
    def __init__(self):
        self.prioridade = None
        self.tempo_gasto = 0
        self.id = ''
        self.titulo = ''
        self.subtitulo = ''
        self.descricao = ''
        self.task_status = ''
        self.data_criacao = ''
        self.data_atualizacao = ''
        self.data_fechamento = ''
        self.arquivado = ''
        self.criado_por = ''
        self.data_validade = ''
        self.data_inicio = ''
        self.tempo_estimado = ''
        self.id_list = ''
        self.id_folder = ''
        self.id_space = ''
        self.parent = ''

    #Receive Json and loop through the Json picking up the necessary data
    def read_task(self, json_string):
        lista_task = []
        for t in json_string['tasks']:
            prioridade = t['priority']
            if prioridade != None:
                for key, value in prioridade.items():
                    if key == 'priority':
                        self.prioridade = value
            
            if 'time_spent' in t:
                self.tempo_gasto = t['time_spent']
            
            self.id = t['id']
            self.parent = t['parent']
            self.titulo = t['name']
            self.subtitulo = t['text_content']
            self.descricao = t['description']
            self.task_status = t['status']['status']
            self.data_criacao = datetime.fromtimestamp(int(t['date_created'])/1000) if t['date_created'] is not None else None
            self.data_atualizacao = datetime.fromtimestamp(int(t['date_updated'])/1000) if t['date_updated'] is not None else None
            self.data_fechamento = datetime.fromtimestamp(int(t['date_closed'])/1000) if t['date_closed'] is not None else None
            self.arquivado = t['archived']
            self.criado_por = t['creator']['username']
            self.data_validade = datetime.fromtimestamp(int(t['due_date'])/1000) if t['due_date'] is not None else None
            self.data_inicio = datetime.fromtimestamp(int(t['start_date'])/1000) if t['start_date'] is not None else None
            self.tempo_estimado = t['time_estimate']
            self.id_list = t['list']['id']
            self.id_folder = t['folder']['id']
            self.id_space = t['space']['id']

            #instantiating the object
            task = dao_task.Task()
            task.ID = self.id
            task.ID_PARENT = self.parent
            task.TITULO = self.titulo
            task.SUBTITULO = self.subtitulo
            task.DESCRICAO = self.descricao
            task.TASK_STATUS = self.task_status
            task.DATA_CRIACAO = self.data_criacao
            task.DATA_ATUALIZACAO = self.data_atualizacao
            task.DATA_FECHAMENTO = self.data_fechamento
            task.ARQUIVADO = self.arquivado
            task.CRIADO_POR = self.criado_por
            task.DATA_VALIDADE = self.data_validade
            task.DATA_INICIO = self.data_inicio
            task.TEMPO_ESTIMADO = self.tempo_estimado
            task.ID_LIST = self.id_list
            task.ID_FOLDER = self.id_folder
            task.ID_SPACE = self.id_space
            
            #call function to persists DBMS
            dao_task.insert_update(task)
                                    
            
    #It receives an ID and the option if it is archived or not, checks the pagination, assembles the URL and generates a Json
    def get_task(self,id_list,arquivado):
        obj_task = Task()
        #The initial page always will be 0
        pagina = 0

        if arquivado == 0:
            url_final = '&include_closed=true&subtasks=true'
        else:
            url_final = '&include_closed=true&subtasks=true&archived=true'
        
        #Build URL
        url_list = cf.root_url+'list/'+id_list+'/task?page='+str(pagina)+url_final

        response = requests.get(url_list, headers=cf.headers)

        if (response.status_code == 200):
            retorno_list = response.json()
            
            #Receive Json length
            tamanho = len(retorno_list['tasks'])
            #Print the page and Json length, for display only
            print('página ',str(pagina),' tamanho ',tamanho)

            #calls a function that receives the Json, captures the data and persists in the database
            obj_task.read_task(retorno_list)

            #IF the length of Json is 100, we need to go to the next page and check if there are data in there
            if tamanho == 100:
                #While the return is 100, will be in the loop incrementing the page
                while tamanho == 100:
                    pagina += 1
                    url_list = cf.root_url+'/list/'+id_list+'/task?page='+str(pagina)+url_final
                    response = requests.get(url_list, headers=cf.headers)

                    if (response.status_code == 200):
                        retorno_list = response.json()
                        #Update variable with Json length
                        tamanho = len(retorno_list['tasks'])
                        #Print the page and Json length, for display only
                        print('página ',str(pagina),' tamanho ',tamanho)
                        #calls a function that receives the Json, captures the data and persists in the database
                        obj_task.read_task(retorno_list)
                        time.sleep(1)
                    else:
                        print('without connection')
        else:
            print('without connection')