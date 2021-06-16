import csv


def max_value(hotel_list, location, index, col_codes):
    if location != "india":
        hotel_sublist = [hotel for hotel in hotel_list if hotel[2].lower() == location]
    else:
        hotel_sublist = hotel_list

    value_sublist = [hotel[index] for hotel in hotel_sublist]
    val_index = max(range(len(value_sublist)), key=value_sublist.__getitem__)

    val_col = ""
    for col, col_code in col_codes.items():
        if col_code == index:
            val_col = col
            break

    if location != "india":
        loct = hotel_sublist[val_index][2]
    else:
        loct = "India"

    print("Hotel with highest " + val_col + " in " + loct + " is " + hotel_sublist[val_index][1] + ", with " + val_col +
          " " + str(hotel_sublist[val_index][index]))


def min_value(hotel_list, location, index, col_codes):
    if location != "india":
        hotel_sublist = [hotel for hotel in hotel_list if hotel[2].lower() == location]
    else:
        hotel_sublist = [hotel for hotel in hotel_list]

    value_sublist = [hotel[index] for hotel in hotel_sublist]
    val_index = min(range(len(value_sublist)), key=value_sublist.__getitem__)

    val_col = ""
    for col, col_code in col_codes.items():
        if col_code == index:
            val_col = col
            break

    if location != "india":
        loct = hotel_sublist[val_index][2]
    else:
        loct = "India"

    print("Hotel with lowest " + val_col + " in " + loct + " is " + hotel_sublist[val_index][1] + ", with " + val_col +
          " " + str(hotel_sublist[val_index][index]))


def avg_value(hotel_list, location, index, col_codes):
    if location != "india":
        hotel_sublist = [hotel for hotel in hotel_list if hotel[2].lower() == location]
    else:
        hotel_sublist = [hotel for hotel in hotel_list]

    value_sublist = [hotel[index] for hotel in hotel_sublist]
    avg_val = sum(value_sublist) / len(value_sublist)

    val_col = ""
    for col, col_code in col_codes.items():
        if col_code == index:
            val_col = col
            break

    if location != "india":
        loct = hotel_sublist[0][2]
    else:
        loct = "India"

    print("Average " + val_col + " of Hotel in " + loct + " is " + str(avg_val))


hotels = []
locations = set()
col_codes = {"cost": 3, "rating": 4}
op_codes = {"highest": max_value, "cheapest": min_value, "average": avg_value}

with open('hotels.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    rows = 0
    for row in my_reader:
        if rows == 0:
            rows += 1
            continue

        p_row = row
        p_row[0] = int(p_row[0])
        for i in [3, 4]:
            p_row[i] = float(p_row[i])

        locations.add(p_row[2].lower())
        hotels.append(p_row)
        rows += 1

while True:

    while True:
        Location = input("What is the state:").lower()
        if Location in locations:
            break
        elif Location == "india":
            break
        else:
            print("Location invalid (not found) - should be one of " + str(
                locations) + " or 'India' (case doesn't matter)")

    while True:
        C_or_R = input("Cost or rating:").lower()
        if C_or_R in col_codes:
            break
        else:
            print("Parameter invalid (should be 'Cost' or 'Rating')")

    while True:
        Opcode = input("Operation:").lower()
        if Opcode in op_codes:
            break
        else:
            print("Invalid operation (should be 'highest', 'cheapest', or 'average')")

    op_codes[Opcode](hotels, Location, col_codes[C_or_R], col_codes)
    print()
