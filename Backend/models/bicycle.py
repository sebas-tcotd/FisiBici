from mongoengine import *

class Bicycle(Document):
    name = StringField(required=True)
    price = FloatField(required=True)
    colors = ListField(StringField(), required=True)
    stock = IntField(default=1)
    use = StringField(default="General")
    image = ImageField(thumbnail_size=(320, 240, False))


    def json(self):
        bicycle_dict = {
            'id': str(self.pk),
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "colors": self.colors,
            "use": self.use,
            "img": str(self.image.read()),
            "thumbnail": str(self.image.thumbnail.read())
        }

        return bicycle_dict

    meta = {
        "indexes": ["name"]
    }