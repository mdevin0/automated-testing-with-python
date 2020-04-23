from rest_api.main.models.item import ItemModel
from rest_api.tests.test_base import TestBase

class ItemTest(TestBase):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 30.25)

            self.assertIsNone(ItemModel.find_by_name('test'), 
                f'Found an item with name {item.name} but expected none.')

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'), 
                f'Item "{item.name}" was not inserted on database.')

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'), 
                f'Item "{item.name}" not deleted from database.')