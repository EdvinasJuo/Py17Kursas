# Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string
# tipo parametrus ir turi galimybę būti panaudotas kaip papildomas dekoratorius.

def input_only_string(func):
    def wrapper(text):
        if type(text) != str:
            return "Inputas turi buti string formato."
        return func(text)
    return wrapper

@input_only_string
def returns_string(text):
    return text

print(returns_string(8))