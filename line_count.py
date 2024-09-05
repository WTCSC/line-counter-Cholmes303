def line_count(file):
  """
  Reference the "Reading Files in Python" lesson to open the `file.txt` file, count the number of words in the file, and return the count.
  """
  file = open('file.txt', 'r') 
  return file.readlines() + 1
  

      


  
