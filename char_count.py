Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

test_str = 'hello welcome to python'
 

print("The original string is : " + str(test_str))

res = len([ele for ele in test_str if ele.isalpha()])

print("Count of Alphabets : " + str(res))
