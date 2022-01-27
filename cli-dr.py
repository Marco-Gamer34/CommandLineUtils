import cv2
import sys
import os
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread(str(sys.argv[1])))
if os.path.isfile("cli-dr.txt"):
	output = open("cli-dr.txt", "w")
else:
	output = open("cli-dr.txt", "x")
output.write(val)
output.close()