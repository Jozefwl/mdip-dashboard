"""Průzkum dat: výpis struktury a kontrol do konzole.

Cíl: poznat data dřív, než z nich vznikne první graf.
Vypíše: počet řádků a sloupců podle roku, chybějící hodnoty ve sloupcích,
varianty a četnosti kategoriálních sloupců, duplicitní ID respondentů
a kontroly souladu (věk = rok šetření − rok narození, věková skupina
odpovídá roku narození).
Spuštění: Run. Skript nic nekreslí a dashboard na něm nezávisí.
Zjištění zapisujeme do docs/PRUZKUM_DAT.md; podle nich vznikají pravidla
ve funkci vycisti_data v dashboard/data.py.
"""

from dashboard import data

if __name__ == "__main__":
    surova = data.nacti_surova_data()
    # Jednotlivé kontroly doplníme zde, každou s nadpisem ve výpisu.
