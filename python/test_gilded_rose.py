# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # Normal Items
    def test_normal_item_quality_and_sellin_decrease(self):
        items = [Item("Normal Item", 5, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_normal_item_quality_degrades_twice_after_expiry(self):
        items = [Item("Normal Item", 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    # Aged Brie
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_quality_doubles_after_expiry(self):
        items = [Item("Aged Brie", 0, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(2, items[0].quality)

    # Backstage Passes
    def test_backstage_pass_increase_by_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_pass_increase_by_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_pass_increase_by_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_pass_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(0, items[0].quality)

    # Sulfuras
    def test_sulfuras_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    # Conjured Items
    def test_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_conjured_item_degrades_four_after_expiry(self):
        items = [Item("Conjured Elixir", 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_conjured_item_quality_does_not_go_negative(self):
        items = [Item("Conjured Bread", 0, 3)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
