"""Záložka Audit: zatím jen informační text.

Cíl: výsledky auditní studie (oslovené firmy, odeslaná CV, odezva, pohovory).
Stav: data zatím nejsou k dispozici, proto záložka nic nepočítá ani nekreslí.
Až data budou: vlastní načtení v data.py, grafy v grafy.py a zde
registruj_callbacky(app) stejně jako u záložky Dotazník.
"""

from dash import html


def vytvor_layout():
    return html.Div([
        html.P("Data pro auditní studii zatím nejsou k dispozici."),
    ])
