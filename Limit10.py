# Author: Sanford Ren	
# Date: 2/3/16

# Open file
f = open("Input.txt","r")
f1 = open("Output.txt", "w")

# Set the limit of characters in each line
limit = 10
count = 0

contents = f.read()

f1.write(contents)
# This limits the amount of characters in each line, as it reads each letter, the count increases by 1, limit 10.
for x in contents:
	count += 1
	if count > limit:
		f1.write("\n")
		count = 0
		
			
f.close()
f1.close()		
	