
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURE."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
 
print "Truncating the file. Goodbye!"
target.truncate()
 
 
print "Now I'm going to ask you for three lines."
 
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
 
print "I'm going to write there to the file."
 
targer.write(line1)
targer.write("\n")
targer.write(line2)
targer.write("\n")
targer.write(line3)
targer.write("\n")
 
print "And finally, we close it."
targer.close()
 