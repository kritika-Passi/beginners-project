from datetime import date

user_input_arr = []
def todo():
    i = 1
    while True:
            user_input = input(f"enter task {i}(or press N to end the list)")
            if user_input.lower() == "n":
                break
            user_input_arr.append(user_input)
            i = i+1

    return user_input_arr

def remove():
     rm_task = input("mention the task number you would like to ")
     for idx in user_input_arr:
          if idx == rm_task:
               user_input_arr.remove("rm_task")
          
def done():
     done_task = input("enter the task number that is done")
     for idx in user_input_arr:
          if idx == done_task:
               print(idx , "done")
        
#def edit():
     


today = date.today()
day = today.strftime("%B %d, %Y")
print("Today is : ", day)
print("\n")

while True:
    print("""What would you like to do :\n
      Press T for adding a task.
      Press R for removing a task.
      Press D for marking a task Done.
      Press E for editing a task.
      Press Q to quit\n""")
    user_wish = input("")
    if user_wish == "":
         print("please first type something")
    else:
        if user_wish.lower() == "T":
          final_todo = todo()
        elif user_wish.lower() == "R":
            rm_task = remove()
        elif user_wish.lower() == "D":
             done_task = done()
        #elif user_wish.lower() == "E":
             #edit_task = edit()
            
print("TO-DO : ")
for idx,items in enumerate(final_todo, start=1):
        print(idx,". ", items)