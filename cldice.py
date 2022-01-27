import random
import sys
import os
if os.path.isfile("cldice.txt"):
	output = open("cldice.txt", "w")
else:
	output = open("cldice.txt", "x")
output.write(str(random.randint(int(sys.argv[1]), int(sys.argv[2]))))
output.close()
