# Write your solution here

gift = float(input("Value of gift: "))

if gift < 5000:
    print("No tax!")
else:
    if gift <= 25000:
        base = 100
        incremental = 0.08
        excess = gift - 5000
        tax = base + (excess * incremental)
    elif gift <= 55000:
        base = 1700
        incremental = 0.10
        excess = gift - 25000
        tax = base + (excess * incremental)
    elif gift <= 200000:
        base = 4700
        incremental = 0.12
        excess = gift - 55000
        tax = base + (excess * incremental)
    elif gift <= 1000000:
        base = 22100
        incremental = 0.15
        excess = gift - 200000
        tax = base + (excess * incremental)
    else:
        base = 142100
        incremental = 0.17
        excess = gift - 1000000
        tax = base + (excess * incremental)
    
    print(f"Amount of tax: {round(tax, 2)} euros")