import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

from google.cloud import storage
from google.oauth2 import service_account

KEY_PATH = "/opt/airflow/config/key.json"
BUCKET_NAME = "my-advanced_data-bucket"

def list_gcs_files():
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    client = storage.Client(credentials=credentials)
    bucket = client.bucket(BUCKET_NAME)

    prefixes = ["votes/", "hackle_final/"]

    for prefix in prefixes:
        print(f"[📁 GCS 폴더 탐색]: {prefix}")
        blobs = bucket.list_blobs(prefix=prefix)
        for blob in blobs:
            print(f"[📄 파일 발견]: {blob.name}")

with DAG(
    dag_id="check_gcs_files_dag",
    schedule_interval=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["debug", "GCS"],
) as dag:
    
    check_task = PythonOperator(
        task_id="list_gcs_file_names",
        python_callable=list_gcs_files,
    )
