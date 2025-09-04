# Write your solution here

# def chessboard(num):
#     total_length = num*num
#     counter = 0

#     print("1", end="")
#     counter += 1

#     for i in range(total_length):

#         if (counter % num) != 0:
#             print("0", end="")
#             counter += 1
#             if (counter % num) != 0:
#                 print("1", end="")  
#                 counter += 1
#             else: 
#                 print("")
#                 counter += 1
#         else: 
#             print("")
#             counter += 1

# chessboard(5)

# def chessboard(num):
#     total_length = num * num
#     counter = 0
#     line_start = 1  

#     for i in range(total_length):
#         if (counter % num) == 0 and counter != 0:
#             print("")  
#             line_start = 1 - line_start  

#         if (counter % 2) == (line_start % 2):
#             print("1", end="")
#         else:
#             print("0", end="")
#         counter += 1

# chessboard(3)

# def chessboard(num):
#     total_length = num * num
#     counter = 0
#     line_start = 1

#     for i in range(total_length):
#         if (counter % num) == 0 and counter != 0:
#             print("")
#             line_start = 1 - line_start

#         if (counter + line_start) % 2 == 0:
#             print("0", end="")
#         else:
#             print("1", end="")
#         counter += 1

# chessboard(3)

def chessboard(num):
    for i in range(num):
        index = ''
        for j in range(num):
            if (i + j) % 2 == 0:
                index += '1'
            else:
                index += '0'
        print(index)

# chessboard(3)
# chessboard(6)

# Testing the function
# if __name__ == "__main__":
#     chessboard(3)
