
def test_login(client):
    response = client.post(
        '/login',
        json={
            "username": "usertest",
            "password": "123456789"
        },
        headers={
            'Content-type': 'application/json',
            'Accept': 'application/json'
        },
    )
    assert response.status_code == 401


def test_avm_create(client):
    response = client.post(
        '/avm/create',
        json={
            "address": "Carrer de Pau Alsina 10, Principal A",
            "latitude": 41.410610,
            "longitude": 2.161880,
            "zipcode": "08025",
            "city": "Barcelona",
            "year_of_construction": 1900,
            "year_of_renovation": 2020,
            "total_price": 450000,
            "total_area": 83,
            "price_m2": 5421,
            "has_elevator": "Y",
            "valuation_date": "10/09/2021"
        },
    )
    assert response.status_code == 401
