from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

from dash import Dash, dcc,html,Output,Input,page_container,page_registry
from controllers.auth import auth
import dash_bootstrap_components as dbc
from dash_auth import BasicAuth
from auth import authorization_function

external_scripts=[
    {'src': 'https://cdn.tailwindcss.com'}
]
server=Flask(__name__)

app=Dash(
    __name__,
    server=server,
    use_pages=True,
    pages_folder="pages",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=external_scripts,
    url_base_pathname="/"
)
app.scripts.config.serve_locally=True
BasicAuth(app,auth_func=authorization_function)


server.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///transactdb.db"
server.config['SECRET_KEY']="SUPER_SECRET_KEY"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# app.config["JWT_COOKIE_SECURE"] = False
# app.config["JWT_SECRET_KEY"] = "super-secret"
# app.config['CACHE_TYPE']='simple'
# app.config['MODEL_PATH']='path/to'
# app.config['JWT_COOKIE_CSRF_PROTECT']=False
# app.config['JWT_TOKEN_LOCATION'] = ["headers", "cookies", "json", "query_string"]

db=SQLAlchemy(server)
# jwt=JWTManager(app)
# cache = Cache(app)
# socket=SocketIO(app,cors_allowed_origins="*")