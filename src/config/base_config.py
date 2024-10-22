# config.py
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from exceptions.custom_exceptions import ConfigurationException

# Determine the environment and load the appropriate .env file
app_env = os.getenv('APP_ENV')  

if app_env == 'dev':
    load_dotenv('.env.dev')
elif app_env == 'uat':
    load_dotenv('.env.uat')
elif app_env == 'prod':
    load_dotenv('.env.prod')
else:
    load_dotenv('.env.local')
    
     
class Config:

    APP_ENV = app_env

    #Disk paths & URL
    BASE_URL = os.getenv('BASE_URL')
    VETVISION_UPLOAD = os.getenv('VETVISION_UPLOAD')
    VECTORSTORE = os.getenv('VECTORSTORE')
    #mongodb credentials 
    VETVISION_MONGO_URI = os.environ.get('VETVISION_MONGO_URI')
    VETREFS_MONGO_URI = os.environ.get('VETREFS_MONGO_URI')
    #openai credentials 
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    LLM_NAME = os.environ.get('LLM_NAME')

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ConfigurationException("OPENAI_API_KEY not found in environment variables")

# Usage: Create an instance of Config to access settings
config = Config()

