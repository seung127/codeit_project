import os
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

from google.cloud import storage
from google.oauth2 import service_account
import pandas as pd

# 설정
KEY_PATH = "/opt/airflow/config/key.json"
BUCKET_NAME = "my-advanced_data-bucket"
RAW_DATA_PATH = "/opt/airflow/data/raw/"

default_args = {
    "owner": "airflow",
    "retries": 1,
}

# GCS에서 parquet 파일 다운로드 (prefix별 2개만)
def load_gcs_data(only_test=True):
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    client = storage.Client(credentials=credentials)
    bucket = client.bucket(BUCKET_NAME)

    prefixes = ["votes/", "hackle_final/"]
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    for prefix in prefixes:
        print(f"▶ 탐색 중: {prefix}")
        blobs = list(bucket.list_blobs(prefix=prefix))  # 미리 리스트로 변환
        downloaded = 0

        for blob in blobs:
            if blob.name.endswith(".parquet"):
                gcs_path = f"gs://{BUCKET_NAME}/{blob.name}"
                file_name = blob.name.split('/')[-1].replace(".parquet", "")
                df = pd.read_parquet(gcs_path, storage_options={"token": KEY_PATH})
                local_file_path = os.path.join(RAW_DATA_PATH, f"{file_name}.parquet")
                df.to_parquet(local_file_path, index=False)
                print(f"[✅ 저장 완료] {gcs_path} → {local_file_path}")

                downloaded += 1
                if only_test and downloaded >= 2:
                    print(f"🔒 테스트 모드: 2개까지만 다운로드 완료")
                    break

with DAG(
    dag_id="load_gcs_data_dag",
    schedule_interval=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    default_args=default_args,
    tags=["data_load", "GCS"],
) as dag:

    load_task = PythonOperator(
        task_id="load_data_from_gcs",
        python_callable=load_gcs_data,
        op_kwargs={"only_test": True},  # True이면 2개만 다운로드
    )
