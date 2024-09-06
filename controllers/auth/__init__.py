from flask import Blueprint

auth=Blueprint("auth",__name__,url_prefix="/api/v1/auth")

@auth.route("",methods=['GET'])
def index():
    return "mridul"