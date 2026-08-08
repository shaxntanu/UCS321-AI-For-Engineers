# Program 5: Classify House as Affordable or Expensive

# Function to classify house
def classify_house(price):
    if price <= 50:
        return "Affordable"
    else:
        return "Expensive"

# Test with different prices
price1 = 30
result1 = classify_house(price1)
print ("Price:", price1, "Lakhs →", result1)

price2 = 45
result2 = classify_house(price2)
print ("Price:", price2, "Lakhs →", result2)

price3 = 60
result3 = classify_house(price3)
print ("Price:", price3, "Lakhs →", result3)

price4 = 75
result4 = classify_house(price4)
print ("Price:", price4, "Lakhs →", result4)

price5 = 90
result5 = classify_house(price5)
print ("Price:", price5, "Lakhs →", result5)
