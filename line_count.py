def line_count():
  #opens the file as only read
	file = open('file.txt', 'r')
  #reads all of the lines in the opened file
	lines = file.readlines()
  #the length of the lines becomes the output
  output = len(lines)
  #closes the file
  file.close()
  # returnes the output
  return output  

