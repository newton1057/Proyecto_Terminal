from neo4j import GraphDatabase

class Neo4jService (object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def Crear_Author(self, tx, MR_Author, Name, Gender, Classifications):
        tx.run("CREATE (:Autor {MR_Author: $MR_Author, Name: $Name, Gender: $Gender, Classifications: $Classifications})", MR_Author = MR_Author, Name = Name, Gender = Gender, Classifications = Classifications)

URL = "bolt://localhost:7687"
DB = "neo4j"
Password = "PT_DB1220"

BD = Neo4jService(URL, DB, Password) # Crear conexion a BD

Name = 'Alicia Monserrat'
MR_Author = 'MR1234'
Gender = 'Female'
Classifications = ['H1', 'H3']

 # Creamos una sesion para interactuar con Neo4j
BD._driver.session().execute_write(BD.Crear_Author, MR_Author, Name, Gender, Classifications)

BD.close()