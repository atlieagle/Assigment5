max_int = 0

num_int = int(input("Input a number: "))    # Do not change this line

while num_int >= 0:
    num_new = num_int
    if num_new > max_int:
        max_int = num_new
    print("The maximum is", max_int)    # Do not change this line
    num_int = int(input("Input a number: "))    # Do not change this line
