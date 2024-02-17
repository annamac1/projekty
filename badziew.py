import datetime
import random

def generuj_horoskop_i_przepowiednie(data_urodzenia):
    znak = okresl_znak_zodiaku(data_urodzenia)
    horoskop = generuj_horoskop(znak)
    przepowiednia = generuj_przepowiednie()
    print(znak)
    print(horoskop)
    print(przepowiednia)
    return f"{horoskop}\nTwoja przepowiednia: {przepowiednia}"

def generuj_horoskop(znak_zodiaku):
    cechy = {
        'Baran': 'Odważny i energiczny',
        'Byk': 'Stabilny i cierpliwy',
        'Bliźnięta': 'Elastyczny i towarzyski',
        'Rak': 'Opiekuńczy i czuły',
        'Lew': 'Pewny siebie i kreatywny',
        'Panna': 'Pracowity i analityczny',
        'Waga': 'Sprawiedliwy i ugodowy',
        'Skorpion': 'Intensywny i tajemniczy',
        'Strzelec': 'Optymistyczny i niezależny',
        'Koziorożec': 'Ambitny i cierpliwy',
        'Wodnik': 'Oryginalny i niezależny',
        'Ryby': 'Wrażliwy i kreatywny'
    }

    if znak_zodiaku.capitalize() in cechy:
        return f"Twój horoskop dla znaku {znak_zodiaku}: {cechy[znak_zodiaku.capitalize()]}"
    else:
        return "Podano niepoprawny znak zodiaku."

def generuj_przepowiednie():
    przepowiednie = [
        "Dziś jest dobry dzień, aby podjąć ryzyko.",
        "Bądź otwarty na nowe możliwości.",
        "Twoje wysiłki przyniosą ci sukces.",
        "Zachowaj spokój w trudnych sytuacjach.",
        "Pamiętaj o ważnych relacjach rodzinnych."
    ]
    return random.choice(przepowiednie)

def okresl_znak_zodiaku(data_urodzenia):
    daty_znakow = {
        'Baran': (datetime.date(1, 3, 21), datetime.date(1, 4, 19)),
        'Byk': (datetime.date(1, 4, 20), datetime.date(1, 5, 20)),
        'Bliźnięta': (datetime.date(1, 5, 21), datetime.date(1, 6, 20)),
        'Rak': (datetime.date(1, 6, 21), datetime.date(1, 7, 22)),
        'Lew': (datetime.date(1, 7, 23), datetime.date(1, 8, 22)),
        'Panna': (datetime.date(1, 8, 23), datetime.date(1, 9, 22)),
        'Waga': (datetime.date(1, 9, 23), datetime.date(1, 10, 22)),
        'Skorpion': (datetime.date(1, 10, 23), datetime.date(1, 11, 21)),
        'Strzelec': (datetime.date(1, 11, 22), datetime.date(1, 12, 21)),
        'Koziorożec': (datetime.date(1, 12, 22), datetime.date(1, 1, 19)),
        'Wodnik': (datetime.date(1, 1, 20), datetime.date(1, 2, 18)),
        'Ryby': (datetime.date(1, 2, 19), datetime.date(1, 3, 20))
    }

    for znak, (data_poczatkowa, data_koncowa) in daty_znakow.items():
        if data_poczatkowa.month == data_urodzenia.month and data_poczatkowa.day <= data_urodzenia.day or \
                data_koncowa.month == data_urodzenia.month and data_koncowa.day >= data_urodzenia.day:
            return znak


# Przykład użycia
data_text = input("Podaj datę urodzenia w formacie RRRR-MM-DD: ")
data_urodzenia = datetime.datetime.strptime(data_text, "%Y-%m-%d").date()
wynik = generuj_horoskop_i_przepowiednie(data_urodzenia)
print(wynik)


