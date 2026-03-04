def test_get_activities(client):
    # Arrange: fixture provides `client` and reset state

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # Spot check a known activity
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"].get("participants"), list)
