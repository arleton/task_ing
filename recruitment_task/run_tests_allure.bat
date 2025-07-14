@echo off
pytest --alluredir=allure-results
allure serve allure-results