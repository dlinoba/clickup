from sqlalchemy import create_engine

#header API
headers = {'Authorization': 'YOUR COD AUTHORIZATION'}
root_url = 'https://api.clickup.com/api/v2/'

#Team ID CLICKUP
Space = 'YOUR SPACE TEAM'

#Conexão banco
host='IP YOUR DBMS'
user='USER'
password='PASSWORD'
banco = 'DATABASE'

conexao = create_engine("mysql://"+user+":"+password+"@"+host+":3306/"+banco,echo=True)