from rest_api.main.models.item import ItemModel
from rest_api.main.models.store import StoreModel
from rest_api.tests.test_base import TestBase


class ItemTest(TestBase):
    def test_canary(self):
        self.assertTrue(True)

    def test_crud(self):
        with self.app_context():
            StoreModel('store one').save_to_db()
            item = ItemModel('test', 30.25, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              f'Found an item with name {item.name} but expected none.')

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 f'Item "{item.name}" was not inserted on database.')

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'),
                              f'Item "{item.name}" not deleted from database.')

    def test_create_item(self):
        with self.app_context():
            StoreModel('store one').save_to_db()
            item = ItemModel('item name', 25.99, 1)

            self.assertEqual('item name', item.name)
            self.assertEqual(25.99, item.price)

    def test_item_to_json(self):
        with self.app_context():
            StoreModel('store one').save_to_db()
            item = ItemModel('item name', 25.99, 1)
            expected = {'name': 'item name', 'price': 25.99}

            self.assertDictEqual(expected, item.json())
