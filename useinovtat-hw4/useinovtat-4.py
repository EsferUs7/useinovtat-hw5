from math import ceil


class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return ceil(self.item_count() / self.items_per_page)

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        for i in range(self.page_count()):
            if i == page_index:
                if (i + 1) == self.page_count() and self.item_count() % self.items_per_page != 0:
                    return self.item_count() % self.items_per_page
                return self.items_per_page
        return -1

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        for i in range(self.item_count()):
            if i == item_index:
                return i // self.items_per_page
        return -1
