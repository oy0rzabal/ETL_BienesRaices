import json
from datetime import datetime, timedelta
import os
import logging
import airflow
from airflow.models import Variable
from airflow import models
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
import snowflake.connector as sf
import pandas as pd
import time
import random
import os
from utils import get_data,data_processing
from datetime import datetime


#Autor de quien lo hizo:
default_arguments = {
    'owner': 'oy0rzabal',
    'email': 'oy0rzabal.l0pez@gmail.com',
    'retries':1 ,
    'retry_delay':timedelta(minutes=5)
}

#Empezamos a realizar el DAG para el webscraping:
with DAG('Bienes_Raices',
         default_args=default_arguments,
         description='Extracting Data' ,
         start_date = datetime(2022, 9, 21),
         schedule_interval = None,
         tags=['tabla_espn'],
         catchup=False) as dag :

         params_info = Variable.get("feature_info", 
         deserialize_json=True)

         extract_data = PythonOperator(task_id='EXTRACT_OFICINES',
                                    provide_context=True,
                                    python_callable=extract_info,
                                    op_kwargs={"df":df,"df_team":df_team})

         params_info = Variable.get("params_info = Variable.get("feature_info", deserialize_json=True)")
         rentas= pd.read_csv('rentas.csv')
         rentas_2= pd.read_csv('rentas_2.csv')
         def etl_transform():

