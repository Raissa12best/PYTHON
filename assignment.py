def camel_to_snake(name):
    result = ""
    for letter in name:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    return result
camel_case_name = input("enter a camel case name: ")
snake_case_name = camel_to_snake(camel_case_name)
print("snake case is:",snake_case_name)
