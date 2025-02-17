import boto3
import logging
import psycopg2
import os
import config

s3 = boto3.clent('s3')
logger = logging.getLogger(__name__)

with open('pw.txt','r') as f:
    pw = f.read(f)

def load_s3(file_name,key,bucket):
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    try:
        s3.upload_file(file_name,key,bucket)
        logger.INFO("SUCCESSFULLY LOADED")
    except Exception as e:
        print("Failed")
        logger.ERROR("FAILED")

def load_postgres(table_name):
    conn = psycopg2.connect(
        host = config['HOST'],
        port = config['PORT'],
        user = config['USERNAME'],
        password = pw,
        database = config['DATABSE']
    )
    cursor = conn.cursor()
