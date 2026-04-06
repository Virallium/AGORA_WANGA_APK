import folium 

carte=folium.Map(location=[-4.387953529076802, 15.43947438882351],zoom_start=13)
lieux=[
     {
         "name":"AGORA WANGA",
         "catg":"Agence",
         "description":"Ceci est la résidence de AGORA WANGA",
         "coords":[-4.346624545338484, 15.273659641814447],
     },
]
for lieu in lieux:
    folium.Marker(
        location=lieu["coords"],
        popup=lieu["name"],
        tooltip=lieu["description"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(carte)
carte.save("templates/pages/carte.html")