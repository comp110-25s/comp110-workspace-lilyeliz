"""Gameplay of Wordle"""

__author__: str = "730799969"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # this is to establish the turn number
    turn: int = 1
    # this is to have the looped game play with a max of 6 turns and execute the game.
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        # this is to initialize the guess as calling the input_guess (which uses the length of the secret word as the parameter of the function input_guess)
        guess = input_guess(len(secret))
        # Because I initialized the guess variable, I can use this as the parameter of the emojified function and compare it with the secret word to print the boxes of the guess.
        print(emojified(guess, secret))
        # this keeps the game running by increasing the turn if you did not guess the secret or stops it if you've won.
        if guess != secret:
            # since there are only 6 turns, if you didn't guess right and it is the 6th turn, the game is over and it prints. The return is to exit the while loop.
            if turn == 6:
                print(f"X/6 - Sorry, try again tomorrow!")
                return
            # if you didn't guess right and it is not the last turn, increase turn by 1 and go back to the while loop which restarts your turn gameplay as being the next turn increased by 1.
            else:
                turn += 1

        else:
            print(f"You won in {turn}/6 turns!")
            return


def contains_char(string: str, char: str) -> bool:
    """Is the single character found in the string?"""
    assert len(char) == 1, f"len('{char}') is not 1"
    # Looping through every character in a string with a while loop and increasing index/idx returning true if the character is found in the string at that index. Since this code needs to work for all lengths of strings, and go through each index of the length of the string, the parameter for this function that is the string needs to be in the 'while idx < len(string):' and 'if string[idx] == char:', not a fixed thing.
    idx: int = 0
    while idx < len(string):
        if string[idx] == char:
            return True
        idx = idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Are the letters in the right spot?"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    result: str = ""
    # This goes through a loop of adding on a white, yellow, or green box as you increase index by using idx = idx + 1. In "codes", if the first letter of the guess is c, it adds a green box showing it the c is indeed at that spot in the secret's word. By calling the contains_char function, it adds on the yellow box if the guess at that idx is in the secret word. White box for none of these options.
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        idx = idx + 1
    return result


def input_guess(expected: int) -> str:
    """Is the input word expected characters long?"""
    # this prompts "Enter a {expected} character" and it is this input that is assigned to a variable of the user_input so that the length of it can be inspected without repeated prompting of "Enter a "{expected} character"
    user_input: str = input(f"Enter a {expected} character word:")
    # When in the while loop, the user_input has to have a chance to change in order for this to not keep being true and recurring infinitely.
    while len(user_input) != expected:
        # this gives a second chance to change the user_input to go on to the rest of the code and return the string of the input as the result.
        user_input = input(f"That wasn't {expected} chars! Try again:")
    # no matter either pathway, once the user_input's length equals the expected characters, the result is the string of the input.
    result = str(user_input)
    return result


if __name__ == "__main__":
    main(secret="codes")
