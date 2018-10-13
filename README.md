# ABS

    ABS project was created with the intention of detecting blurred and/or flared images.
    
    This proyect const of 4 files, 2 for blurred images detection and 2 for flared images detection:
    
      - blurry-or-no.py and flared-or-not.py 
      Takes an image and analize it to determine if it's blurred or flared respectively.
      
      - blurrytest.py and flaredtest.py 
      Takes all images in a given directory and analyze them using a windown as a interface to
      show the image and result of the analysis. It's more convenient for analysing a bunch of images without invokint the comand
      for every single image.
    
    
 Getting started
 
 To run and test this commands you can use the python console or run them directly in your Ubuntu command line interface (if
 you already have installed python in your linux machine).
  - 
 
Requisites

This python scripts are made with the following configuration system:

  - Ubuntu 16.04.5 LTS
  - Python 2.7.12
  - OpenCV 2.4.9.1

Once you get your installation done (check this howto if you ineed to install it
https://docs.opencv.org/3.4.1/d2/de6/tutorial_py_setup_in_ubuntu.html ) you are ready to run this programs.
Here are some examples.
  
  - To run blurry-or-not.py just type:
    ./flared-or-not.py -i /path_to_your_data/image.jpg -t 700

    - To run flared-or-not.py just type:
    ./flared-or-not.py -i /path_to_your_data/image.jpg -t 72

  - To run blurrytest.py just type:
    ./blurrytest.py -i /path_to_your_data//directory_containing_images -t 700
  
  - To run flaredtest.py just type:
   ./flaredtest.py -i /path_to_your_data/directory_containing_images -t 72
   
