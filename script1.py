import folium

import pandas


data=pandas.read_csv("coord.txt")


map=folium.Map(location=[13.0927, 80.2707], zoom_start=6, title="Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")

fg.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),

style_function=lambda  x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 

else 'blue' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'orange' if 50000000 <= x['properties']['POP2005'] < 900000000 else 'red' }))

map.add_child(fg)

map.save("pop.html")
