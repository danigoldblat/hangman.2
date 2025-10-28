from game_hangman.game import choose_secret_word, words, init_state



if __name__ == "__main__":
    state = init_state(8)
    print(state)