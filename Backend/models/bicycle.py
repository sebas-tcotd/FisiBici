from mongoengine import *

class Bicycle(Document):
    name = StringField(unique=True, required=True)
    price = FloatField(required=True)

    def json(self):
        bicycle_dict = {
            'id': str(self.pk),
            "name": self.name,
            "price": self.price
        }

        return bicycle_dict

    meta = {
        "indexes": ["name", "price"]
    }