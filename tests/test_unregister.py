def test_unregister_from_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "to_remove_student@example.edu"

    # Ensure the participant is present first
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup_resp.status_code == 200

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "Unregistered" in body.get("message", "")

    # Verify removal
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]
