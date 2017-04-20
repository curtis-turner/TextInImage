Author: Curtis Turner

Course: CPSC-353 Intro to Computer Security

Professor: Reza

Description:

This program is a practice in steganography, which is the idea of hiding data within data. 

Design:

The main design of this program is to go through the pixels from the bottom right corner and examine them individually and then manipulate the least significant bit in-order to hide our data inside the image. We save the image to a PNG format in order to avoid data loss. 

The program two major functions Encode and Decode. The functions take in an image and then the encode function will embed either a message or a file into the image. The decode functions does the opposite and serves as a method for extracting data from images.

How To Run The Program:
1. Open a terminal window.
2. Navigate to the location containing the .py file and the image you are going to encode or decode.
3. At the terminal prompt enter python3 TextInImage.py for instance:
blah@blah Downloads $ python3 TextInImage.py

4. The program will the prompt you to enter 'e' or 'd' without quotes to commence encoding or decoding.
5. If you choose to encode the program will prompt you to enter a filename. The file name MUST be a JPG format.
6. If you choose encode you will then need to enter a message to encode or you have the option to hit ENTER and then give the program a file name to encode.
7. After the encoding process is done you should see a file with the same name as the one you supplied with the file extension changed to .png

8. If you choose to decode you will only need to give a filename which must be a PNG format.
9. The program will then extract and display the text that is hidden in the file.
10. The program will the run and should shortly finish.
