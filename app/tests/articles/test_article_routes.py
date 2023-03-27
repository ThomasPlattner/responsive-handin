def test_boats_success(client):
    # Page loads
    response = client.get('/blog/boats')
    assert response.status_code == 200

def test_bikes_success(client):
    # Page loads
    response = client.get('/blog/bikes')
    assert response.status_code == 200

def test_cars_success(client):
    # Page loads
    response = client.get('/blog/cars')
    assert response.status_code == 200

def test_planes_success(client):
    # Page loads
    response = client.get('/blog/planes')
    assert response.status_code == 200