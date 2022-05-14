#impot packages
import insert_banco as db
import sys
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP/DAO')

import dao_space


class Space:
    def init(self):
        self.id = ""
        self.name = ""

    #Receive Json and loop through the Json picking up the necessary data
    def read_space(self,json_string):
        lista_space = []
        for s in json_string['spaces']:
            self.id = s['id']
            self.name = s['name']
            
            #instantiating the object
            space = dao_space.Space()
            space.ID = self.id
            space.NOME = self.name
            #call function to persists DBMS
            dao_space.insert_update(space)
            
            #Save values into list to use in the next URL
            lista_space.append([self.id,self.name])
        return lista_space