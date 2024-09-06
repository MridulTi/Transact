from dash import Dash

def authorization_function(username,password):
    if(username =="mridul" ) and (password=="#mridul"):
        return True
    else:
        return False