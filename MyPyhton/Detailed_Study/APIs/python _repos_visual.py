import requests

from plotly.graph_objs import Bar
from plotly import offline

# read for plotly details at https://plot.ly/python/user-guide/
# https://plot.ly/python/reference/ lists all the settings you can use to configure Plotly visualizations
# GitHub API, refer to its documentation at https://developer.github.com/v3/.

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# to find teh search free limit https://api.github.com/rate_limit

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

# process results
# store API response in a variable
response_dict = r.json()
repo_dicts = response_dict['items']

#repo_names, stars, labels = [], [], []
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
    #repo_names.append(repo_dict['name'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

# custom hover text
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualization.
data = [{
    'type': 'bar',
    #'x': repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
              },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
              },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_response.html')

