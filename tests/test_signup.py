def test_signup_for_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "pytest_student@example.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "Signed up" in body.get("message", "")

    # Verify participant was added (act + assert)
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]
