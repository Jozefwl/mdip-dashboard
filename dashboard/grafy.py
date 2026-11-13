"""2. Grafy: každá funkce dostane již vyfiltrovaná data a vrátí figuru Plotly.

Cíl: jeden graf, jedna funkce vytvor_graf_..., jedno sdělení.
Patří sem: uprav_graf, prazdny_graf a funkce vytvor_graf_... pro každý graf.
Nepatří sem: filtrování dat (data.py) ani komponenty Dash. Modul neimportuje dash.
Pravidla: osa sloupců začíná nulou, rozsah procentní osy se s filtry nemění,
rok 2025 a 2026 mají vždy stejnou barvu, prázdný výběr vrací prazdny_graf.
Nad každou funkcí je komentář s účelem grafu.
"""

import plotly.graph_objects as go

from dashboard import styl


def uprav_graf(fig):
    """Společný vzhled všech grafů: písmo, okraje, mřížka, legenda mimo graf."""
    raise NotImplementedError


def prazdny_graf(nadpis):
    """Graf s vysvětlením pro výběr, ve kterém nejsou žádní respondenti."""
    raise NotImplementedError


# Grafy záložky Dotazník. Všechny porovnávají podíly odpovědí v letech 2025 a 2026.
# vytvor_graf_vlivu_veku(data)        Ovlivňuje věk šanci na přijetí
# vytvor_graf_vnimani(data)           Vnímání trhu práce
# vytvor_graf_delky_hledani(data)     Doba hledání posledního zaměstnání
# vytvor_graf_odmitnuti(data)         Počet odmítnutí uchazeče
# vytvor_graf_praxe(data)             Praxe u juniorských pracovních pozic
# vytvor_graf_dostupnosti(data)       Dostupnost pracovních příležitostí
# vytvor_graf_stereotypu(data)        Stereotypy a předsudky
# vytvor_graf_preferenci(data)        Preference Gen Z
