#impot packages
import sys
sys.path.insert(0, 'C:/PDI_PROEJTOS/API_CLICKUP/Classes')
import config as cf
from class_chamado import Task
from class_responsavel import Responsavel
from class_space import Space
from class_list import List
from class_folder import Folder
from class_task import Task
from sqlalchemy import create_engine
import requests

#create support list
lista_folder = []
flat_lista_folder = []
lista_sem_folder = []
flat_lista_sem_folder = []
lista_listas = []
flat_lista_listas = []
lista_tasks = []
flat_lista_tasks = []

#Build principal URL to begin the API call
url = cf.root_url+'team/'+cf.Space+'/space'
 
response = requests.get(url, headers=cf.headers)
 
if (response.status_code == 200):
    
    retorno_space = response.json()
    obj_space = Space()
    #Call function that persists in DBMS and return the ID_Space list
    spaces = obj_space.read_space(retorno_space)
else:
    print('without connection')

'''
For each space ID saved in last step, will be call the next URL with ID parameter and will catch the list_id that don't have folders
'''
for ls in spaces:

    url_list_without_folder = cf.root_url+'/space/'+ls[0]+'/list'

    response = requests.get(url_list_without_folder, headers=cf.headers)

    if (response.status_code == 200):
        retorno_list_without_folder = response.json()
        obj_list = List()
        #Call function that persists in DBMS and return the ID_list
        lista_sem_folder.append(obj_list.read_list(retorno_list_without_folder))
    else:
        print('without connection')

#Normalize tha list, because the return came list inside list
for sublist in lista_sem_folder:
    for item in sublist:
        flat_lista_sem_folder.append(item)

'''
For each ID saved in space list, will be call the next URL with ID parameter and will catch the id folder
'''
for fs in spaces:

    url_folder = cf.root_url+'/space/'+fs[0]+'/folder'

    response = requests.get(url_folder, headers=cf.headers)

    if (response.status_code == 200):
        retorno_folder = response.json()
        obj_folder = Folder()
        #Call function that persists in DBMS and return the ID_list
        lista_folder.append(obj_folder.read_folder(retorno_folder))
    else:
        print('without connection')

#Normalize tha list, because the return came list inside list
for sublist in lista_folder:
    for item in sublist:
        flat_lista_folder.append(item)

'''
For each ID saved in folders list, will be call the next URL with ID parameter and will catch the id list
'''
for lf in flat_lista_folder:

    url_list = cf.root_url+'/folder/'+lf[0]+'/list'

    response = requests.get(url_list, headers=cf.headers)

    if (response.status_code == 200):
        retorno_list = response.json()
        obj_list = List()
        #Call function that persists in DBMS and return the ID_list
        lista_listas.append(obj_list.read_list(retorno_list))
    else:
        print('without connection')

#Normalize tha list, because the return came list inside list
for sublist in lista_listas:
    for item in sublist:
        flat_lista_listas.append(item)

#Append list of lists with list of lists without folder
flat_lista_listas.extend(flat_lista_sem_folder)

'''
For each ID saved in list of lists, will be call two functions to catch the tasks and save in DBMS
'''
for lt in flat_lista_listas:
    obj_task = Task()
    
    print('picking up unfiled tasks')
    obj_task.get_task(lt[0],0) 
    
    print('picking up archived tasks')
    obj_task.get_task(lt[0],1)

print('Finished')
