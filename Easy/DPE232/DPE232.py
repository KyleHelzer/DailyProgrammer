print '\n'
fileName = raw_input("Enter file name: ")
with open(fileName, 'r') as f:
	string = f.read().replace('\n', '')

#string = raw_input("Enter string: ")
compactString = ''.join(i for i in string if i.isalnum())

if compactString.lower() == compactString[::-1].lower():
	print '\n', "Palindrome", '\n'
else:
	print '\n' "Not a Palindrome", '\n'