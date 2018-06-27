import sys
script, filename = sys.argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename,'w')
print "Truncating the file. Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line1:")
line1 = line1.decode(sys.getfilesystemencoding()).encode('utf-8')
line2 = raw_input("line2:")
line2 = line2.decode(sys.getfilesystemencoding()).encode('utf-8')
line3 = raw_input("line3:")
line3 = line3.decode(sys.getfilesystemencoding()).encode('utf-8')
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1+"\n"+line2+"\n"+line3+"\n")
print "And finally,we close it."
target.close()
file = open(filename)
print file.read().decode('utf-8')
file.close()