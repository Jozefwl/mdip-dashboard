# Gen Z na trhu práce

Dashboard týmu 6 pro předmět MDIP Interpretace a prezentace dat (zima 2026).
Zobrazuje výsledky dotazníkového šetření mezi respondenty generace Z z let
2025 a 2026. Záložka Audit zatím čeká na data.

Stav: v repozitáři je zatím jen struktura projektu a návrh architektury.

## Spuštění

Potřebujete Python 3.12.

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

Dashboard poběží na http://127.0.0.1:8050. Po úpravě kódu Stop a znovu Run.

## Data

Data nejsou součástí repozitáře. Aplikace je načítá z
`https://cdn.waldhauser.sk/data/janjonak/`. Pokud soubory uložíte do složky
`data/`, použije místní kopie a poběží i bez internetu:

- `kvantititativni_vyzkum_data_2025.csv`
- `kvantititativni_vyzkum_data_2026.csv`

Jinou adresu lze nastavit proměnnou prostředí `DATA_URL`.

## Struktura

| Soubor | Obsah |
|---|---|
| `app.py` | spuštění, rozvržení stránky, záložky |
| `dashboard/data.py` | načtení a čištění dat, výběr podle filtrů, výpočty |
| `dashboard/styl.py` | barvy, velikosti písma, slovníky stylů |
| `dashboard/grafy.py` | funkce vytvářející grafy |
| `dashboard/komponenty.py` | karty a filtry |
| `dashboard/dotaznik.py` | záložka Dotazník |
| `dashboard/audit.py` | záložka Audit |
| `pruzkum_dat.py` | průzkum dat s výpisem do konzole |
| `docs/ARCHITECTURE.md` | návrh architektury a pravidla vizualizace |
| `docs/navrh/` | papírový návrh dashboardu |

Podrobnosti jsou v [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
