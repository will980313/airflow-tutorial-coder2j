from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Task 공통 속성값 정의
default_args = {
    'owner': 'jueon',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# Dag 정의
with DAG(
    dag_id='my_first_dag',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2023, 4, 25),
    schedule_interval='@daily'
) as dag:
    
    # Task 정의
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hey, I am task2 and will be running after task1!"
    )

    task3 = BashOperator(
        task_id='thrid_task',
        bash_command="echo hey, I am task3 and will be running after task1 at the same time as task2!"
    )

    # Task 종속성
    # task는 다른 task들과 종속성을 가진다


    # Task 종속성을 나타내는 방법들

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]