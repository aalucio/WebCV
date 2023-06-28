import os
from whoosh.fields import *
from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import open_dir
from whoosh import qparser


#1
schema = Schema(Titulo=TEXT(stored=True), Noticia=TEXT(stored=True), Resumen=TEXT(stored=True))
if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)

#2
def index_document(filename):
    with open(filename, "r") as f:
        # Aquí se deben extraer los valores del documento (título, noticia, resumen)
        Titulo = ...
        Noticia = ...
        Resumen = ...
        writer = ix.writer()
        writer.add_document(Titulo=Titulo, Noticia=Noticia, Resumen=Resumen)
        writer.commit()

# Aquí se debe llamar a index_document para cada archivo que se quiera indexar


#3
search_field = input("¿En qué campo desea buscar? (título/noticia/resumen) ")

#4
# Crear un objeto QueryParser
parser = qparser.QueryParser(search_field, schema=schema)

# Crear una consulta a partir de la entrada del usuario
query_str = input("Ingrese su consulta: ")
query = parser.parse(query_str)

#5

# Crear un objeto Searcher
searcher = ix.searcher()

# Buscar los documentos que coinciden con la consulta
results = searcher.search(query)

# Imprimir los resultados
for hit in results:
    print(hit["Titulo"]) # o cualquier otro campo que desee imprimir

