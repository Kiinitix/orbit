from modus.models import ModusModel
from modus.data import GraphData

class DependencyAnalyzer(ModusModel):
    def predict(self, data: GraphData):
        bottlenecks = []
        for node in data.nodes:
            if node["type"] == "Resource" and node["usage"] > node["capacity"]:
                bottlenecks.append(node)
        return {"bottlenecks": bottlenecks}
