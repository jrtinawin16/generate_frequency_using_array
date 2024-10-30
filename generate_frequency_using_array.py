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

# define dictionary for random numbers
data_inserted_numbers = {}
# loop 1 - ask user to input a number from 1-50
while True:
    try:
        random_number = int(input("Please enter a number from 1-50: "))
        if random_number >= 1 and random_number <= 50:
            continue
        elif random_number == 0:
            break
        elif random_number > 50:
            break
    except:
        break    

    data_inserted_numbers[random_number]= {
        "data_range_1_10" : 0,
        "data_range_11_20" : 0,
        "data_range_21_30" : 0,
        "data_range_31_40" : 0,
        "data_range_41_50" : 0
    }

for random_number in data_inserted_numbers:
    if random_number == 1 and random_number <= 10:
        "data_range_1_10" + 1
    elif random_number == 11 and random_number <= 20:
        "data_range_11_20" + 1
    elif random_number == 21 and random_number <= 30:
        "data_range_21_30" +1