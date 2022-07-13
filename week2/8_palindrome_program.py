
def palindrome(num):
        reverse_int = 0
        original_num = num
        while(num != 0):
                remainder = num % 10
                reverse_int = reverse_int * 10 + remainder
                num = num//10
        if reverse_int == original_num:
                return f"{original_num} is a Palindrome"
        else:
                return f"{original_num} is not a Palindrome"

numb = int(input("Enter an integer with atleast of length of 5: "))
print(palindrome(numb))