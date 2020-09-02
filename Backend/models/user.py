from mongoengine import *

class User(Document):
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