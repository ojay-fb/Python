summe = 0

for feld in range(64):
    reiskoerner = 2**feld
    summe += reiskoerner
    print(f"Feld {feld+1} = {reiskoerner:>25,} Reiskörner und damit insgesamt" f"{summe:>27,} Reiskörner")

gewicht = summe * 0.02 / 1000 / 1000

print()
print("Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten Reiskörner " f"{gewicht:,.0f} Tonnen!")
print()