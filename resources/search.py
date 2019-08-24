from flask import request, current_app
from flask_restful import Resource
import time
import json
from redisearch import TextField, NumericField, Query, AutoCompleter, Suggestion


class Search(Resource):
    def get(self):
        keyword = request.args['term']
        ac = AutoCompleter(current_app.config["REDISSEARCH_INDEX"], current_app.config["REDISSEARCH_URI"])
        res = ac.get_suggestions(keyword, fuzzy = True)
        return {"suggestion": [x.string for x in res]}, 200

class Add(Resource):
    def post(self):
        mydata = request.json
        location = str(mydata['location'])
        ac = AutoCompleter(current_app.config["REDISSEARCH_INDEX"], current_app.config["REDISSEARCH_URI"])
        res = ac.get_suggestions(location, 1.0)
        if len(res)>0:
            data = {'msg': 'Location already present'}
        else:
            ac.add_suggestions(Suggestion(location, 1.0))
            data = {'status': 'Location added'}
        return data, 200

class Delete(Resource):
    def post(self):
        mydata = request.json
        location = str(mydata['location'])
        ac = AutoCompleter(current_app.config["REDISSEARCH_INDEX"], current_app.config["REDISSEARCH_URI"])
        res = ac.get_suggestions(location, 1.0)
        if len(res)>0:
            #ac.delete_document
            data = {'msg': 'Location deleted'}
        else:
            data = {'status': 'No Location Present'}
        return data, 200
        data = {'status': 'OK'}
        return data, 200
