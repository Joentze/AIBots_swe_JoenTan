"""pytest to test api outputs"""
# test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app
from schemas.Conversation import Conversation, ConversationFull


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


def test_get_all_conversations(test_client):
    """tests all conversaiotns GET request"""
    response = test_client.get("/conversations")
    # tests response code
    assert response.status_code == 200

    # test model of each conversation
    conversations = response.json()["data"]
    for convo in conversations:
        assert Conversation(**convo)


def test_post_new_conversation(test_client):
    """tests POST request to create new conversation"""
    test_post_data = {
        "name": "Test Conversation",
        "params": {},
        "tokens": 0
    }
    response = test_client.post("/conversations", json=test_post_data)
    print(response)
    assert response.status_code == 201
    # test response
    assert isinstance(response.json()["id"], str)
