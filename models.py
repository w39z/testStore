from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    parameters: List[dict] = []

    class Config:
        schema_extra = {
            "example": {
                "name": "MacBook",
                "description": "notebook",
                "parameters": [
                    {"year of release": "2021"},
                    {"manufacturer": "Apple"},
                    {"availability": "Yes"},
                ]
            }
        }


def responses(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }