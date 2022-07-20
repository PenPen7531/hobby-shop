import json
from models.toy import Toy
class Collection:
    def __init__(self, collection_name):
        if type(collection_name) != str:
            raise TypeError
        self.name =  collection_name
        self.collection = []
        try:
            with open(f"data/{self.name}.json") as file:
                self.collection = [
                    Toy(
                        toy["name"], 
                        toy["price"],
                        toy["description"],
                        toy["link"],
                        toy["review"]
                    ) for toy in json.load(file)
                ]
        except:
            self.employees = []


    def find_item_by_id(self, item_name):
        for item in self.collection:
            if item_name == item.name:
                return item
        return None

    def find_items_by_id(self, search_name):
        items=[]
        for item in self.collection:
            if search_name.lower() in item.name.lower():
                items.append(item)
        return items