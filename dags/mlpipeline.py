from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

## Define Task 1
def preprocess_data():
    print("Preprocessing data...")

## Define Task 2
def train_model():
    print("Training model...")

## Define Task 3
def evaluate_model():
    print("Evaluate models...")

# Define DAG

with DAG(
    'ml_pipeline',
    start_date=datetime(2025,1,27),
    schedule_interval='@weekly'
) as dag:

    ## Define the Task
    preprocess=PythonOperator(task_id="preprocess_task",python_callable=preprocess_data)
    train=PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate=PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)

    ## Set Dependencies
    preprocess >> train >> evaluate
