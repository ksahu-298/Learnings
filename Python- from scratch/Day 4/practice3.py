#Create a tuple of your favorite 5 fruits.Then print: 1. The total number of fruits and 2. The index of one selected fruit
fav_food1 = input("Enter your first favorite food: ")
fav_food2 = input("Enter your second favorite food: ")
fav_food3 = input("Enter your third favorite food: ")
fav_food4 = input("Enter your fourth favorite food: ")
fav_food5 = input("Enter your fifth favorite food: ")

favorite_foods = (fav_food1, fav_food2, fav_food3, fav_food4, fav_food5)
print("Your favorite foods are:", favorite_foods)
# This code collects the user's five favorite foods and stores them in a tuple.

print(f"The length of your favorite foods tuple is: {len(favorite_foods)} items.")
index = input("Enter the food item you want to find the index of: ")
if index in favorite_foods:
    print(f"The index of {index} is: {favorite_foods.index(index)}")
