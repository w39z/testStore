# Инсталяция проекта:
```bash
pip install -r requirements.txt
```
# Запуск проекта:
## 1. Запуск базы данных с помощью Docker
```bash
docker run -d -p 27017:27017 mongo
```
## 2. Запуск проекта через unicorn
```bash
uvicorn main:app --reload
```
Проект запущен на локальном сервере http://127.0.0.1:8000/
Чтобы открыть интерактивную документацию можно перейти по пути: http://127.0.0.1:8000/docs/ или http://127.0.0.1:8000/redoc/
# curl команды:
## 1. Создание товара: 
```bash
curl -X POST "http://127.0.0.1:8000/item" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"MacBook\",
\"description\":\"notebook\",\"parameters\":[{\"year of release\":\"2021\"},{\"manufacturer\":\"Apple\"},{\"availability\":\"Yes\"}]}"
```
В данном случае поля наименования и описания товара являются обязательными, id генерируется автоматически, а параметры могут быть в бесконечном количестве, как и не быть вовсе.
## 2. Поиск по параметру: 
```bash
curl -X GET curl -X GET "http://127.0.0.1:8000/items/?name=MacBook&description=notebook&availability=Yes" -H  "accept: application/json"
```
В поиске может быть использован один или несколько параметров.
## 3. Детали найденного товара: 
```bash
curl -X GET "http://127.0.0.1:8000/item/ "id товара" " -H  "accept: application/json"
```
