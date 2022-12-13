from app import app
from model.model_response import model_class
from flask import request
obj = model_class()
@app.route("/user/getall")
def get_data():
    return obj.get_all_data()

@app.route("/user/post",methods=['POST'])
def post_data():
    return obj.post_all_details(request.form)