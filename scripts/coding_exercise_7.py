class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        newStore = cls(store.name + ' - franchise')
        newStore.items = store.items
        return newStore

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        # The line below only works on Python 3.6+
        return f'{store.name}, total stock price: {store.stock_price()}'


if __name__ == '__main__':
    store = Store('X items')
    print(f'Store before franchising: {store}')
    store = Store.franchise(store)
    print(f'Store after franchising: {store}')

    print(Store.store_details(store))
