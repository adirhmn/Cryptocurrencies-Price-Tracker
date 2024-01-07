import json

email = "test@example.com"
password = "testing1*"

def test_show_tracked_coins_success(client):    
    data = {"email":email, "password":password}
    response = client.post("/signin/",data=json.dumps(data))
    token = response.json()["data"]["token"]

    headers = {
        "Authorization" : f"Bearer {token}"
    }

    response = client.get("/tracker/", headers=headers)

    assert response.status_code == 200 
    assert response.json()["code"] == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"] != None 

def test_show_tracked_coins_failed_token_expired(client):    
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aGVvQGdtYWlsLmNvbSIsImV4cCI6MTcwNDYyNzIxOX0.bx4YTjLgTEdoM6uHNQ3sA2BxccvOpsj903lAKWhICnx"

    headers = {
        "Authorization" : f"Bearer {token}"
    }

    response = client.get("/tracker/", headers=headers)

    assert response.status_code == 401 
    assert response.json()["code"] == 401
    assert response.json()["status"] == "failed"
    assert response.json()["message"] == "Signature has expired" 

def test_show_tracked_coins_failed_unauthenticated(client):    

    response = client.get("/tracker/")

    assert response.status_code == 401 
    assert response.json()["detail"] == "Not authenticated"