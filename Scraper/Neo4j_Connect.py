from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, nombre):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, nombre)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, nombre):
        tx.run("CREATE (:Autor {nombre: $nombre})", nombre=nombre)
        #return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "PT_DB1220")
    greeter.print_greeting("hello, world")
    greeter.close()