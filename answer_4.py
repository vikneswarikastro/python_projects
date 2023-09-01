a=input()   --------------------------------------------->a is a input in string
vowels=['a','e','i','o','u','A','E','I','O','U']-----------------------> vowels in the list
result=""               ------------------------------------------------------>result is a empty string
for i in range(len(a)):   --------------------------------------------------------> for loop is used to iterate the string a
  if a[i]not in vowels:  -----------------------------------------------------------------> if condition used to check the vowels are present in the given string
    result=result+a[i]----------------------------------------------------------------------->then consonants are add in the result
print(result)   --------------------------------------------------------------------------------->print fun is used to print the output result
