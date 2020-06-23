import os
import slug
import json
from app import app
from flask import jsonify, Response, request
from app.models import Shop, Category, Products


@app.route('/products', methods=['GET'])
def Products(id):
    items = Products.objects().filter(shop=id).to_json()
    return jsonify(items), 200


@app.route('/product', methods=['POST'])
def CreateProduct():
    body = request.get_json()
    body['slug'] = slug.slug(body['name'])
    items = Products(**body).save()
    return Response(items, mimetype="application/json", status=200)