import json

email = "test@example.com"
password = "testing1*"

def test_signup_user_success(client):    
    data = {"email":email, "password":password, "password_confirm":password}
    response = client.post("/signup/",data=json.dumps(data))

    assert response.status_code == 200 
    assert response.json()["code"] == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"] == {"email":email}

def test_signup_user_failed(client):    
    data = {"email":email, "password":password, "password_confirm":"password"}
    response = client.post("/signup/",data=json.dumps(data))

    assert response.status_code == 400 
    assert response.json()["code"] == 400
    assert response.json()["status"] == "failed"
    assert response.json()["message"] == "Email already registered"

