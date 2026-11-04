import os
from sqlalchemy import create_engine, URL
from dotenv import load_dotenv

load_dotenv()

#header API
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
}
root_url = 'https://api.clickup.com/api/v2/'

#Team ID CLICKUP
Space = os.getenv('SPACE_TEAM')

#Conexão banco
host=os.environ["HOST"]
user=os.environ["USER"]
password=os.environ["PASSWORD"]
banco =os.environ["DATABASE"]

url = URL.create("mysql+pymysql",username=user,password=password,host=host,port=3306,database=banco)

conexao = create_engine(url)
