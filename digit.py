number_to_word = ["zero","one","two","three","four"]

number = input("Enter a number : ")

words = [number_to_word[int(digit)]for digit in number]
print(", ".join(words))

# Input number as a string to handle each digit
# Convert each digit to word using the list
# Join and print the result