# 구조

advanced_project/
│
├── airflow_env/              (Airflow 환경)
│   ├── dags/
│   │   └── my_dag.py
│   ├── plugins/
│   ├── config/                (옵션: key.json 같은 config)
│   ├── .env
│   ├── docker-compose.yml
│   ├── Dockerfile             (Airflow 전용 Dockerfile)
│
├── notebooks/                 (Jupyter 작업 폴더)
│   └── eda.ipynb              (EDA 작업용 노트북 등)
│
├── README.md
├── requirements.txt
└── .gitignore
