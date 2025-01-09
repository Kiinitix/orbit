from neo4j import GraphDatabase

class Neo4jService:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters)

    def add_project(self, name, start_date, end_date):
        query = """
        CREATE (p:Project {name: $name, start_date: $start_date, end_date: $end_date})
        RETURN p
        """
        return self.execute_query(query, {"name": name, "start_date": start_date, "end_date": end_date})
   
    def calculate_critical_path(self):
        query = """
        MATCH (start:Project)-[r*]->(end:Project)
        WHERE NOT (start)<-[:DEPENDENCY]-()
        AND NOT (end)-[:DEPENDENCY]->()
        WITH start, end, REDUCE(total_duration = 0, rel IN r | total_duration + rel.duration) AS path_duration
        ORDER BY path_duration DESC
        RETURN start.name AS start_project, end.name AS end_project, path_duration
        LIMIT 1
        """
        result = self.execute_query(query)
        return [{"start_project": record["start_project"], "end_project": record["end_project"], "path_duration": record["path_duration"]} for record in result]
