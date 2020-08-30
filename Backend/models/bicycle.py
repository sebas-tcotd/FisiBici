from mongoengine import *
import base64

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
            "img": str(base64.b64encode(self.image.read()), 'utf-8'),
            "thumbnail": str(base64.b64encode(self.image.thumbnail.read()), 'utf-8')
        }
        return bicycle_dict

    meta = {
        "indexes": ["name"]
    }