# Buveinės adresas: Konstitucijos pr. 20A, 03502 Vilnius
# Telefonai:
# 1884 arba +370 5 268 4444 (Privatiems klientams)
# 1633 arba +370 5 268 4422 (Verslo klientams)
# Faksas: (8 5) 258 2700
# El. paštas: info@swedbank.lt
# Įmonės kodas: 112029651
# PVM mokėtojo kodas: LT120296515
# Banko sąskaita: LT55 7300 0100 0000 0036
# Banko kodas: 73000
# SWIFT kodas: HABALT22
#
# 1.
# PAIMA 20'A' Raide
# [A-ZĄČĘĖĮŠŲŪŽ][a-ž]*

# 2.
#
# \b[A-ZĄČĘĖĮŠŲŪŽ]+\d*\b

# 3.
# [1-1][0-9][0-9][0-9]\b

# 4.
# \+370\s\d{0,3}\s\d{0,3}\s\d{4}

# 5.[(]8\s\d[)]\s\d{0,3}\s\d{4}

# 6.
# \+370\s\d{0,3}\s\d{0,3}\s\d{4}|[(]8\s\d[)]\s\d{0,3}\s\d{4}

# 7.
# LT\d+\s\d+\s\d+\s\d+\s\d+

# 8.
# LT\d{9}

# 9.
# \w[a-ž]+(?=:)


# 10.
# \w[a-z]+@+\w+[a-z](?=.)+.+\w
