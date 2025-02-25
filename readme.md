# Installation and Project Guide

## Create Virtual Environment
```
python -m venv env
```

## Activate the environment
```
source env/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## Run Migrations
```
python manage.py migrate
```

## Run the Server
```
python manage.py runserver
```

# API Guid

## Create Candidate
Hit Endpoint http://127.0.0.1:8000/v1/candidate/ with **POST** method and payload
```
{
    "id": 1,
    "phone_number": "9598119099",
    "name": "Rohan Dixit",
    "age": 25,
    "gender": "male",
    "email": "rohandixit@gmail.com"
}
```
Or alternatively use curl
```
curl --location 'http://127.0.0.1:8000/v1/candidate/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": 1,
    "phone_number": "9598119099",
    "name": "Rohan Dixit",
    "age": 25,
    "gender": "male",
    "email": "rohandixit@gmail.com"
}'
```
## List All Candidate
Hit API endpont http://127.0.0.1:8000/v1/candidate/ with **GET** method
or alternatively use curl
```
curl --location 'http://127.0.0.1:8000/v1/candidate/' \
--data ''
```
## Update Candidate
Hit API endpont http://127.0.0.1:8000/v1/candidate/1/ with **PUT** method and payload
```
{
    "phone_number": "9598119099",
    "name": "Rohan Dixit",
    "age": 25,
    "gender": "male",
    "email": "rohandixit@gmail.com"
}
```
alternatively can use curl
```
curl --location --request PUT 'http://127.0.0.1:8000/v1/candidate/1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "phone_number": "9598119099",
    "name": "Rohan Dixit",
    "age": 25,
    "gender": "male",
    "email": "rohandixit@gmail.com"
}'
```
## Delete Candidate
Hit API endpoint http://127.0.0.1:8000/v1/candidate/1/ with **DELETE** method
or alternatively use curl
```
curl --location --request DELETE 'http://127.0.0.1:8000/v1/candidate/1/' \
--data ''
```
## Search Candidate
Hit API endpoint http://127.0.0.1:8000/v1/candidate/?search=Rohan Dixit Yadav with method **GET**
or alternatively use curl
```
curl --location 'http://127.0.0.1:8000/v1/candidate/?search=Rohan%20Dixit%20Yadav' \
--data ''
```