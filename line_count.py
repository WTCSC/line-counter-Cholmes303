def line_count(file):
  """
  Reference the "Reading Files in Python" lesson to open the `file.txt` file, count the number of words in the file, and return the count.
  """
  #opens file named "file.txt" and reads the file
  file = open('file.txt', 'r') 
  #returns the file and reads/counts lines in the file, +1 is used as counting starts at 0
  return file.readlines() + 1