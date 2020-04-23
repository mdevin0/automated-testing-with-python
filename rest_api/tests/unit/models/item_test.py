from unittest import TestCase

from rest_api.main.models.item import ItemModel


class ModelTest(TestCase):
    def test_canary(self):
        self.assertTrue(True)


    def test_create_item(self):
        item = ItemModel('item name', 25.99)

        self.assertEqual('item name', item.name)
        self.assertEqual(25.99, item.price)


    def test_item_to_json(self):
        item = ItemModel('item name', 25.99)
        expected = {'name': 'item name', 'price': 25.99}

        self.assertDictEqual(expected, item.json())