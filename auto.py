def replace_char_in_txt(file, char1, char2):
	try:
		file = open(f"{file}", "r+")
		lines = [l.replace(char1, char2) for l in file.readlines()]
		file.seek(0)
		file.truncate()
		file.writelines(lines)

	except FileNotFoundError:
		file = open(f"{file}", "w")
		file.write(f"File didn't exist.\n")

	finally:
		file.close()

def num_lines(file):
	try:
		file = open(f"{file}", "r+")
		lines = []
		num = 1
		for line in file.readlines():
			if line[0] not in "0123456789\n":
				lines.append(f"{num}. {line}")
				num += 1
			else:
				lines.append(line)
		file.seek(0)
		file.truncate()
		file.writelines(lines)

	except FileNotFoundError:
		file = open(f"{file}", "w")
		file.write(f"File didn't exist.\n")

	finally:
		file.close()

#replace_char_in_txt("laptops.txt", " || ", "||")
replace_char_in_txt("laptops comp.txt", ",", "  ||")
num_lines("laptops comp.txt")