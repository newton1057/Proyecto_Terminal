from neo4j import GraphDatabase, RoutingControl


URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "Rocanlover12")


def add_Collaboration(driver, a, b):
    driver.execute_query(
        "MERGE (a:Person {name: $a}) "
        "MERGE (b:Person {name: $b}) "
        "MERGE (a)-[:COLABORA]->(b)"
        "MERGE (b)-[:COLABORA]->(a)",
        a=a, b=b, database_="neo4j",
    )

def create_Node(driver, name , gender):
    driver.execute_query(
        "MERGE (a:Person {name: $name, gender: $gender})",
        name = name, gender = gender, database_="neo4j",
    )

"""
def print_friends(driver, name):
    records, _, _ = driver.execute_query(
        "MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
        "RETURN friend.name ORDER BY friend.name",
        name=name, database_="neo4j", routing_=RoutingControl.READ,
    )
    for record in records:
        print(record["friend.name"])
"""

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    add_Collaboration(driver, "Li, Kunpeng", "Li, Qingye")
    add_Collaboration(driver, "Li, Kunpeng", "Lv, Liye")
    add_Collaboration(driver, "Li, Kunpeng", "Song, Xueguan")
    add_Collaboration(driver, "Li, Kunpeng", "Ma, Yunsheng")
    add_Collaboration(driver, "Li, Kunpeng", "Lee, Ikjin")

    add_Collaboration(driver, "Li, Qingye", "Lv, Liye")
    add_Collaboration(driver, "Li, Qingye", "Song, Xueguan")
    add_Collaboration(driver, "Li, Qingye", "Ma, Yunsheng")
    add_Collaboration(driver, "Li, Qingye", "Lee, Ikjin")

    add_Collaboration(driver, "Lv, Liye", "Song, Xueguan")
    add_Collaboration(driver, "Lv, Liye", "Ma, Yunsheng")
    add_Collaboration(driver, "Lv, Liye", "Lee, Ikjin")

    add_Collaboration(driver, "Song, Xueguan", "Ma, Yunsheng")
    add_Collaboration(driver, "Song, Xueguan", "Lee, Ikjin")

    add_Collaboration(driver, "Ma, Yunsheng", "Lee, Ikjin")

    create_Node(driver,"Eduardo Davila","M")
    #print_friends(driver, "Arthur")