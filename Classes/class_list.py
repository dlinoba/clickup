#impot packages
import sys
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP/DAO')

import dao_list
import insert_banco as db

class List:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.folder_id = ""

    #Receive Json and loop through the Json picking up the necessary data
    def read_list(self, json_string):
        lista_list = []
        for l in json_string['lists']:
            self.id = l['id']
            self.name = l['name']
            self.folder_id = l['folder']['id']

            #instantiating the object
            lista = dao_list.Lista()
            lista.ID = self.id
            lista.ID_FOLDER = self.folder_id
            lista.NOME = self.name
            #call function to persists DBMS
            dao_list.insert_update(lista)

            #Save values into list to use in the next URL
            lista_list.append([self.id,self.name,self.folder_id])
        return lista_list