import dash
from dash import html

# Import the offline detect plugin
from dash_offline_detect_plugin import setup_offline_detect_plugin

# Enable the offline detect plugin for the current app, default interval is 5000ms
setup_offline_detect_plugin()

app = dash.Dash(__name__)

app.layout = html.Div("Test App.", style={"padding": 50})

if __name__ == "__main__":
    app.run()
