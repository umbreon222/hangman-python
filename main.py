def get_phrases():
    f = open("./phrases.txt", "r")
    file_content = f.read()
    return file_content.split(';')

def print_game_status(lives: int, phrase: str, letters_guessed: list[str]):
    letters_guessed_clone = letters_guessed.copy()
    letters_guessed_clone += ' ' # Add space as a guessed letter so we don't replace it with an underscore
    status = ''
    for character in phrase:
        if character.lower() in letters_guessed_clone:
            status += character
            continue
        status += '_'
    status += "; lives left: {0}".format(lives)
    print(status)

def get_guessed_letter(user_guess: str):
    lower_case_user_guess = user_guess.lower()
    if len(lower_case_user_guess) > 0:
        return lower_case_user_guess[0]
    return None

def get_phrase_solved(phrase: str, letters_guessed: list):
    letters_guessed_clone = letters_guessed.copy()
    letters_guessed_clone += ' ' # Add space as a guessed letter so we don't make the user guess spaces
    lower_case_phrase = phrase.lower()
    for character in lower_case_phrase:
        if character not in letters_guessed_clone:
            return False
    return True

def main():
    lives = 6 # represents the 6 parts of the body you draw
    phrases_list = get_phrases()
    for phrase in phrases_list:
        phrase_solved = False 
        letters_guessed = []
        while not phrase_solved and lives != 0:
            print_game_status(lives, phrase, letters_guessed)
            user_guess = input("Please input guess letter:")
            guessed_letter = get_guessed_letter(user_guess)
            if guessed_letter == None:
                print("You need to guess a letter.")
                continue
            if guessed_letter in letters_guessed:
                print("You guessed \"{0}\" already.".format(guessed_letter))
                continue
            letters_guessed += guessed_letter
            if guessed_letter not in phrase:
                print("Too bad! The phrase does not contain \"{0}\"".format(guessed_letter))
                lives -= 1
                if lives == 0:
                    print("You've lost! The phrase was:")
                    print("\"{0}\"".format(phrase))
                    print()
                continue
            print("Good guess! The phrase contains \"{0}\"".format(guessed_letter))
            phrase_solved = get_phrase_solved(phrase, letters_guessed)
            if phrase_solved:
                print("Congrats! You've solved the hangman! The phrase was:")
                print("\"{0}\"".format(phrase))
                print()
                lives = 6
    print("GAME OVER.")

if __name__ == "__main__":
    main()
