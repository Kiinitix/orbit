from services.neo4j_service import Neo4jService

def load_graph_data(db: Neo4jService):
    query = """
    MATCH (n)-[r]->(m)
    RETURN n AS source, m AS target, r AS relationship
    """
    result = db.execute_query(query)
    graph_data = {
        "nodes": [],
        "edges": []
    }

    node_ids = set()
    for record in result:
        source = record["source"]
        target = record["target"]
        relationship = record["relationship"]

        if source.id not in node_ids:
            graph_data["nodes"].append({"id": source.id, "name": source["name"], "type": source.labels})
            node_ids.add(source.id)
        if target.id not in node_ids:
            graph_data["nodes"].append({"id": target.id, "name": target["name"], "type": target.labels})
            node_ids.add(target.id)

        graph_data["edges"].append({
            "source": source.id,
            "target": target.id,
            "type": relationship.type
        })

    return graph_data

def clear_graph(db: Neo4jService):
    query = "MATCH (n) DETACH DELETE n"
    db.execute_query(query)
    print("Graph cleared.")

if __name__ == "__main__":
    db = Neo4jService(uri="bolt://localhost:7687", user="neo4j", password="test_password")
    clear_graph(db)
    db.close()
