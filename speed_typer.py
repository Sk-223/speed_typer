import random
import time

def speed_typer_game():
    sentence_list = [
    "The quick brown fox jumps over the lazy dog.",
    "Keep calm and code on!",
    "Python is a versatile programming language.",
    "Coding is fun and rewarding.",
    "Practice makes perfect.",
    "Terminal games are a great way to learn programming."
    ]

    play_again = "yes"

    while play_again:
        print("Let's test your speed typing skills!")
        input("Press ENTER to start...")

        total_time = 0
        num_sentences = 0

        for sentence in sentence_list:
            input("Okay! When you're ready, press ENTER to reveal the sentence!")
            print(sentence)
            start_time = time.time()
            typed_sentence = input("^ Type the sentence above ^: ")
            end_time = time.time()

            if typed_sentence == sentence:
                time_taken = end_time - start_time
                total_time += time_taken
                num_sentences += 1
                print(f"WOW! You typed that sentence in {time_taken:.2f} seconds!")
            else:
                print("Oops! You've got a typo! It's okay, keep practicing!")

        if num_sentences > 0:
            average_speed = total_time / num_sentences
            print(f"You're average typing speed is {average_speed:.2f} seconds per sentence! That's incredible!")

        play_again = input("Would you like to play again? (yes/no)")

speed_typer_game()