import json

email = "test@example.com"
password = "testing1*"

def test_remove_coin_to_tracker_success(client):    
    data = {"email":email, "password":password}
    response = client.post("/signin/",data=json.dumps(data))
    token = response.json()["data"]["token"]

    headers = {
        "Authorization" : f"Bearer {token}"
    }

    coin = "bitcoin"
    response = client.delete(f"/tracker/{coin}", headers=headers)

    assert response.status_code == 200 
    assert response.json()["code"] == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"] == f"{coin} success deleted"

def test_add_coin_to_tracker_failed_not_found_coin(client):    
    data = {"email":email, "password":password}
    response = client.post("/signin/",data=json.dumps(data))
    token = response.json()["data"]["token"]

    headers = {
        "Authorization" : f"Bearer {token}"
    }

    coin = "logam"
    response = client.delete(f"/tracker/{coin}", headers=headers)

    assert response.status_code == 404 
    assert response.json()["code"] == 404
    assert response.json()["status"] == "failed"
    assert response.json()["message"] == f"{coin} not found"

def test_add_coin_to_tracker_failed_unauthenticated(client):    
    coin = "logam"
    response = client.delete(f"/tracker/{coin}")

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"