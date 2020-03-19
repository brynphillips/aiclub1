# 3.17.20 AI Club Coding exercises. These are mostly just for practice. Small Change here.



###
# 
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
###

# def anagram(str1, str2):
#     anagram1 = False
#     for element in str1:
#         if str1.count(element) == str2.count(element):
#             anagram1 = True
#         elif str1.count(element) != str2.count(element): 
#             anagram1 = False
#             print ("This is not an anagram")
#             return
#     if anagram1 == True:
#         print ("This is not an anagram")

# anagram("silent", "listen")


def anagram(s, t):
    if sorted(s.lower()) == sorted(t.lower()):
        print("These are anagrams")
    else:
        print("These are not anagrams")

# anagram("Silent", "Listen")


###
# 
# 
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
###


def palindrome(string1):
    string2 = reversed(string1)
    palin = True
    for elements1, elements2 in zip(string1, string2):
        if elements1 == elements2:
            palin = True
        else:
            palin = False
    if palin == True:
        print("This is a Palindrome")
    else:
        print("This is not a Palindrome")

#palindrome("racecar")


###
#
#
# Write a program that outputs the string representation of numbers from 1 to n. But for multiples of three it 
# should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are 
# multiples of both three and five output “FizzBuzz”.
#
###

# def fizzbuzz(number, n = 1):
#     if n - 1 == number:
#         return
#     if (n % 3 == 0): 
#         print ("Fizz")
#     elif (n % 5 == 0):
#         print("Buzz")
#     else:
#         print (n)
#     fizzbuzz(number, n + 1)

# fizzbuzz(15)


def fizzbuzz(number, n = 1):
    if n - 1 == number:
        return
    if (n % 3 == 0) and (n % 5 == 0): 
        print("FizzBuzz")
    elif (n % 3 == 0): 
        print("Fizz")
    elif (n % 5 == 0): 
        print("Buzz")
    else:
        print (n)
    fizzbuzz(number, n + 1)

#fizzbuzz(15)

###
#
#Count the number of prime numbers less than a non-negative number, n. 
#
###

def prime(number, start = 0, count = 0):
    if start < number:
        for i in range(2, number):
            if number % i == 1:
                count += 1
                start += 1
    print (count)
        

prime(10)