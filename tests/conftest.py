from fastapi.testclient import TestClient
import copy
import pytest
from src import app as app_module

# Keep an immutable snapshot of the initial activities state so tests can reset global state
_original_activities = copy.deepcopy(app_module.activities)

@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory `activities` dict before each test (arrange).
    This ensures tests are isolated and can run in any order."""
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_original_activities))
    yield


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app (act)."""
    return TestClient(app_module.app)
