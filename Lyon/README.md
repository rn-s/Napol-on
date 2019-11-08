Lyon
====

## 説明
    Google Place APIのラッパーAPI
    Basic + Detail格納
    
    For Python 3.7.4

2019/10/24 : 基本情報と詳細情報の格納部分まで

## 使い方
    python manage.py makemigrations shop
    python manage.py migrate
    python manage.py runserver
※listenは適宜

## インストール
ライブラリなど

    pip install django
    pip install djangorestframework
    pip install django-rest-swagger
    pip install django-filter
    pip install mysqlclient
    pip install requests
    pip install ppretty

## エンドポイント
    GET http://[url]:[port]/swagger/
    GET http://[url]:[port]/shop/
    GET http://[url]:[port]/shop/update_google/
    
## Author
@kagamikarasu