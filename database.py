from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['products_DB']
col = db['prod_col']


def main(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': str(item['name']),
        'description': str(item['description']),
        'parameters': item['parameters'],
    }


def create_item(item_data: dict) -> dict:
    item = col.insert_one(item_data)
    new_item = col.find_one({'_id': item.inserted_id})
    return main(new_item)


def retrieve_item_by_id(id: str) -> dict:
    if ObjectId.is_valid(id):
        item = col.find_one({'_id': ObjectId(id)})
        return main(item)
    else:
        return {'error': 'id is not found'}


def retrieve_items_by_parameters(params: dict):
    items = []
    query = {}

    for p in params:
        if p in ['name', 'description']:
            query[p] = {'$regex': params[p]}
        else:
            query['parameters.' + p] = params[p]
    for item in col.find(query, {"name": 1, "_id": 0}):
        items.append(item)
    return items
