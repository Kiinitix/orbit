import json
import csv
from services.neo4j_service import Neo4jService

def load_from_json(file_path, db: Neo4jService):
    with open(file_path, 'r') as f:
        data = json.load(f)

    for project in data.get("projects", []):
        db.add_project(project["name"], project["start_date"], project["end_date"])
        for dependency in project.get("dependencies", []):
            db.add_dependency(project["name"], dependency)

    for resource in data.get("resources", []):
        db.add_resource(resource["name"], resource["capacity"])

def load_from_csv(file_path, db: Neo4jService):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            db.add_project(row["name"], row["start_date"], row["end_date"])

if __name__ == "__main__":
    db = Neo4jService(uri="bolt://localhost:7687", user="neo4j", password="test_password")
    load_from_json("data/projects.json", db)
    load_from_csv("data/resources.csv", db)
    db.close()
