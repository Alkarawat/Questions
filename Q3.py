# Input a five-digit number from the user

num = input("Enter a five-digit number: ")


if len(num) != 5 or not num.isdigit():
    print("Please enter a valid five-digit number.")

else:
    # Reverse the number
    reversed_num = num[::-1]

    print(f"Reversed Number: {reversed_num}")

    
    
    if num == reversed_num:
        print("The original number and the reversed number are equal.")
    else:
        print("The original number and the reversed number are not equal.")
