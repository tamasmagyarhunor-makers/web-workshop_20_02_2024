from lib.item import *
from lib.item_repository import *

def test_item_repository_all_returns_all_items(db_connection):
    """
    Given I call Itemrepository#all() function
    I get back a list[] of Item objects
    """
    db_connection.seed("seeds/item_seed.sql")
    item_repository = ItemRepository(db_connection)
    actual = item_repository.all()
    expected = [
        Item(1, "Tennis racquet", "sports equipment"),
        Item(2, "iPhone", "electric")
    ]

    assert actual == expected