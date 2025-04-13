import boto3
import logging
import psycopg2
import os
import yaml

s3 = boto3.client('s3')
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger(__name__)

with open('pw.txt','r') as f:
    pw = f.read()

with open('./config/config.yaml','r') as f:
    config = yaml.safe_load(f)

s3_key = config['s3']['s3_key']
file_path = config['local']['file_path'] 
bucket_name = config['s3']['bucket_name']


def load_s3(s3_key,file_path,bucket_name):
    try:
        s3.upload_file(file_path,bucket_name,s3_key)
        logger.info("SUCCESSFULLY LOADED")
        print('Loaded successfully')
    except Exception as e:
        print("Failed", e)
        logger.error("FAILED")

load_s3(s3_key,file_path,bucket_name)

def load_postgres(table_name):
    conn = psycopg2.connect(
        host = config['HOST'],
        port = config['PORT'],
        user = config['USERNAME'],
        password = pw,
        database = config['DATABSE']
    )
    cursor = conn.cursor()
