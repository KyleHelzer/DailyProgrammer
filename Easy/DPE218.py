#Daily Programmer Challenge #218 [Easy] Making Numbers Palindromic

#n = firstNumber = int(raw_input("Enter a number: "))
import datetime
import time

f = open("Lychrel_Numbers.txt", "a")
line = str("%s\nThese Lychrel numbers were found:\n") % (datetime.datetime.now())
f.write(line)
f.close()

print "\n"
max = int(raw_input("Calculate Possible Lychrel Numbers from 1 to: "))
Lychrel_Numbers = []

for i in range (1, max + 1):
	n = firstNumber = i
	for j in range(0,1000):
		if n == int(str(n)[::-1]): #tests if the number is palindromic
			print "After %d steps, %d becomes the palindrome %d" % (j, firstNumber, n)
			i += 1;
			break;
		elif n != int(str(n)[::-1]):
			n = n + (int(str(n)[::-1])) #adds n to its palindrome
			j += 1;
	else:
		Lychrel_Numbers.append(i)
		print "The number %d does not become palindromic after 1000 steps" % (firstNumber)
		line = str("%s\n") % (firstNumber)
		f = open("Lychrel_Numbers.txt", "a")
		f.write(line)
		f.close()
else:
	print "\nThese possible Lychrel Numbers were found: ", Lychrel_Numbers, "\n"