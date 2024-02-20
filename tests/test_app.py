import json
# Tests for your routes go here

# === Example Code Below ===

"""
GET /items
"""
def test_get_items(web_client):
    response = web_client.get('/items')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Item(1, Tennis racquet, sports equipment) Item(2, iPhone, electric)"

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

"""
GET /
"""
def xtest_index_home_page(web_client):
    response = web_client.get("/")
    expected = {
        'success': True,
        'data': {
            'some_property': 'some value',
            'some_other_property': 13,
            'amazing': True
        }
    }

    actual = json.loads(response.data)
    assert actual == expected

"""
POST /books
"""
def test_adds_new_book_from_post_request(web_client):
    response = web_client.post('/books', data={
        'title': 'Life is amazing',
        'author_name': 'Hunor'
    })

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book added successfully"

# === End Example Code ===
