from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from models import Product, responses
from database import create_item, retrieve_item_by_id, retrieve_items_by_parameters

app = FastAPI(title='Item application')


@app.get('/item/{item_id}')
async def get_item(item_id: str):
    return retrieve_item_by_id(item_id)


@app.get('/items/')
async def get_items(request: Request):
    return retrieve_items_by_parameters(dict(request.query_params))


@app.post('/item')
async def add_item(item: Product):
    new_item = create_item(jsonable_encoder(item))
    return responses(new_item, 'Successfully added to the DB!')