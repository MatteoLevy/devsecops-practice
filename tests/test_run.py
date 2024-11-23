from app.run import app


def test_home():
    # Test the home route
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
