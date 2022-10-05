from random import randint
#PESEL YYMMDDxxxSK
def generate_pesel(y, m, d, sex):
    #year 2 ostatnie liczby z roku urodzenia 
    pesel = y[-2:]

    #month 
    if len(m) == 1:
        pesel = pesel + "0" + m
    else:
        pesel = pesel + m

    #day
    if len(d) == 1:
        pesel = pesel + "0" + d
    else:
        pesel = pesel + d
    
    #xxx 3 losowe cyfry
    pesel = pesel + "{:03}".format(randint(0, 999))

    #płeć
    if sex == "k":
        pesel = pesel + str(randint(0, 4) * 2)   #tworzy liczby parzyste od 0 do 8
    else:
        pesel = pesel + str(randint(0, 4) * 2 + 1)   #tworzy nieparzyste od 0 do 9

    pesel = pesel + control_number(pesel)
    return(pesel)

#print(generate_pesel("1989", "7", "20", "k"))

def control_number(p): #parametr p to moj dotychczas wygenerowany pesel
    #10 cyfr z nr pesel * waga 1, 3, 7, 9 
    sum = 0
    waga = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    for i in range(len(p)):
        sum += (waga[i] * int(p[i]))
    k = 10 - (sum % 10)   # x % 10 to wzór na wyliczanie części dziesiętnych
    return(str(k))

#print(generate_pesel("1989", "7", "20", "k"))

def pesel_is_valid(pesel):
    if pesel[-1] == control_number(pesel[:-1]):
        return(True)
    else:
        return(False)

print(pesel_is_valid(generate_pesel("2011", "3", "23", "k")))