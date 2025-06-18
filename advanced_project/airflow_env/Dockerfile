FROM apache/airflow:2.9.1

# 필요한 패키지 있으면 추가 설치 가능
USER root

# 예: OS 패키지 설치
# RUN apt-get update && apt-get install -y gcc

USER airflow

# Python 패키지 설치 (옵션)
# requirements.txt가 있다면 다음처럼 설치
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# dags, plugins 폴더는 docker-compose에서 볼륨으로 마운트할 것이므로 복사할 필요 없음
