#Author: Curtis Turner
#Course: CPSC 353 Intro to Computer Security
#Project 1
#Hide and Extract Text in Images

from PIL import Image
from math import floor

def cleanBits(byte):
    byte = byte[2:]
    while len(byte) < 8:
        byte = '0' + byte
    return byte

def firstEleven(data):
	while len(data) < 32:
		data = '0' + data
	return data

def setBits(byte, bit):
	if bit == '0':
		newByte = byte[:-1] + '0'
		return newByte
	elif bit == '1':
		newByte = byte[:-1] + '1'
		return newByte

def messageToBin(message):
	binaryMessage = ''
	for i in message:
		binaryMessage += cleanBits(bin(ord(i)))
	return binaryMessage

def decode(file):
	message = ''
	length = ''
	image = Image.open(file)
	size = image.size
	width = size[0] - 1
	height = size[1] - 1
	pic = image.load()
	for i in range(11):
		pixelValues = pic[width, height]
		binR = bin(pixelValues[0])
		binG = bin(pixelValues[1])
		binB = bin(pixelValues[2])

		length = length + binR[-1] + binG[-1] + binB[-1]
		width = width - 1
	length = length[:-1]
	#print(length)
	length = int(length, 2)
	#print(length)

	while len(message) < length:	
		pixelValues = pic[width, height]
		binR = bin(pixelValues[0])
		binG = bin(pixelValues[1])
		binB = bin(pixelValues[2])

		message = message + binR[-1]
		message = message + binG[-1]
		message = message + binB[-1]
		width -= 1
		if width == 0:
			height -= 1
			width = size[0] - 1
	n = 8
	message = [message[i:i+n] for i in range(0, len(message), n)]
	newMessage = ''
	for i in message:
		newMessage = newMessage + str(chr(int(i, 2)))
	return newMessage

def encode(file, message):
	binMessage = messageToBin(message)
	length = firstEleven(cleanBits(bin(len(binMessage))))
	extraPixel = ''

	if len(binMessage)%3 == 0:
		pixelCount = len(binMessage)/3
	elif len(binMessage)%3 == 1:
		pixelCount = floor(len(binMessage)/3)
		extraPixel = 'r'
	elif len(binMessage)% 3 == 2:
		pixelCount = floor(len(binMessage)/3)
		extraPixel = 'rg'

	image = Image.open(file)
	size = image.size
	width = size[0] - 1
	height = size[1] - 1
	pic = image.load()

	index = 0
	while index < 30:
		pixelValues = pic[width, height]
		binR = bin(pixelValues[0])
		binG = bin(pixelValues[1])
		binB = bin(pixelValues[2])

		binR = setBits(binR, length[index])
		newR = int(binR, 2)
		index += 1
		binG = setBits(binG, length[index])
		newG = int(binG, 2)
		index += 1
		binB =  setBits(binB, length[index])
		newB = int(binB, 2)
		index += 1
		pic[width, height] = (newR, newG, newB)
		width = width - 1

	pixelValues = pic[width, height]
	binR = bin(pixelValues[0])
	binG = bin(pixelValues[1])
	binB = bin(pixelValues[2])

	binR = setBits(binR, length[index])
	newR = int(binR, 2)
	index += 1
	binG = setBits(binG, length[index])
	newG = int(binG, 2)
	index += 1

	pic[width, height] = (newR, newG, pixelValues[2])
	width -= 1

	stop = 0
	count = 0
	while stop < pixelCount:
		pixelValues = pic[width, height]
		binR = bin(pixelValues[0])
		binG = bin(pixelValues[1])
		binB = bin(pixelValues[2])

		binR = setBits(binR, binMessage[count])
		newR = int(binR, 2)
		count += 1
		binG = setBits(binG, binMessage[count])
		newG = int(binG, 2)
		count += 1
		binB = setBits(binB, binMessage[count])
		newB = int(binB, 2)
		count += 1
		pic[width, height] = (newR, newG, newB)
		stop += 1
		width -= 1
		if width == 0:
			height -= 1
			width = size[0] - 1
	if extraPixel == 'r':
		pixelValues = pic[width, height]
		binR = bin(pixelValues[0])
		binG = pixelValues[1]
		binB = pixelValues[2]
		binR = setBits(binR, binMessage[count])
		count += 1
		newR = int(binR, 2)
		pic[width, height] = (newR, binG, binB)
	elif extraPixel == 'rg':
		pixelValues = pic[width, height]
		binR = bin(pixelValues[0])
		binG = bin(pixelValues[1])
		binB = pixelValues[2]

		binR = setBits(binR, binMessage[count])
		count += 1
		newR = int(binR, 2)
		binG = bin(pixelValues[1])
		binG = setBits(binG, binMessage[count])
		count += 1
		newG = int(binG, 2)
		pic[width, height] = (newR, newG, binB)
	image.save(file[:-3] + 'png')

def main():
	print('Do you want to encode or deocde data?')
	choice = input("enter 'e' to encode or 'd' to decode >>")
	if choice == 'e':
		print('encoding')
		filename = input('enter the filename to hide your message in >> ')
		msg = input('enter the message you would like to hide or hit enter to run a file >> ')
		if msg == '':
			textFile = input('enter the file you wish to encode >> ')
			openfile = open(textFile, 'r')
			msg = openfile.read()
		encode(filename, msg)
	elif choice == 'd':
		print('decoding')
		filename = input('enter the filename you wish to extract the message from >> ')
		msg = decode(filename)
		print('the hidden message is: ' + msg)
	else:
		print('incorrect choice refer to the README for correct usage')

if __name__ == '__main__':
	main()