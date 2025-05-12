from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import sys
sys.path.append('/usr/local/airflow/app')  # caminho para importar o módulo dentro do container

from producer_utils import buscar_e_enviar

default_args = {
    'owner': 'lucas',
    'start_date': datetime(2025, 5, 12),
    'retries': 0
}

dag = DAG(
    'coleta_api_para_kafka',
    default_args=default_args,
    schedule_interval='*/5 * * * * *',  # A cada 5 segundos
    catchup=False
)

task = PythonOperator(
    task_id='buscar_e_enviar_para_kafka',
    python_callable=buscar_e_enviar,
    dag=dag
)
