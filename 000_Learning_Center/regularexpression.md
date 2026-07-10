Source: https://www.youtube.com/watch?v=teO7rW2eUcM&t=2896s



# Regular Expression.

	If we want to represent a group of strings according to a particular pattern then we should go for Regular expression
	eg mobile numbers, email id format, password format, otp pattern....

Main important application areas of Regular Expression. 
	1. To perform validation 
	2. To check a pattern available or not. To develop pattern matching application (Ctrl+F)
	3. Translators like compilers, interpreters, assemblers. 
	4. To develop digital circuits 
	5. Communication protocol TCP/ IP etc....

# re Module:
	1. Compile() --> function:
	2. finditer() --> returns the itera
	3. start() --> Start index of the matched pattern. 
	4. end() --> end+1 index of the match
	5. group() --> Returns the matched string. 

# Character Classes:
	[abc] --> either a or b or c
	[^abc] --> except a b and c
	[a-z] --> any lower case alphabets
	[A-Z] --> any upper case alphabets
	[a-zA-Z] --> Any alphabet symbol
	[0-9]--> any number
	[a-zA-Z0-9]-->any Alpha numeric character
	[^a-zA-Z0-9]-->Any other than alpha numerical symbols (special symbols.)

# Predefined Character classes:
	\s --> space character
	\S --> except space character
	\d --> digits equivalent to [0-9]
	\D --> except digit[^0-9]
	\w --> any word character (alpha numeric)[a-zA-Z0-9]
	\W --> any character except word (special Character) [^a-zA-Z0-9]
	. --> any or every character.

# Quantifiers:
	it is used to specify number of occurances to match. 
	a --> exactly one "a"
	a+ --> atlest one "a"
	a* --> any number of a's including zero number also meaning where there is any other alphabet eg:..
		'abaabaaab'
		start:0 ........ group:a
		start:1 ........ group:
		start:2 ........ group:aa
		start:4 ........ group:
		start:5 ........ group:aaa
		start:8 ........ group:
		start:9 ........ group:
	a? --> atmost 1 a (either one a or zero a)
	a{n} --> exactly n number of a's
	a{m,n} --> min m number of a's and maximum n mumber of a's
	^a --> it will check if the given target string starts with a or not. 
	a$ --> it will check if the given target string ends with a or not.

# Important Function of re module:
	1. match() --> To check the given pattern at the begining of the string. If yes it returns match object otherwise none. (similar to startswith)
	2. fullmatch() --> complete string match. 
	3. search() --> match object of the first occurance else none
	4. findall() --> find all match string and show it in a form of a list. 
	5. finditer() --> returns iterator of matched object in a form of a list. 
	6. sub() -->
	7. subn()
	8. split()
	9. compile()

