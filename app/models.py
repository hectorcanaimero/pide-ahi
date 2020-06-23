from app import db


class Users(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)


class Products(db.Document):
    name = db.StringField()
    slug = db.StringField(required=True)
    description = db.StringField()
    image = db.DictField()
    extras = db.DictField()
    preco = db.DictField()
    category = db.StringField()
    shop = db.StringField()


class Category(db.Document):
    name = db.StringField(required=True)
    slug = db.StringField(required=True)
    shop = db.StringField()


class Shop(db.Document):
    name = db.StringField(required=True)
    slug = db.StringField()
    nit = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    phone = db.IntField(required=True, unique=True)
    address = db.DictField()
    shipping = db.DictField()
    categories = db.ReferenceField(Category)