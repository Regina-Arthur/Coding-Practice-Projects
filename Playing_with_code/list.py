correct_fruit = "guava"
fruits = list()
print("""Fruit Guessing Game
Enter Five Fruits and Let's See If You Can Guess The Fruit of The Day""")

quit = 0

while quit < 4:
    quit += 1
    guess= input("Kindly enter a guess: ")
    fruits.append(guess)

print("""Now let's see if your guess was right""")

print("You guessed right, the fruit of the day was", correct_fruit) if correct_fruit in fruits else print("Sorry")