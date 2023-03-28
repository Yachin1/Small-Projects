from tkinter import *
import random
from PIL import ImageTk, Image
import os

word_list = ["Apple", "Banana", "Pineapple", "Mango", "Strawberries",
             "Grapes", "Jackfruit", "Dragonfruit", "Pear", "Guava"]
selected_word = random.choice(word_list)
hidden_word = ["_" for letter in selected_word]
incorrect_guesses = 0
max_guesses = 6


cwd = os.getcwd()


window = Tk()
window.title("Hangman")
window.geometry("400x400")
hidden_word_label = Label(window, text=" ".join(hidden_word))
hidden_word_label.pack()
incorrect_guesses_label = Label(
    window, text="Incorrect Guesses: " + str(incorrect_guesses))
incorrect_guesses_label.pack()
guess_entry = Entry(window)
guess_entry.pack()
submit_button = Button(window, text="Guess", command=lambda: check_guess())
submit_button.pack()
hangman_image_path = os.path.join(cwd, "hangman0.png")
hangman_image = ImageTk.PhotoImage(Image.open(hangman_image_path))
hangman_image_label = Label(window, image=hangman_image)
hangman_image_label.pack()


def check_guess():
    global selected_word, hidden_word, incorrect_guesses, max_guesses, hangman_image

    guess = guess_entry.get().lower()
    guess_entry.delete(0, END)

    if guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i].lower() == guess:
                hidden_word[i] = guess
        hidden_word_label.config(text=" ".join(hidden_word))
        if "_" not in hidden_word:
            message_label.config(text="You Win!")
            submit_button.config(state=DISABLED)
            return

    else:
        incorrect_guesses += 1
        incorrect_guesses_label.config(
            text="Incorrect Guesses: " + str(incorrect_guesses))
        hangman_image_path = os.path.join(
            cwd, "hangman" + str(incorrect_guesses) + ".png")
        hangman_image = ImageTk.PhotoImage(Image.open(hangman_image_path))
        hangman_image_label.config(image=hangman_image)

        if incorrect_guesses == max_guesses:
            message_label.config(
                text="you lose! The word was " + selected_word)
            submit_button.config(state=DISABLED)
            return


message_label = Label(window, text="")
message_label.pack()


window.mainloop()
