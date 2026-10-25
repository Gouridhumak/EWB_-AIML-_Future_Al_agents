from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crud_workflow():
    root_res = client.get("/")
    assert root_res.status_code == 200

    student_payload = {
        "name": "Alex Smith",
        "dob": "2004-03-15",
        "email": "alex.smith@example.com",
        "phone": "9876543210",
        "course": "Computer Science"
    }
    create_res = client.post("/students", json=student_payload)
    assert create_res.status_code == 201
    created_data = create_res.json()
    student_id = created_data["id"]
    assert created_data["name"] == "Alex Smith"

    get_all_res = client.get("/students")
    assert get_all_res.status_code == 200
    assert len(get_all_res.json()) > 0

    get_one_res = client.get(f"/students/{student_id}")
    assert get_one_res.status_code == 200
    assert get_one_res.json()["email"] == "alex.smith@example.com"

    update_payload = {"course": "Data Analytics"}
    put_res = client.put(f"/students/{student_id}", json=update_payload)
    assert put_res.status_code == 200
    assert put_res.json()["course"] == "Data Analytics"

    del_res = client.delete(f"/students/{student_id}")
    assert del_res.status_code == 200

    verify_res = client.get(f"/students/{student_id}")
    assert verify_res.status_code == 404