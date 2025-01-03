import random

print("🎡 Welcome to the Wheels of Fortune: Secret Number Edition! 🎡")
print("Guess the secret number between 1 and 10. Spin your luck and win big!")

# Step 1: Generate a random secret number
secret_number = random.randint(1, 10)

# Step 2: Initialize variables
attempts = 0
max_attempts = 3

# Step 3: Start the guessing game
while attempts < max_attempts:
    try:
        guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("🔻 Too low! The wheel spins on...")
        elif guess > secret_number:
            print("🔺 Too high! The wheel spins on...")
        else:
            print("🎉🎊 Congratulations! You guessed it right!")
            print(f"The secret number was indeed {secret_number}. You've won the Wheels of Fortune round!")
            break
    except ValueError:
        print("⚠️ Invalid input! Please enter a number between 1 and 10.")

# Step 4: Handle game over scenario
if attempts == max_attempts and guess != secret_number:
    print("\n⏳ Time's up! Better luck next time!")
    print(f"The secret number was {secret_number}. Thanks for playing Wheels of Fortune!")

