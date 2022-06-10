Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]

print ("The list after removing duplicates : " + str(res))
