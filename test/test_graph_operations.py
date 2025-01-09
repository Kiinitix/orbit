import unittest
from services.neo4j_service import Neo4jService

class TestNeo4jOperations(unittest.TestCase):
    def setUp(self):
        self.db = Neo4jService(uri="bolt://localhost:7687", user="neo4j", password="test_password")

    def tearDown(self):
        self.db.close()

    def test_add_project(self):
        result = self.db.add_project("Test Project", "2025-01-01", "2025-12-31")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
