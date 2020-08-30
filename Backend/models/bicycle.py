from mongoengine import *

class Bicycle(Document):
    name = StringField(unique=True, required=True)
    price = FloatField(required=True)

    def json(self):
        bicycle_dict = {
<<<<<<< HEAD
=======
            'id': str(self.pk),
>>>>>>> origin/backend
            "name": self.name,
            "price": self.price
        }

        return bicycle_dict

    meta = {
        "indexes": ["name", "price"]
    }