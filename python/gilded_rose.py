
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Base Updater and Utilities functionality
class ItemUpdater:

    def update(self, item):
        raise NotImplementedError

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        self.increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.increase_quality(item)


class BackstagePassUpdater(ItemUpdater):
    def update(self, item):
        self.increase_quality(item)
        if item.sell_in < 11:
            self.increase_quality(item)
        if item.sell_in < 6:
            self.increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item)


class ConjuredItemUpdater(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 2)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item, 2)


# Helper Methods

# Factory class

class ItemUpdaterFactory:
    def get_updater(self, item):
        name = item.name.lower()
        if name == "Aged Brie":
            return AgedBrieUpdater()
        elif name.startswith("backstage passes"):
            return BackstagePassUpdater()
        elif name == "sulfuras, hand of ragnaros":
            return SulfurasUpdater()
        elif name.startswith("conjured"):
            return ConjuredItemUpdater()
        else:
            return NormalItemUpdater()


# -*- coding: utf-8 -*-

# Main GildeRose Class
class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.factory = ItemUpdaterFactory()

    def update_quality(self):
        for item in self.items:
            updater = self.factory.get_updater(item)
            updater.update(item)
