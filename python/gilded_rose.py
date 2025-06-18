
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if self.is_aged_brie(item):
                self._update_aged_brie(item)
            elif self.is_backstage_pass(item):
                self._update_backstage_pass(item)
            elif self.is_sulfuras(item):
                self._update_sulfuras(item)
            elif self.is_conjured(item):
                self._update_conjured_item(item)
            else:
                self._update_normal_item(item)


# Item-Type Update Methods

def _update_aged_brie(self, item):
    self.increase_quality(item)
    item.sell_in -= 1
    if item.sell_in < 0:
        self.increase_quality(item)


def _update_backstage_pass(self, item):
    self.increase_quality(item)
    if item.sell_in < 11:
        self.increase_quality(item)
    if item.sell_in < 6:
        self.increase_quality(item)
    item.sell_in -= 1
    if item.sell_in < 0:
        item.quality = 0


def _update_sulfuras(self, item):
    pass  # Legendary item, do nothing


def _update_normal_item(self, item):
    self.decrease_quality(item)
    item.sell_in -= 1
    if item.sell_in < 0:
        self.decrease_quality(item)


def _update_conjured_item(self, item):
    self.decrease_quality(item, 2)
    item.sell_in -= 1
    if item.sell_in < 0:
        self.decrease_quality(item, 2)


# Helper Methods
def is_aged_brie(self, item):
    return item.name == "Aged Brie"


def is_backstage_pass(self, item):
    return item.name == "Backstage passes to a TAFKAL80ETC concert"


def is_sulfuras(self, item):
    return item.name == "Sulfuras, Hand of Ragnaros"


def decrease_quality(self, item, amount=1):
    item.quality = max(0, item.quality - amount)


def increase_quality(self, item, amount=1):
    item.quality = min(50, item.quality + amount)


def is_conjured(self, item):
    return item.name.lower().startswith("conjured")
