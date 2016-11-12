
import cv2
import argparse
import os
import numpy
import sys

#python version 2.7
#libray : opencv
#useage :
#put 2 paramater.inputpath and outputpath and set output_side_length.
##like this        
#python resize.py company_documents/ classed_opencv_text_detiction/

print "input img path is :", sys.argv[1]
print "output img path is :", sys.argv[2]


if len(sys.argv[1]) != 0 and len(sys.argv[2]) != 0:
  input_imgpath = sys.argv[1]
  files = os.listdir(str(input_imgpath))

  for file in files:

      if file.find('.jpg') == -1 and file.find('.png') == -1:
        continue

      print file
      img = cv2.imread(input_imgpath+file)
      height, width, depth = img.shape

      print str(height) + " " + str(width)
      
      output_side_length=590
      new_height = output_side_length
      new_width = output_side_length
      if height > width:
        new_height = output_side_length * height / width
      else:
        new_width = output_side_length * width / height
      resized_img = cv2.resize(img, (new_width, new_height))
      height_offset = (new_height - output_side_length) / 2
      width_offset = (new_width - output_side_length) / 2
      cropped_img = resized_img[height_offset:height_offset + output_side_length,
      width_offset:width_offset + output_side_length]

      print "imwreite done"
      cv2.imwrite(sys.argv[2]+"590_"+file, cropped_img)


else:
  print "please set argv[1] argv[2]"



# how about this resize algorizm
#
# src = cv2.imread("reni.jpg", 1)
# hight = src.shape[0]
# width = src.shape[1]
# half_img = cv2.resize(src,(hight/2,width/2))

