from mongoengine import *

class Bicycle(Document):
    name = StringField(required=True)
    price = FloatField(required=True)
    colors = ListField(StringField(), required=True)
    stock = IntField(default=1)
    use = StringField(default="General")


    def json(self):
        bicycle_dict = {
            'id': str(self.pk),
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "colors": self.colors,
            "use": self.use
        }

        return bicycle_dict

    meta = {
        "indexes": ["name"]
    }