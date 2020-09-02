from mongoengine import *

class User(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    residence = StringField(required=True)
    district = StringField(required=True)
    postal_code = StringField(required=True)

    def json(self):
        user_dict = {
            'user_id': str(self.pk),
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