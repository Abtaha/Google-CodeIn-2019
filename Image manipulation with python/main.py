import cv2
import os


def decreaseSize(PATH):
	for img in os.listdir(PATH):
		image = cv2.imread(PATH + '/' + img)

		x = image.shape[1]
		y = image.shape[0]

		if x >= y:
			newY = int((y * 400) / x)
			newX = 400
			image = cv2.resize(image, (newX, newY))
			
			os.remove(PATH + '/' + img)
			cv2.imwrite(PATH + '/' + img, image, [int(cv2.IMWRITE_JPEG_QUALITY), 80])

		elif x < y:
			newX = int((x * 400) / y)
			newY = 400
			image = cv2.resize(image, (newX, newY))
			
			os.remove(PATH + '/' + img)
			cv2.imwrite(PATH + '/' + img, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])


if __name__ == "__main__":
	try:
		path = input("Enter the entire path to the images folder >> ")
		decreaseSize(path)
	except:
		print("Error")