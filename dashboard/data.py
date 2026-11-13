"""1. Data: načtení, čištění, výběr podle filtrů a výpočty.

Cíl: jediné místo, které ví, odkud data pocházejí a jak se jmenují sloupce.
Patří sem: načtení CSV, pravidla čištění, vyber_data, pořadí kategorií, podíly.
Nepatří sem: grafy ani komponenty. Modul importuje pouze pandas.
Pravidlo: df se načte jednou při importu a potom se už nemění.
Data nejsou v gitu. Čtou se z CDN, nebo ze složky data/, pokud tam soubory jsou.
"""

import os
from pathlib import Path

import pandas as pd

URL_DAT = os.environ.get("DATA_URL", "https://cdn.waldhauser.sk/data/janjonak/")
SLOZKA_DAT = Path(__file__).resolve().parents[1] / "data"
SOUBORY_DAT = [
    "kvantititativni_vyzkum_data_2025.csv",
    "kvantititativni_vyzkum_data_2026.csv",
]

# Původní hlavička CSV (po odstranění mezer) -> krátký název sloupce v kódu.
# Doplníme po průzkumu dat, viz pruzkum_dat.py.
SLOUPCE = {}

# Logické pořadí odpovědí u pořadových proměnných (PORADI_VNIMANI,
# PORADI_DOSTUPNOSTI, PORADI_DELKY_HLEDANI, PORADI_ODMITNUTI...).
# Doplníme po průzkumu dat.


def nacti_surova_data():
    """Načte oba soubory tak, jak jsou, a spojí je pod sebe. Nic nečistí."""
    raise NotImplementedError


def vycisti_data(surova):
    """Jediné místo s pravidly čištění. Každé pravidlo má komentář s důvodem."""
    raise NotImplementedError


def nacti_data():
    """Surová data přejmenuje podle SLOUPCE a vyčistí."""
    raise NotImplementedError


def vyber_data(rok, pohlavi, vekova_skupina, kraj):
    """Všechny podmínky platí současně. Původní df neměníme."""
    raise NotImplementedError


def podily_podle_roku(data, sloupec):
    """Podíl odpovědí v procentech v rámci každého roku šetření."""
    raise NotImplementedError


# df = nacti_data()  # Zapneme, až bude načtení hotové.
