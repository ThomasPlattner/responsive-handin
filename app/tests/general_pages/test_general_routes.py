def test_index_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_about_success(client):
    # Page loads
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_success(client):
    # Page loads
    response = client.get('/contact')
    assert response.status_code == 200

def test_categories_success(client):
    # Page loads
    response = client.get('/categories')
    assert response.status_code == 200