'''
user.py: Modulo para definir el modelo Usuario
'''
from mongoengine import Document, StringField, DateTimeField


class User(Document):
    '''
    Clase que define el modelo usuario
    '''
    name = StringField(required=True)
    last_name = StringField(required=True)
    telephone = StringField(required=True)
    birthdate = DateTimeField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    residence = StringField(required=True)
    district = StringField(required=True)
    postal_code = StringField(required=True)

    def json(self):
        '''
        Metodo que devuelve los atributos de la clase en formato json
        '''
        user_dict = {
            'user_id': str(self.pk),
            "name": self.name,
            "last_name": self.last_name,
            "telephone": self.telephone,
            "birthdate": {
                "day": self.birthdate.day,
                "month": self.birthdate.month,
                "year": self.birthdate.year
            },
            "email": self.email,
            "password": self.password,
            "residence": self.residence,
            "district": self.district,
            "postal_code": self.postal_code
        }
        return user_dict

    meta = {
        "indexes": ["district"]
    }
