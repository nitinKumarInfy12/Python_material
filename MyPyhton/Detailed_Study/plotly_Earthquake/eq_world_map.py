import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# explore the structure of the data
#filename = 'data/eq_data_1_day_m1.json'
filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    #json_str = f.read()
    #print(len(json_str))
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)


all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))
#print(all_eq_dicts[0])

# extract the eq magnitudes
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)


# map the earth quakes
#data = [Scattergeo(lon=lons, lat=lats)]
# this allows teh customization of data
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
     'marker': {
         'size': [5*mag for mag in mags],
         'color': mags,
         'colorscale': 'Viridis',
         'reversescale': 'True',
         'colorbar': {'title': 'Magnitude'},
     },
    }]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')