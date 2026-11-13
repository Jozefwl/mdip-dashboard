# CLAUDE.md

Dash dashboard "Gen Z na trhu práce" for the MDIP course (team 6). Read
`docs/ARCHITECTURE.md` before changing anything; it is the source of truth for
structure, scope and visual rules. The paper design in `docs/navrh/` is the
specification of what the dashboard shows.

## The one rule that overrides habits

The code must read like the course examples in `MDIP_public/Dash`
(`Dash09.py`, `Dash10.py`, `Dash12.py`; upstream
https://github.com/karelsafr/MDIP_public). When unsure how to write something,
open `Dash12.py` and write it the same way. Do not "improve" the style.

- Czech identifiers without diacritics: `vyber_data`, `vytvor_graf_vnimani`,
  `vytvor_kartu`, `vytvor_filtr`, `uprav_graf`, `prazdny_graf`,
  `aktualizuj_dotaznik`. Constants in capitals: `AKCENT`, `TMAVA`, `STYL_KARTY`.
- Czech comments, docstrings and UI text, with diacritics.
- Every module starts with a docstring in the course format (what the module
  is for, what belongs in it).
- Inline style dicts passed to `style=`. No CSS files, no `assets/`, no
  Bootstrap or other component libraries.
- Plain functions and module-level constants. No classes, no type-hint-heavy
  code, no dataclasses, no config framework.
- `@app.callback` with `Output`/`Input` listed one per line; the order of
  `return` matches the order of `Output`, with a trailing comment per item as
  in `Dash12`.
- `"Všechny"` is the "no filter" option in every dropdown, `clearable=False`.
- An empty selection shows `prazdny_graf(...)` and "—" in calculated cards,
  never a zero that looks like a real value and never stale results.
- Pinned versions from `requirements.txt`. Do not add dependencies without
  asking.

## Layering

Imports only point downwards:

1. `app.py`
2. `dashboard/dotaznik.py`, `dashboard/audit.py`
3. `dashboard/grafy.py`, `dashboard/komponenty.py`
4. `dashboard/data.py`, `dashboard/styl.py`

- `data.py` imports only pandas. `grafy.py` does not import `dash`.
  `komponenty.py` does not touch data.
- `df` is loaded once at import and never modified. `vyber_data` returns a
  selection; nothing writes to `df`.
- Cleaning rules live only in `vycisti_data()`, each with a comment saying
  what was found in the data and why it is handled that way.
- All cards and charts on a tab are computed from the same `vyber_data`
  result inside one callback.
- Colours, font sizes and style dicts are defined only in `styl.py`.
- Component ids are prefixed with the tab: `dotaznik-rok`,
  `dotaznik-graf-vnimani`.

## Visual rules (details in ARCHITECTURE.md)

- 2025 is light blue, 2026 is green, in every chart, in that order.
- Bar axes start at zero. The percentage axis has a fixed range that does not
  change with filters.
- Values are percentages within each survey year, not raw counts.
- Ordinal answers appear in their logical order (constants `PORADI_…` in
  `data.py`), never alphabetically.
- Legend outside the plot, few round ticks, no decoration, zoom and pan off
  on bar charts.
- Each `vytvor_graf_…` function has a comment stating the chart's purpose.

## Scope

- Audit tab: placeholder only until data exists. Do not invent audit data.
- No Pozice filter (no such column).
- No Dockerfile, CI or `k8s/` on `main`; hosting is planned on another branch.
- Data is never committed. `data/` and `*.csv` are git-ignored; the app reads
  from the CDN (`DATA_URL`) unless local copies exist in `data/`.
- Do not copy text or images from the course textbook into the repo. Rules
  derived from it are summarised in our own words in `ARCHITECTURE.md`.

## Commands

- Run: `python app.py`, then http://127.0.0.1:8050 (Python 3.12).
- Explore data: `python pruzkum_dat.py`.
- There are no automated tests. Verify changes by running the app and
  checking numbers against a manual calculation, as the course does.
