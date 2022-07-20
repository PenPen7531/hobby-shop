from unittest.util import strclass


class Toy:
    def __init__(self, item_name, item_price, item_description, item_img_lnk, item_review):
        if type(item_name) != str:
            raise TypeError
        self.name=item_name
        if type(item_img_lnk) != str:
            raise TypeError
        self.link = item_img_lnk
        if type(item_price) != str:
            raise TypeError
        self.price = item_price
        if type(item_description) != str:
            raise TypeError
        self.description = item_description
        if type(item_review) != str:
            raise TypeError
        self.review = item_review

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "link": self.link,
            "review": self.review
        }
        

        