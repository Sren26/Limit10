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
for x in line:
	count += 1
	if count > limit:
		f1.write("\n")
		count = 0
		
			
f.close()
f1.close()		
	