from services.neo4j_service import Neo4jService
from models.dependency_analyzer import DependencyAnalyzer
from utils.graph_helpers import load_graph_data
from utils.visualization import visualize_graph
from services.notification_service import send_alert_email
from config.settings import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

def main():
    db = Neo4jService(uri=NEO4J_URI, user=NEO4J_USER, password=NEO4J_PASSWORD)
    analyzer = DependencyAnalyzer()

    graph_data = load_graph_data(db)

    results = analyzer.predict(graph_data)
    if results["bottlenecks"]:
        alert_message = "Critical bottlenecks detected:\n"
        for bottleneck in results["bottlenecks"]:
            alert_message += f"Resource: {bottleneck['name']}, Usage: {bottleneck['usage']}\n"
        send_alert_email("Project Dependency Alert", alert_message)

    critical_path = db.calculate_critical_path()
    if critical_path:
        print("Critical Path Analysis:")
        for path in critical_path:
            print(f"Start: {path['start_project']}, End: {path['end_project']}, Duration: {path['path_duration']} days")

    visualize_graph(graph_data)

    db.close()

if __name__ == "__main__":
    main()
