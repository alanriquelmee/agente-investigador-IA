import os 
from langchain_community.utilities import SerpAPIWrapper
os.environ['SERPAPI_API_KEY'] = 'd1bf6d7574345617f5efc875360ab489a9ac2dbf3154c9b2ba13f3ecd9646bef'


#creamos la instancia del buscador web
buscador = SerpAPIWrapper()

# consulta que se realizara 
consulta = "Avances de la inteligencia artificial en Paraguay año 2025"

# se ejecuta la busqueda y se almacenan los resultados 
resultados = buscador.run(consulta)

#se muestra el resultado

print("\n Resultados brutos de la busqueda: \n")
print(resultados)