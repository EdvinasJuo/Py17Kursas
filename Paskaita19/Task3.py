def kmi(svoris, ugis):
    try:
        svoris = float(svoris)
        ugis = float(ugis)
        if 30 <= svoris <= 160 and 0.90 <= ugis <= 2.50:
            kmi = svoris / (ugis ** 2)
            return kmi
        else:
            raise ValueError("Svoris arba ugis neatitinka standartų..")
    except ValueError:
        raise ValueError("Svoris arba ugis neatitinka standartu..")

def kmi_result(svoris, ugis):
    kmi_result = kmi(svoris, ugis)
    if kmi_result < 18.5:
        return f"Jusu KMI yra {kmi_result:.2f} per mazas."
    elif kmi_result < 25:
        return f"Jusu KMI yra {kmi_result:.2f} normalus."
    elif kmi_result < 30:
        return f"Jusu KMI yra {kmi_result:.2f} per didelis."
    else:
        return f"Jusu KMI yra {kmi_result:.2f} labai per didelis."


result = kmi_result(78, 1.92)
print(result)