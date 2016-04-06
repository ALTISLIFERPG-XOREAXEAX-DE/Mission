#!/usr/bin/env python

import sys
import glob
import os

import re

#
# main function
#
if __name__ == "__main__":
  _item_counter = 0
  _itemid_counter = int(sys.argv[2])

  with open(sys.argv[1], "r") as file_reader:
    regex = re.compile(r"id=[0-9]*;", re.IGNORECASE)
    rege2 = re.compile(r"class Item[0-9]*", re.IGNORECASE)

    for line in file_reader:
      if line.find("id=") > 0:
        line = regex.sub("id=%s;" % _itemid_counter, line)
        _itemid_counter = _itemid_counter + 1

      if line.find("class Item") > 0:
        line = rege2.sub("class Item%s" % _item_counter, line)
        _item_counter = _item_counter + 1

      print line

    print ("""

    items=%s;

""" % _item_counter)

