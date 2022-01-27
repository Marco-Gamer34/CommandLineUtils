import random, string

def random_alphanum(noch):
	return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(noch))

if os.path.isfile("pwdgen.txt"):
	file = open("pwdgen.txt", "w")
else:
	file = open("pwdgen.txt", "x")
file.write(
	random_alphanum(10)
	)
file.close()