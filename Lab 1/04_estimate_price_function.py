# Program 4: Function to Estimate House Price Based on Size

# Function to estimate house price
def estimate_house_price(size):
    price = size / 33.33  # Formula: Price = Size / 33.33
    return price

# Test the function with different sizes
size1 = 1000
price1 = estimate_house_price(size1)
print ("Size:", size1, "sq. ft. → Price:", price1, "Lakhs")

size2 = 1800
price2 = estimate_house_price(size2)
print ("Size:", size2, "sq. ft. → Price:", price2, "Lakhs")

size3 = 2200
price3 = estimate_house_price(size3)
print ("Size:", size3, "sq. ft. → Price:", price3, "Lakhs")

size4 = 2500
price4 = estimate_house_price(size4)
print ("Size:", size4, "sq. ft. → Price:", price4, "Lakhs")

size5 = 3000
price5 = estimate_house_price(size5)
print ("Size:", size5, "sq. ft. → Price:", price5, "Lakhs")
