import requests
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Random User Generator API endpoint
base_url = 'https://randomuser.me/api/'

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Random User Generator Dashboard"),
    html.Button('Get Random User', id='submit-button', n_clicks=0),
    html.Div(id='user-output')
])

# Callback to fetch and display random user data
@app.callback(
    Output('user-output', 'children'),
    [Input('submit-button', 'n_clicks')]
)
def update_user(n_clicks):
    # Make request to Random User Generator API
    response = requests.get(base_url)

    if response.status_code == 200:
        user_data = response.json()['results'][0]

        # Extract relevant information from the JSON response
        first_name = user_data['name']['first']
        last_name = user_data['name']['last']
        email = user_data['email']
        picture = user_data['picture']['large']

        # Display user information
        user_info = html.Div([
            html.Img(src=picture, style={'width': '150px', 'height': '150px'}),
            html.H3(f"{first_name} {last_name}"),
            html.P(f"Email: {email}")
        ])
        return user_info
    else:
        return html.P("Failed to fetch user data.")

if __name__ == '__main__':
    app.run_server(debug=True)
