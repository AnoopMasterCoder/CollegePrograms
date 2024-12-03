s = input("Enter the number: ")

s_new = s.strip()

if s_new[:] == s_new[::-1]:
    print("The given number is a palindrome!")
else:
    print("The given number is NOT a palindrome!")