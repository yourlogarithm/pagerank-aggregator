import unittest

import src.main
from fastapi.testclient import TestClient


client = TestClient(src.main.app)


class TestMain(unittest.TestCase):
    def test_increment(self):
        assert src.main.counter == 0

        response = client.get("/increment")

        assert response.status_code == 200
        assert response.json() == {'calculate': False}

        for _ in range(src.main.threshold-1):
            response = client.get('/increment')

        assert response.status_code == 200
        assert response.json() == {'calculate': True}
        assert src.main.counter == 0
