import cv2
import pytesseract
import os
from url_parser import download_imagesFromUrl

pytesseract.pytesseract.tesseract_cmd = 'tesseract'



def recognize_text(img,img_name):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	blur = cv2.GaussianBlur(gray, (3,3), 0)
	thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

	dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)

	contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
													cv2.CHAIN_APPROX_NONE)

	im2 = img.copy()


	for cnt in contours:
		x, y, w, h = cv2.boundingRect(cnt)
		
		rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cropped = im2[y:y + h, x:x + w]


		file = open("recognized.txt", "a")
		text = pytesseract.image_to_string(cropped)

		file.write(text)
		
		file.close



dirImg = "download_img"

download_imagesFromUrl()

file = open("recognized.txt", "w+")
file.write("")
file.close()

print("Записываем в файл")
for img in os.listdir(dirImg):

	cv2Img = cv2.imread(f"{dirImg}/{img}")

	recognize_text(cv2Img,img)


print("Все!")