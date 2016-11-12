# opencv3_textdetection

* how to resize image
python version 2.7
libray : opencv
useage :
put 2 paramater.inputpath and outputpath and set output_side_length.
like this        
python resize.py company_documents/ classed_opencv_text_detiction/

* how to build 
g++ `pkg-config --libs opencv` `pkg-config --cflags opencv` textdetection_loop.cpp -o textdetection_loop

how to use
./textdetection_loop classed_opencv_text_detiction/

* how to build 
g++ `pkg-config --libs opencv` `pkg-config --cflags opencv` textdetection_show.cpp -o textdetection_show

how to use
./textdetection_show company_documents/b.jpg

