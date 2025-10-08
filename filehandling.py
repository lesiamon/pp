#f = open('simple.txt', 'rt')
#print(f.read())
#f.close()
#for i in f:
  #  print(i)
#this one is for appending a file
'''
with open('simple.txt', 'a') as f:
    f.write("the file contais lesi as a user of some domanin system")
    '''
#creating a file in is by using 'x' mode
'''
with open('lesi.txt', 'x'):
    pass
    '''
#to dlete a file you must import the os module and reomve .os 
'''
import os
os.remove('lesi.txt')
'''
import os 
if os.path.exists('lesi.txt'):
     os.remove('lesi.txt')
else:
    print("the file does not exist")
     