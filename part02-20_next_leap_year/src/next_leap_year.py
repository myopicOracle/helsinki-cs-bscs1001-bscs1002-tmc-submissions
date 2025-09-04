# Write your solution here   

while True:

    user_input = input("Year: ")
    year = int(user_input)
    next_year = year + 1

    while True:

        is_leap = (next_year % 4 == 0) and (next_year % 100 != 0 or next_year % 400 == 0)

        if is_leap:
            break

        next_year += 1

    print(f"The next leap year after {year} is {next_year}")
    break
