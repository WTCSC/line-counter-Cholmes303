def line_count():
  """
  Reference the "Reading Files in Python" lesson to open the `file.txt` file, count the number of words in the file, and return the count.
  """
  #opens file named "file.txt" and reads the file
  file = open('file.txt', 'r') 
  #returns the file and reads/counts lines in the file by len() function
  length = len(file.readlines())
  #closes file after reading and counting lines
  file.close()
  #returns the amount of lines within the file
  return length