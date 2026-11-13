"""3. Komponenty: opakovaně použitelné části stránky.

Cíl: karta a filtr vypadají na obou záložkách stejně.
Patří sem: vytvor_kartu, vytvor_filtr a další malé stavební prvky.
Nepatří sem: data ani grafy. Komponenty o datech nic nevědí.
"""

from dash import dcc, html

from dashboard import styl


def vytvor_kartu(nazev, id_hodnoty, vysvetleni, barva):
    """Karta s názvem ukazatele, hodnotou a krátkým vysvětlením výpočtu."""
    raise NotImplementedError


def vytvor_filtr(nazev, id_prvku, moznosti):
    """Popisek a rozbalovací seznam s výchozí volbou Všechny."""
    raise NotImplementedError
