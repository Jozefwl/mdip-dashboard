"""Společný vzhled: barvy, velikosti písma a slovníky stylů.

Cíl: každá barva a velikost je určena jednou a znamená v celém dashboardu totéž.
Patří sem: konstanty barev, velikosti písma, slovníky pro parametr style.
Nepatří sem: komponenty (komponenty.py) ani úprava figur (grafy.py).
Tento modul neimportuje nic z projektu.
"""

# Barvy rolí. Hodnoty doladíme podle papírového návrhu v docs/navrh.
AKCENT = "#087f8c"
TMAVA = "#19324d"
SEDA = "#61738a"
POZADI = "#f2f5f9"

# Roky šetření mají ve všech grafech stejnou barvu i pořadí.
BARVY_ROKU = {2025: "#2bb5e8", 2026: "#3fa35b"}

# Karty: modrá pro neutrální počty, žlutá a červená pro varovné ukazatele.
BARVA_KARTY_NEUTRALNI = "#2bb5e8"
BARVA_KARTY_VAROVANI = "#f5c400"
BARVA_KARTY_PROBLEM = "#e5383b"

# Hierarchie textu: nadpis, hodnota karty, nadpis grafu, popisky, poznámky.
PISMO = "Arial, sans-serif"
VELIKOST_NADPISU = "36px"
VELIKOST_HODNOTY = "32px"
VELIKOST_NADPISU_GRAFU = 20
VELIKOST_TEXTU = 13
VELIKOST_POZNAMKY = "12px"

STYL_RADKU = {"display": "flex", "flexWrap": "wrap", "gap": "18px"}
STYL_KARTY = {"backgroundColor": "white", "borderRadius": "12px",
              "padding": "22px", "flex": "1 1 210px", "minWidth": 0,
              "boxShadow": "0 2px 8px #10243b10"}
STYL_STRANKY = {"fontFamily": PISMO, "color": TMAVA,
                "backgroundColor": POZADI, "maxWidth": "1280px",
                "margin": "0 auto", "padding": "24px"}
