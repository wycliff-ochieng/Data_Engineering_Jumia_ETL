from pyspark.sql import SparkSession
import yaml


class ETL:
    def __init__(self,app_name:str):
        self.spark = (SparkSession.builder.appName(app_name) \
                      .config("spark.hadoop.fs.s3a.access.key", access_key) \
                      .config("spark.hadoop.fs.s3a.secret.key", secret_key) \
                      .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
                      .config("spark.hadoop.fs.s3a.connection.maximum", "100") \
                      .getOrCreate())

    def read_file(self):
        df = self.spark.read.option('header','true').csv('s3://reddit-backo/rawData/jumiatv.csv')
        print(df.show(50))
        return df
    
    def transform(self,df):
        transformed_df = df.dropna()
        return transformed_df
    
    def write_to_postgres(self,transformed_df,table:str,pw:str,port:int,user:str,host:str):
        jdbc_url = f"jdbc:postgresql://{host}:{port}/your_database_name"
        properties = {
            "user":user,
            "password":pw,
            "driver":"org.postgres.Driver"
        }

        transformed_df.write.jdbc(url=jdbc_url,table=table,mode='overwrite',properties=properties)
    

    def stop(self):
        self.spark.stop()

with open('pw.txt','r') as f:
    pw = f.read()

with open('./config/config.yaml','r') as f:
    config = yaml.safe_load(f)

table = config['postgres']['table_name']
user = config['postgres']['user']
host = config['postgres']['user']
port = config['postgres']['host']
access_key = config['s3']['access_key']
secret_key = config['s3']['access_key']


if __name__ =="__main":
    processing = ETL(appName="Jumia_transformation")
    input_path = ""
    df = processing.read_file(input_path)
    transformed = processing.transform()
    processing.write_to_postgres()