# README

가상환경 셋팅

```text
python -m venv venv
```

가상환경 접속

```text
source venv/Scripts/activate/
```

MovieData 저장

```text
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata moviedata.json
```

패키지 설치

```text
pip install -r requirements.txt
```