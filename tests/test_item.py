from lib.item import *
"""
Given a Item is instantiated
It has an id, name and type
"""
def test_item_instantiates_with_id_name_type():

    item = Item(1, "Phone", "electric")
    assert item.id == 1
    assert item.name == "Phone"
    assert item.type == "electric"

"""
Given two Items have identical parameters
They are equal
"""
def  test_two_item_objects_with_identical_properties_are_equal():
    item1 = Item(1, "Tennis shorts", "sportswear")
    item2 = Item(1, "Tennis shorts", "sportswear")

    assert item1 == item2

"""
Given I print out an Item
It prints in a nice format

"""
def test_item_instance_prints_in_nice_format():
    item = Item(1, "Bike", "sports equipment")
    assert str(item) == "Item(1, Bike, sports equipment)"