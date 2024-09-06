import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__,path="/login")
ALLOWED_TYPES = [
    ("email","Email Address"),
    ("text","Username"),
    ("password","Password"),
]

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#",className="text-gray-600")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True,className="text-gray-600"),
                dbc.DropdownMenuItem("Page 2", href="#",className="text-white"),
                dbc.DropdownMenuItem("Page 3", href="#",className="text-white"),
            ],
            nav=True,
            in_navbar=True,
            className="text-white",
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="",
    className="text-white",
    dark=True,
)

layout=html.Div([
    navbar,
    html.Div([
        html.Div([
            html.H1("Log in to your account !",className="w-full text-center font-medium text-xl py-2"),
            html.Form([
                html.Div([
                    dbc.Label(name,color="black", className="px-2 font-semibold"),
                    dbc.Input(placeholder=name, type=input_type ,className="rounded-xl"),
                ],className="my-3")for input_type, name in ALLOWED_TYPES
            ]),
             dbc.Button("Login", color="info", className="me-1 text-white font-bold w-full"),
            html.Div([
                dbc.Label(
                    "Don't have an account yet?", 
                    className="w-full text-center font-medium text-md my-4",
                ),
                dcc.Link(
                    "Signup!",
                    href="/Signup",
                    className="text-blue-500 text-center w-full font-medium text-md underline hover:text-blue-700"
                )
            ],className="w-full flex flex-col place-items-center gap-0")
            
        ],className="bg-white text-black rounded-xl px-3 w-96 py-3")
    ],className="grid place-items-center h-full ")
    ],
    className="h-screen w-full bg-gradient-to-t from-violet-500 to-fuchsia-500 text-white"
)
