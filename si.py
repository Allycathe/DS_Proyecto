import osmnx as ox

lugar = "Providencia, Santiago, Chile"

# 1. El límite
limite = ox.geocode_to_gdf(lugar)
print(limite)

# 2. Elementos por tag
parques = ox.features_from_place(lugar, tags={"leisure": "park"})
print(parques.columns)

# 3. La red vial
G = ox.graph_from_place(lugar, network_type="drive")
nodos, aristas = ox.graph_to_gdfs(G)



