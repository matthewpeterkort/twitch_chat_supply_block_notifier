import pytesseract
import cv2
import pygetwindow
import pyautogui
import numpy as np
import time
import socket
import re
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


while(1):
	imagenumber=0
	img = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
	cv2.imwrite("in_memory_to_disk_supply"+str(imagenumber)+".png", image)
	image = cv2.imread("in_memory_to_disk_supply"+str(imagenumber)+".png")


	crop_img_two = image[140:160, 1505:1580]
	gray_two = cv2.cvtColor(crop_img_two, cv2.COLOR_BGR2GRAY)
	retOne,thresh2 = cv2.threshold(gray_two,180,255,cv2.THRESH_BINARY)
	resized_two = cv2.resize(thresh2, (300,100), interpolation = cv2.INTER_LINEAR)

	Left_Num= pytesseract.image_to_string(resized_two,config='config="-c tessedit_char_whitelist=0123456789/"')

	new_Left_Num=""
	for m in Left_Num:
		if m.isdigit() or m == '/':
			new_Left_Num = new_Left_Num + m


	if('/'  in new_Left_Num):
		new_Left_Num=new_Left_Num.split('/')
		if(len(new_Left_Num[0])>0 and len(new_Left_Num[1])>0):
			print(new_Left_Num[0],new_Left_Num[1])
			if(new_Left_Num[0].isdigit() and new_Left_Num[1].isdigit() and int(new_Left_Num[1]) != 0):
				if(int(new_Left_Num[0])/int(new_Left_Num[1])==1 and (int(new_Left_Num[0]) != 200 
				and int(new_Left_Num[1]) != 200) and (int(new_Left_Num[0]) != 15 and int(new_Left_Num[1]) != 15) and 
				(int(new_Left_Num[0]) > 9 and int(new_Left_Num[1]) > 9)):
					print("supply block")
					replace_line('supply_block.txt', 0,  'Congratulations! streamer is supply blocked at '+ 
					str(new_Left_Num[0]) + '/' + str(new_Left_Num[1]))
					time.sleep(30)


	#cv2.imshow("Test_img.jpg",resized_two)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	

	
	



