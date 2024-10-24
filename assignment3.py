def remove_vowels(text):
    vowels = "AEIOUaeioe"
    result = ""
    for letter in text:
        if letter not in vowels:
            result += letter
    return result
text = input("enter the text: ")
new_text= remove_vowels(text)
print("the text without vowels is: ",new_text)
