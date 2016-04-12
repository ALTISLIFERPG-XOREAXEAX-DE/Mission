#!/usr/bin/env python

import sys
import os

import random

output_buffer = []

#
# main function
#
if __name__ == "__main__":
  with open(sys.argv[1], "r") as file_reader:
    for line in file_reader:
      #
      # Marihuana
      #
      buy_price = 10000
      sell_price = buy_price + random.randint(0, 10000)

      line = line.replace("%%%MARIJUANA_PROCESSED_BUYPRICE%%%", "%s" % buy_price)
      line = line.replace("%%%MARIJUANA_PROCESSED_SELLPRICE%%%", "%s" % sell_price)

      #
      # Cocaine
      #
      buy_price = 20000
      sell_price = buy_price + random.randint(0, 20000)
      line = line.replace("%%%COCAINE_PROCESSED_BUYPRICE%%%", "%s" % buy_price)
      line = line.replace("%%%COCAINE_PROCESSED_SELLPRICE%%%", "%s" % sell_price)

      #
      # Heroin
      #
      buy_price = 20000
      sell_price = buy_price + random.randint(0, 20000)
      line = line.replace("%%%HEROIN_PROCESSED_BUYPRICE%%%", "%s" % buy_price)
      line = line.replace("%%%HEROIN_PROCESSED_SELLPRICE%%%", "%s" % sell_price)

      output_buffer.append(line.replace("\r", "").replace("\n", ""))

  for line in output_buffer:
    print line

