import random

words_list = ["pingvinas", "obuolys", "batutas", "kate", "pasaulis"]

playing_word = random.choice(words_list)
guessed_word = "_" * len(playing_word)

attempts = 6
used_letters = []

while True:
    print(f"\nZodis: {guessed_word}")
    print(f"Liko bandymu: {attempts}")
    print(f"Naudotos raides: {used_letters}")

    guess = input("Iveskite raide: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Neteisinga ivestis.. Iveskite viena raide.")
        continue

    if guess in used_letters:
        print("Sia raide jau naudojote.")
        continue

    used_letters.append(guess)

    if guess == playing_word:
        print("Atspejote teisinga raide!")

        guessed_word = "".join([c if c == guess or guessed_word[i] != "-" else "-" for i, c in enumerate(playing_word)])

        if guessed_word == playing_word:
            print(f"\nSveikiname! Just atspejote zodi: {playing_word}")
            break
    else:
        print("Neteisinga raide.")
        attempts -= 1
        if attempts == 0:
            print(f"\n Zaidimo pabaiga. Neatspejo zodzio: {playing_word}")
            break