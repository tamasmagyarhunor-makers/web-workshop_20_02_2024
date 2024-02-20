from lib.item import Item

class ItemRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM items")
        items = []
        for row in rows:
            item = Item(row['id'], row['name'], row['type'])
            items.append(item)
        return items