from datetime import date

def todo():
    user_input_arr = []
    i = 1
    while True:
            user_input = input(f"enter task {i}(or press N to end the list)")
            if user_input.lower() == "n":
                break
            user_input_arr.append(user_input)
            i = i+1

    return user_input_arr

today = date.today()
day = today.strftime("%B %d, %Y")
print("Today is : ", day)
print("\n")

print("Please enter the task below : ")
final_todo = todo()
print("TO-DO : ")
for items in final_todo:
    print("* ", items)
