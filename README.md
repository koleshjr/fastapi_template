# pyday-fastapi
Learning how to create and deploy fastapi apps
FastAPI has risen in popularity because it is fast to build and execute, it utilizes python types and automatical generates for you the API documentation via the swagger UI

## Folder one: Utils
Holds all the helper function needed to make up the API

## Folder two: api
Holds the main.py file which has the api executable code and requirements.txt which holds all the requirements required in production
Also has guinicorn.conf.py required for productionizing the FastAPI 

## Folder three: tests
Holds the test_api.py which has unit tests for your api code and property_based_tests.py which runs a bunch of code and tests on your api 

## requirements-dev.txt
Holds all the requirements to run the API and for development testing

## pyproject.toml
Python standard for test generation

## Deploying the API on Microsoft Azure on VS Code
Download the Azure Tools Pack extension
Sign in
Select "Create Resources" -> "Create App Service Web App" 
Enter a name
Select runtime stack e.g python 3.11
Select the tier
Once that is done "deploy" and select the "api" as the path to deploy
Go to your created app service on Azure and select "configuration" > "general settings" then add the code line below on the startup command: python3 -m gunicorn main:app

## Deployed version of this template:
Try it out: https://fastai-pydata.azurewebsites.net/docs
