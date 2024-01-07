import json

email = "test@example.com"
password = "testing1*"

def test_signout_user_success(client):  
    data = {"email":email, "password":password}
    response = client.post("/signin/",data=json.dumps(data))
    token = response.json()["data"]["token"]

    headers = {
        "Authorization" : f"Bearer {token}"
    }  
    response = client.get("/signout/", headers=headers)

    assert response.status_code == 200 
    assert response.json()["code"] == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"] == f"{email} success signout"

def test_signin_user_failed_unauthenticated(client):    
    response = client.get("/signout/")

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"