#!/usr/bin/env python

import sys

import os.path

output_buffer = []

#
# main function
#
if __name__ == "__main__":
  template_directory = sys.argv[1]
  output_file = sys.argv[2]

  print "using template directory: %s" % template_directory

  with open("%s/mission.skel.sqm" % template_directory, "r") as mission_sqm:
    for line in mission_sqm.readlines():
      if not line.find("###") >= 0:
        output_buffer.append(line.replace("\n", "").replace("\r", ""))
      else:
        insert_template = "%s/%s" % (template_directory, line.replace("###", "").replace(" ", "").replace("\t", "").replace("\r", "").replace("\n", ""))

        print "trying to insert template into file: %s" % insert_template

        if not os.path.isfile(insert_template):
          print "FILE NOT FOUND: %s" % insert_template
          sys.exit(1)

        with open(insert_template, "r") as template_content:
          for tline in template_content.readlines():
            output_buffer.append(tline.replace("\n", "").replace("\r", ""))

        print "OK"

  with open(sys.argv[2], "w") as output_file:
    output_file.write("\n".join(output_buffer))

