# Write your solution here

# Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.

# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list))
# print("mean value is", result)

# Sample output

# mean value is 3.0

def mean(my_list : list) -> list:
    sum_of = sum(my_list)
    length_of = len(my_list)
    mean_of = sum_of / length_of
    return round(mean_of, 2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)