age = input("How old are you: ")
age_int = int(age)

if age_int < 18:
    print("Ah, that were good times!") 
else: 
    print("you are pretty old! Okay grandpa/grandpa ...")
    print("... please wait ...")
    print("... hope you got time left ...")

print("\n")

manipulated_age = int(age) + 7
formatted_string = f"After a bit of research my data tells me you are " + str(manipulated_age) + " years old."
print(formatted_string)