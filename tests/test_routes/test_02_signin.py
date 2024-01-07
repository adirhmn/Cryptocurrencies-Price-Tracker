import json

email = "test@example.com"
password = "testing1*"

def test_signin_user_success(client):    
    data = {"email":email, "password":password}
    response = client.post("/signin/",data=json.dumps(data))

    assert response.status_code == 200 
    assert response.json()["code"] == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"]["email"] == email
    assert response.json()["data"]["token"] != None

def test_signin_user_failed_not_found(client):    
    data = {"email":"fail@example.com", "password":password}
    response = client.post("/signin/",data=json.dumps(data))

    assert response.status_code == 404 
    assert response.json()["code"] == 404
    assert response.json()["status"] == "failed"
    assert response.json()["message"] == "User not found"