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
data_frequency = {
    "1-10" : 0,
    "11-20" : 0,
    "21-30" : 0,
    "31-40" : 0,
    "41-50" : 0
}
# loop 1 - ask user to input a number from 1-50
while True:
    try:
        random_number = int(input("Please enter a number from 1-50: "))
        if random_number >= 1 and random_number <= 50:
            if random_number == 1 and random_number <= 10:
                data_frequency["1-10"] += 1
            elif random_number == 11 and random_number <= 20:
                data_frequency["11-20"] += 1
            elif random_number == 21 and random_number <= 30:
                data_frequency["21-30"] += 1
            elif random_number == 31 and random_number <= 40:
                data_frequency["31-40"] += 1
            elif random_number == 41 and random_number <= 50:
                data_frequency["41-50"] += 1
        elif random_number == 0:
            break
        elif random_number > 50:
            break
    except:
        break     

print("The frequency of inserted numbers in each range are:")
for range, count in data_frequency.items():
    print(f"{range}:  {count}")