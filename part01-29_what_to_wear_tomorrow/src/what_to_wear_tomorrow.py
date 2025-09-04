# Write your solution here

print("What is the weather forecast for tomorrow?")

temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ").strip().lower()

wet = rain == "yes"
# print(wet)

if temp <= 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
elif temp <= 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
elif temp <= 20:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
else:
    print("Wear jeans and a T-shirt")

if wet:
    print("Don't forget your umbrella!")