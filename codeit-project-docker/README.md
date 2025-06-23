# branch 가져온 후 

0. 가상환경을 생성 및 실행
```bash
# 가상환경 생성
python3 -m venv google_cloud

# 터미널에서 가상환경 접속
source google_cloud/bin/activate
```

1. 가상환경 실행을 위해서 requirements 있는 곳으로 이동 후 필요한 라이브러리 설치
```bash
cd codeit-project-docker
pip install -r requirements.txt
```

1-1. 라이브설치 후 search_for_activation.ipynb 라이브러리 실행 중 문제
```bash
# 식별된 문제
ModuleNotFoundError: No module named 'distutils'

# 해결 방법
## koreanize 최신버전으로 업그레이드
pip install --upgrade koreanize-matplotlib
```
