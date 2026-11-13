"""Gen Z na trhu práce: dashboard týmu 6.

Cíl: přehled výsledků dotazníkového šetření a auditní studie ve dvou záložkách.
Spuštění: Run, http://127.0.0.1:8050. Po úpravě kódu Stop a znovu Run.
Data nejsou v gitu, načítají se z CDN nebo ze složky data/.

Mapa projektu: 1. data (dashboard/data.py), 2. grafy (dashboard/grafy.py),
3. komponenty (dashboard/komponenty.py) a rozvržení záložek
(dashboard/dotaznik.py, dashboard/audit.py), 4. callbacky (registruj_callbacky
v modulech záložek), 5. server (tento soubor).
"""

from dash import Dash, dcc, html

from dashboard import audit, dotaznik, styl

app = Dash(__name__)
app.title = "Gen Z na trhu práce"

# Obsah obou záložek je přímo v dcc.Tab. Přepínání nepotřebuje callback.
app.layout = html.Div([
    html.Header([
        html.H1("Gen Z na trhu práce",
                style={"fontSize": styl.VELIKOST_NADPISU, "margin": "10px 0"}),
    ]),
    dcc.Tabs(id="zalozky", value="dotaznik", children=[
        dcc.Tab(label="Dotazník", value="dotaznik",
                children=dotaznik.vytvor_layout()),
        dcc.Tab(label="Audit", value="audit",
                children=audit.vytvor_layout()),
    ]),
], style=styl.STYL_STRANKY)

# 4. Callbacky jednotlivých záložek
dotaznik.registruj_callbacky(app)

# 5. Spuštění místního serveru; po změně kódu Stop, Run a obnovení stránky.
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
