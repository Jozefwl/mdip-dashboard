"""Záložka Dotazník: rozvržení a callbacky.

Cíl: výsledky dotazníkového šetření 2025 a 2026 podle papírového návrhu.
Obsah shora dolů: filtry (Rok, Pohlaví, Věková skupina, Kraj), tlačítka Obnovit
a Export, popis výběru, čtyři karty, osm grafů.
Pravidlo: všechny karty i grafy používají stejný výběr z vyber_data.
Identifikátory prvků začínají předponou dotaznik-.
"""

from dash import Input, Output, dcc, html

from dashboard import data, grafy, komponenty, styl


def vytvor_layout():
    """Obsah záložky. Obnovit je odkaz na /, načtení stránky vrátí filtry."""
    return html.Div([
        html.P("Záložka Dotazník zatím není hotová."),
    ])


def registruj_callbacky(app):
    """Propojí filtry se všemi kartami a grafy a tlačítko Export se stažením."""
    # @app.callback(...)
    # def aktualizuj_dotaznik(rok, pohlavi, vekova_skupina, kraj):
    #     Jeden výběr dat, ze kterého vznikne osm grafů, čtyři karty a popis.
    #
    # @app.callback(...)
    # def exportuj_vyber(n_clicks, rok, pohlavi, vekova_skupina, kraj):
    #     Aktuálně vyfiltrovaná data jako CSV přes dcc.Download.
