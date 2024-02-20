import os
from flask import Flask, request
from lib.item_repository import ItemRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/items', methods=['GET'])
def get_items():
    connection = get_flask_database_connection(app)
    repository = ItemRepository(connection)
    list_of_items = repository.all()
    list_of_str_items = []
    for item in list_of_items:
        list_of_str_items.append(str(item))
    return " ".join(list_of_str_items)
# == Example Code Below ==

@app.route('/e', methods=['GET'])
def get_index_home():
    return {
        'success': True,
        'data': {
            'some_property': 'some value',
            'some_other_property': 13,
            'amazing': True
        }
    }

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

