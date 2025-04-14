from pyspark.sql import SparkSession
import yaml


class ETL:
    def __init__(self,app_name:str):
        self.spark = (SparkSession.builder.appName(app_name) \
                      .config("spark.hadoop.fs.s3a.access.key", "your-aws-access-key") \
                      .config("spark.hadoop.fs.s3a.secret.key", "your-aws-secret-key") \
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
    
    def write_to_postgres(self,transformed_df,table:str,password:str,port:int,user:str,host:str):
        properties = {
            "user":user,
            "password":pw,
            "host":host,
            "table":table,
            "port":port
        }
        transformed_df.write.mode('overwrite')
    

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


if __name__ =="__main":
    processing = ETL(appName="Jumia_transformation")
    input_path = ""
    df = processing.read_file(input_path)
    transformed = processing.transform()
    processing.write_to_postgres()