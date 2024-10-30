# ask user to input a number from 1-50 only
    # insert while loop to input a number again
    # if input is invalid - number exceeds 50 or user inserted a letter
        # break loop
# use list to store user input in each range of numbers
    # 1-10
    # 11-20
    # 21-30
    # 31-40
    # 41-50
# once loop is broken, display a tally of frequency for each range

# loop 1 - ask user to input a number from 1-50
while True:
    try:
        random_number = int(input("Please enter a number from 1-50: "))
        if random_number >= 1 and random_number <= 50:
            continue
    except:
        break    