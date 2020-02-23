import json

# explore the structure of the data

filename = 'data/eq_data_1_day_m1.json'

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
mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


