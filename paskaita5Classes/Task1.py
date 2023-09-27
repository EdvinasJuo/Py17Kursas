# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
# • Gražina tekstą atbulai
# • Gražina tekstą mažosiomis raidėmis
# • Gražina tekstą didžiosiomis raidėmis
# • Gražina žodį pagal nurodytą eilės numerį
# • Gražina, kiek tekste yra nurodytų simbolių arba žodžių
# • Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
# • Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus
import re

default_text = "Londonas yra Anglijos Sostine"
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def reversed_sentence(self):
        print(f"Tekstas atbulai: {self.sentence[::-1]}")

    def lowercase(self):
        print(f"Tekstas paverstas į mažasias raides: {self.sentence.lower()}")

    def uppercase(self):
        print(f"Tekstas paverstas į didziasias raides: {self.sentence.upper()}")

    def find_word(self):
        words = input_sentence.split()
        if len(words) > input_queue_number:
            print(f"Jusu surastas zodis yra: {words[input_queue_number]}")
        else:
            print("Sarase nera tiek elementu")

    def symbols_words_count(self):
        words = input_sentence.split()
        print(f"Tekste yra simboliu: {len(self.sentence)}")
        print(f"Tekste yra zodziu: {len(words)}")

    def change_symbol_or_word(self):
        print(f"{self.sentence.replace('Labas', 'Ate')}")

    def sentence_info(self):
        words = input_sentence.split()
        print(f"Zodziu sakinyje yra: {len(words)}. Didziuju raidziu: {len(re.findall(r'[A-Z]', self.sentence))}. "
              f"Mazuju raidziu: {len(re.findall(r'[a-z]', self.sentence))}")


input_sentence = input("Įveskite sakinį: ")
sentence = Sentence(input_sentence)

input_queue_number = int(input("Iveskite kuri zodi norite atspausdinti: "))
quene = Sentence(input_queue_number)


sentence.reversed_sentence()
sentence.lowercase()
sentence.uppercase()
sentence.find_word()
sentence.symbols_words_count()
sentence.change_symbol_or_word()
sentence.sentence_info()