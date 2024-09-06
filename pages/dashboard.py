import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,path="/")

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

layout=html.Div(
    children=[
    navbar,
    ],
    className="h-screen w-full bg-gradient-to-t from-violet-500 to-fuchsia-500 text-white"
)