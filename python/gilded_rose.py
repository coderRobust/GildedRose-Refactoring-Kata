from typing import List


class Item:
    """Represents a single inventory item."""

    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


# Base Updater and Utilities functionality
class ItemUpdater:
    """Base class for item update strategies."""

    def update(self, item):
        raise NotImplementedError(
            "Subclasses must implement the update method.")

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)


class AgedBrieUpdater(ItemUpdater):
    """Aged Brie increases in quality as it ages."""

    def update(self, item):
        self.increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.increase_quality(item)


class BackstagePassUpdater(ItemUpdater):
    """Backstage passes increase in quality as concert approaches, then drop to 0."""

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
    """Sulfuras never changes in quality or sell_in."""

    def update(self, item):
        pass


class NormalItemUpdater(ItemUpdater):
    """Normal items degrade in quality over time."""

    def update(self, item):
        self.decrease_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item)


class ConjuredItemUpdater(ItemUpdater):
    """Conjured items degrade in quality twice as fast."""

    def update(self, item):
        self.decrease_quality(item, 2)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item, 2)


# Factory class

class ItemUpdaterFactory:

    """Factory to get appropriate updater for each item."""

    def get_updater(self, item):
        name = item.name.lower()
        if name == "aged brie":
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
    """Main class that updates all items in the store."""

    def __init__(self, items):
        self.items = items
        self.factory = ItemUpdaterFactory()

    def update_quality(self):
        for item in self.items:
            updater = self.factory.get_updater(item)
            updater.update(item)
