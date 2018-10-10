
def copy_file(infile_name, outfile_name):
	infile = open(infile_name, "r")
	outfile = open(outfile_name, "w")
	while True:
		text = infile.readline()
		if text == "":
			break
		elif text.startswith("#"):
			continue
		else:
			outfile.write(text)
	infile.close()
	outfile.close()

if __name__ == '__main__':
	copy_file("input.txt", "output.txt")