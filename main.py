#alpha version which is also
# this ===> version 1.0

print("This is not fully functional yet.Only functions and other things work.")
print("Also,loops and the def function doesn't work.")
print("And for last, this thing doesn't return things.")
print("you have to set it as a variable.")
print("And not for last,modules don't work")


print("=========================================RESTART=========================================")
print("Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32")
#initialize variables
print("Type copyright, credits ,or license() for more information.")

b=0
s=4
#main loop

while s==4:
	try:
		
		a=input(">>> ")
		if a=="quit()":
			print("by by!")
			
		exec(str(a))
			
	
	except:
		print("sorry, there either was an error, or there was a syntax error. please try again.")
		
	
