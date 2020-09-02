'''
bicycle.py: Modulo para definir el modelo Bicicleta
'''
import base64
from mongoengine import Document, StringField, ImageField
from mongoengine import FloatField, ListField, IntField

class Bicycle(Document):
    '''
    Clase que define el modelo bicicleta
    '''
    name = StringField(required=True)
    price = FloatField(required=True)
    colors = ListField(StringField(), required=True)
    stock = IntField(default=1)
    use = StringField(default="General")
    image = ImageField(thumbnail_size=(320, 240, False))

    def json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
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
