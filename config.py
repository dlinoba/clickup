import os
from sqlalchemy import create_engine
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
host=os.environ["host"]
user=os.environ["user"]
password=os.environ["password"]
banco =os.environ["database"]

conexao = create_engine("mysql+pymysql://"+user+":"+password+"@"+host+":3306/"+banco,echo=True)
