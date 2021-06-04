import cv2
import numpy as np
import sqlite3
import os

def insertOrupdateDB(id, name):
	conn =  sqlite3.connect("data.db")
	''' viết câu lệnh ktra xem id khi chúng ta nhập vào thì nó đã tồn tại hay chưa.
		- nếu tồn tại rồi thì mình sẽ update.
		- ngược lại thì sẽ insert.
	'''
	query = "SELECT * FROM people WHERE ID ="+ str(id)
	cusror = conn.execute(query)
	
	isID = 0
	for i in cusror:
		isID = 1
	if(isID == 0):
		query = "INSERT INTO people(ID, Name) values ("+str(id)+ ",'"+str(name)+"')"
	else:
		query = "UPDATE people SET Name='"+str(name)+"' WHERE ID= "+str(id)

	conn.execute(query)
	conn.commit()
	conn.close()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

id = input("mời bạn nhập vào id của bạn: ")
name =input("mời bạn nhập tên của bạn vào: ")

insertOrupdateDB(id, name)

index=0

while(True):
	ret , frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

		if(not os.path.exists('dataSetimg')):
			os.makedirs('dataSetimg')
		index = index + 1
		cv2.imwrite('dataSetimg/img.'+str(id)+'.'+str(index)+'.jpg',gray[y: y+h,x: x+w])
	cv2.imshow("HienAnh",frame)
	cv2.waitKey(1)
	if(index >5):
		break

cap.release()
cv2.destroyAllWindows()	
