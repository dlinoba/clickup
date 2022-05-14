#impot packages
import sys
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP/DAO')

import dao_folder
import insert_banco as db

class Folder:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.space_id = ""

    #Receive Json and loop through the Json picking up the necessary data
    def read_folder(self, json_string):
        lista_folder = []
        for l in json_string['folders']:
            self.id = l['id']
            self.name = l['name']
            self.space_id = l['space']['id']
            
            #instantiating the object
            folder = dao_folder.Folder()
            folder.ID = self.id
            folder.ID_SPACE = self.space_id
            folder.NOME = self.name
            #call function to persists DBMS
            dao_folder.insert_update(folder)

            #Save values into list to use in the next URL
            lista_folder.append([self.id,self.name,self.space_id])
        return lista_folder