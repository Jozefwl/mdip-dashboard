# Architecture: Gen Z na trhu práce dashboard

Status: draft, waiting for approval. Date: 2026-11-13.

## 1. Intent

Team 6 builds a Dash dashboard, "Gen Z na trhu práce", for the MDIP course. It
shows the results of a questionnaire survey of Gen Z respondents (2025 and 2026)
and, later, the results of a CV audit study.

The code has to read like the teacher's examples in `MDIP_public/Dash`
(`Dash09`, `Dash10`, `Dash12`), because that is what the course teaches and
what the teacher will compare it to. It is also the reference for any AI
assistant working in this repo.

### Course assignment

The course task (MDIP Interpretace a prezentace dat, zima 2026) has two steps:
a hand-drawn A4 design of each dashboard sheet, then the application built from
it. The stated aim is to apply the lectured topics to the team's own output:
aesthetics, colours and colour schemes, layout of elements, choice of chart
types (course chapters 1–3). The assignment also warns about data with gaps.

What this means for the build:

- **The paper design is the specification.** The team's sketches
  (`Tym6_DashBoard_dotazniky.pdf`, `Tym6_DashBoard_audit.pdf`) fix the sheets,
  the order of elements top to bottom (title and tab buttons, filter row,
  four cards, charts in two columns, wide preference chart last), the chart
  types and orientations, and the colour roles. They are stored in
  `docs/navrh/` so the code can be checked against them.
- **Every departure from the sketch is written down** in section 6 with its
  reason, so the team can explain it when presenting.
- **Colour roles from the sketch are kept:** light blue for 2025 and green for
  2026 in every chart, dark blue for headings and frames, blue cards for
  neutral counts, yellow and red cards for the two warning indicators. One
  colour means one thing across the whole dashboard. All of them are defined
  once in `styl.py`.
- **The data is raw.** It has not been cleaned or explored yet. A first look on
  2026-11-13 found 400 and 800 rows, 22 columns each, no empty cells and no
  ragged rows, but that is not an exploratory analysis. Exploration and
  cleaning are their own step before any chart is built (see `pruzkum_dat.py`
  and `vycisti_data()` in section 5).

### Principles applied from the course text

These are our own summary of the course textbook, turned into rules for this
dashboard. Chapters covered: "Typografie a vizualizace", "Typy dat a jejich
prezentace", "Interaktivní prvky ve vizualizacích", "Principy grafické
integrity" and "Úpravy a transformace zobrazení dat". The textbook itself is
not copied into this repo. The summary and this document were prepared with an
AI assistant (Claude) and reviewed by the team. The chapters on colour schemes,
layout of elements and the individual chart types have not been summarised
here yet.

Typography

- Text supports the charts and does not compete with them. One sans-serif
  family for the whole dashboard (Arial, as in `Dash12`), no decorative fonts.
- A fixed text hierarchy, so the eye finds its way quickly: dashboard title,
  then card values, then chart titles, then axis labels and notes. Sizes are
  constants in `styl.py`, not typed into individual components.
- Emphasis comes from size and weight within that hierarchy, not from adding
  more fonts or colours.

Know the data before drawing it

- Before visualising, we establish the structure, the size, the amount of
  missing values and the type of every variable. This is what
  `pruzkum_dat.py` is for.
- The variable type decides the chart. Our variables:

| Type | Columns | Consequence |
|---|---|---|
| Nominal | pohlaví, kraj, věk ovlivňuje přijetí, požadavek praxe | no natural order; used as filters or as bars in a fixed, stated order |
| Ordinal | věková skupina, vnímání trhu práce, dostupnost příležitostí, délka hledání, počet odmítnutí | always shown in their logical order, never alphabetically or by size; no averages are calculated from them |
| Binary | setkal/a se se stereotypem, the eight preference columns | shown as the share of "Ano" |
| Quantitative, discrete | rok narození, věk | not charted directly; věková skupina is used instead |

- Every chart states what it is for. All eight charts on the Dotazník sheet
  are **comparisons** of category shares between two survey years, which is
  why they are grouped bars and why the values are percentages within each
  year (the 2026 sample is twice the size of 2025, so raw counts would
  mislead).

Check after building (for every chart, before it is merged)

1. Does it say the one thing we wanted it to say?
2. Does the chart type fit the type of the variable?
3. Can a teammate who did not build it read it and explain it correctly?

Interactivity

- The amount of interactivity follows the purpose. This is an analytical
  dashboard for exploring survey answers by group, so it gets filters; it does
  not get interaction for its own sake.
- The page follows "overview first, then filter, then details on demand":
  the default view shows all respondents and all cards, the four filters
  narrow the selection, and exact values appear in the hover text of each bar.
- All four filter variables are categorical, so they are dropdowns with a
  "Všechny" option. No sliders, because nothing we filter on is continuous.
- Filtering changes which respondents are included, and every card and chart
  reacts to the same selection. The selection description under the filters
  always says what is currently shown and how many respondents it covers.
- Zoom and pan are for dense scatter plots and maps. On bar charts with a few
  categories they only let the user break the axis by accident, so they are
  switched off on the Dotazník sheet (`config` of `dcc.Graph`). They return
  for the map on the Audit sheet.
- Main values must be readable without hovering. Hover adds precision, it does
  not carry the message.

Graphical integrity

- Each chart has one stated purpose and message, written as a comment above
  its `vytvor_graf_…` function, and the chart is checked against it.
- The data is the most prominent thing in the chart. `uprav_graf` removes what
  does not carry information: white background, light grid lines only on the
  value axis, no frames, no 3D, no decorative effects.
- What the reader perceives must be proportional to the data. Bars show
  values by their length, so **every bar axis starts at zero** and is never
  truncated.
- Few tick marks, at round values (every 10 or 20 percentage points).
- The legend (2025, 2026) sits outside the plotting area. Notes and
  explanations go under the chart or in the footer, not inside it.
- The two years are easy to tell apart and mean the same everywhere: same two
  colours, same order, in every chart.
- Charts must stay readable when small: in a narrow browser window and in a
  screenshot pasted into the team's presentation.
- Chart titles say what is shown and in which unit ("podíl respondentů v %").
  The main findings are visible in the cards and charts themselves, not only
  in accompanying text.
- Building charts is iterative. A first version that follows these rules is a
  starting point; we try alternatives and keep the one that shows the data
  best.

Scales, proportions and orientation

- The same data can look very different when the axis range, aspect ratio or
  axis direction changes, so these are fixed deliberately, not left to chance.
- Charts of the same kind share the same height and proportions (set once in
  `uprav_graf`), so a difference between two charts comes from the data, not
  from the frame.
- **The percentage axis has a fixed range that does not move when filters
  change.** If the axis rescaled itself for every selection, a small group
  would look as dramatic as the whole sample. The range is chosen per chart
  after the exploration shows the largest shares.
- Axes run in the usual direction (values grow upwards or to the right).
  Ordinal categories run in their logical order, from negative to positive or
  from shortest to longest.
- Horizontal bars are used where category names are long, so labels stay
  horizontal and readable.
- No transformed scales. Percentages from 0 to 100 need no logarithmic axis.
- Jittering does not apply: we draw no individual points.

## 2. Goals, non-goals, anti-goals

Goals

- Two tabs, **Dotazník** and **Audit**, following the hand-drawn sketches.
- The Dotazník tab works end to end on the two survey CSVs.
- Code style identical to the course: Czech names, the same helper function
  names, inline style dicts, a module docstring header, pinned versions.
- No data files in git. Data is read from the CDN.
- Runs locally the same way as the course: Run, then `http://127.0.0.1:8050`.

Non-goals (for now)

- **Audit tab content.** No audit data exists yet. The tab shows a short
  "data zatím nejsou k dispozici" text. Tracked in a GitHub issue.
- **Pozice filter** on the Dotazník tab. The CSVs have no such column.
- **Hosting.** Dockerfile, Harbor push and Argo CD manifests come later on a
  separate branch, modelled on `Jozefwl/rene-website` (`k8s/` with four plain
  manifests, namespace `apps`, traefik, `letsencrypt-prod`, manual GitHub
  Actions release). Nothing for it lives on `main`.

Anti-goals

- Code that looks like a generic "enterprise" Dash template (Dash Pages,
  CSS frameworks, class hierarchies, config systems). It would work, and it
  would be the wrong submission.
- Numbers on screen that come from different selections. Every card and chart
  on a tab is computed from the same filtered data, as in `Dash09`–`Dash12`.

## 3. Constraints

- Python 3.12, `dash==4.4.1`, `plotly==7.1.0`, `pandas==2.2.3`,
  `numpy==2.3.5` (the course's `requirements.txt`; `kaleido` is left out
  because nothing is exported to PDF).
- Data source: `https://cdn.waldhauser.sk/data/janjonak/`
  - `kvantititativni_vyzkum_data_2025.csv` (400 respondents)
  - `kvantititativni_vyzkum_data_2026.csv` (800 respondents)
- Both files have the same 22 columns. Several header names have trailing
  spaces. All answer columns are categorical text; the eight preference
  columns are `Ano`/`Ne`.

## 4. Approaches considered

| | Approach | Trade-off |
|---|---|---|
| A | **Small package, course conventions inside it** (chosen) | The course's five file sections become modules. Several teammates can work in parallel and each file stays short. Costs one visible difference from the course: more than one file. |
| B | One file, `Dash/Dash13_GenZ.py` | Indistinguishable from the course examples, but 600–800 lines that the whole team edits at once. |
| C | Full layered app (Dash Pages, `assets/` CSS, config, tests) | The usual community pattern for large apps, but it looks least like the course code and adds parts this project does not need. |

Chosen: **A**, picked by Jozef. Reasoning: 8 charts, 4 cards and 4 filters on
one tab, with a second tab coming, is too much for one file, and the course's
own "mapa souboru" (1. data, 2. grafy, 3. komponenty a layout, 4. callback,
5. server) already gives the module boundaries.

Background for the choice: Plotly publishes no official project structure. The
common community pattern is one entry point that creates the app, separate
modules for data access, figures and layout, and callbacks registered from the
entry point. Approach A is that pattern at the smallest size.

## 5. Structure

```
mdip-dashboard/
├── app.py                 5. server: Dash(), app.layout, dcc.Tabs, app.run
├── dashboard/
│   ├── __init__.py
│   ├── data.py            1. data: načtení CSV, čištění, vyber_data, výpočty
│   ├── styl.py            barvy a slovníky stylů (AKCENT, TMAVA, STYL_KARTY…)
│   ├── grafy.py           2. grafy: uprav_graf, prazdny_graf, vytvor_graf_…
│   ├── komponenty.py      3. komponenty: vytvor_kartu, vytvor_filtr
│   ├── dotaznik.py        záložka Dotazník: layout + registruj_callbacky(app)
│   └── audit.py           záložka Audit: zatím jen informační text
├── pruzkum_dat.py         průzkum dat: výpis struktury a kontrol do konzole
├── data/                  git-ignored; optional local copies of the CSVs
├── docs/ARCHITECTURE.md   this file
├── docs/navrh/            the team's paper design (the two sketch PDFs)
├── CLAUDE.md              rules for AI assistants: style, layering, commands
├── README.md              how to install and run
├── requirements.txt
└── .gitignore
```

### Module responsibilities and dependency rule

Imports only point downwards in this list. A module never imports one above it.

1. `app.py` imports the tab modules and `styl`.
2. `dotaznik.py`, `audit.py` import `data`, `grafy`, `komponenty`, `styl`.
3. `grafy.py` imports `styl`. It receives already filtered data and returns a
   Plotly figure. It does not import `dash`.
4. `komponenty.py` imports `styl`. It returns `html`/`dcc` components and
   knows nothing about the data.
5. `data.py` imports only `pandas`. No Plotly, no Dash.
6. `styl.py` imports nothing from the project.

### `data.py`

- `URL_DAT`: base URL, read from the environment variable `DATA_URL`, default
  the CDN address above.
- `nacti_data()`: for each of the two files, reads `data/<name>` if it exists,
  otherwise `URL_DAT + <name>`. Strips whitespace from headers, renames columns
  to short lowercase names without diacritics through one mapping dict
  (`SLOUPCE`, e.g. `"VĚKOVÁ SKUPINA" -> "vekova_skupina"`), concatenates both
  years. The original header text is kept as the human label for charts and
  for the export.
- `vycisti_data(surova)`: the single place where cleaning rules live. It is
  called by `nacti_data()`. Its rules are written only after the exploration
  has shown what needs cleaning; each rule gets a comment saying what was
  found and why it is handled that way. Answers such as "Nevím", "Netýká se
  mě" and "Dosud nehledal/a" are real categories and stay. If an expected
  column is missing, loading fails with a clear message instead of showing
  wrong numbers.
- `df = nacti_data()` runs once at import, as in the course. **`df` is never
  modified afterwards.** This is also what keeps it safe if the app later runs
  under gunicorn with several workers.
- `vyber_data(rok, pohlavi, vekova_skupina, kraj)`: returns the rows matching
  all conditions; `"Všechny"` means no condition. Same shape as the course's
  `vyber_data`.
- Category orders as constants (e.g. `PORADI_VNIMANI`, `PORADI_DELKY_HLEDANI`)
  so charts show answers in their logical order, not alphabetically.
- Small calculation helpers used by cards and charts, e.g.
  `podily_podle_roku(data, sloupec)` returning percentages within each survey
  year.

### `pruzkum_dat.py`

A stand-alone script in the course's "nejprve vypište do konzole" style. It
imports only the raw loader from `data.py` and prints: number of rows and
columns per year, missing values per column, the distinct values and counts of
every categorical column, duplicate respondent IDs, and consistency checks
(věk = rok šetření − rok narození; věková skupina matches rok narození). It
draws nothing and the dashboard does not depend on it. Its findings are
written into `docs/PRUZKUM_DAT.md` and drive the rules in `vycisti_data()`.

### `grafy.py`

- `uprav_graf(fig)` and `prazdny_graf(nadpis)` exactly as in `Dash12`.
- One `vytvor_graf_…(data)` function per chart. Each returns `prazdny_graf`
  for an empty selection.
- All eight charts are grouped bars, 2025 against 2026, in percent of that
  year's respondents in the current selection:

| Chart | Column | Orientation |
|---|---|---|
| Ovlivňuje věk šanci na přijetí | `vek_ovlivnuje_prijeti` | vertical |
| Vnímání trhu práce | `vnimani_trhu` | horizontal |
| Doba hledání posledního zaměstnání | `delka_hledani` | horizontal |
| Počet odmítnutí uchazeče | `pocet_odmitnuti` | vertical |
| Praxe u juniorských pracovních pozic | `pozadavek_praxe` | vertical |
| Dostupnost pracovních příležitostí | `dostupnost_prilezitosti` | vertical |
| Stereotypy a předsudky | `stereotyp` | horizontal |
| Preference Gen Z | the eight `Ano`/`Ne` columns, share of `Ano` | vertical |

  The data decides the categories. Where the sketch differs (it draws
  "Netýká se mě" under stereotypes, the data has it under praxe), the data
  wins.

### `komponenty.py`

- `vytvor_kartu(nazev, id_hodnoty, vysvetleni)` and
  `vytvor_filtr(nazev, id_prvku, moznosti)` as in `Dash12`.
- `vytvor_kartu` gets one extra argument for the card colour, because the
  sketch uses blue, yellow and red cards.

### `dotaznik.py`

- `vytvor_layout()`: filters (Rok, Pohlaví, Věková skupina, Kraj, all
  defaulting to "Všechny"), the Obnovit and Export buttons, the selection
  description, four cards, eight charts.
- `registruj_callbacky(app)`: defines the callbacks inside with
  `@app.callback`, so the decorator reads as in the course.
  - One callback: four filter Inputs → eight figures, four cards, the
    selection description. Order of `return` matches the order of `Output`.
  - One callback: Export button → `dcc.Download` with the currently filtered
    rows as CSV (`dcc.send_data_frame`, original header names, UTF-8 with BOM
    so Excel opens the Czech characters correctly).
- **Obnovit** is a link to `/` styled as a button. Reloading the page resets
  every filter. It needs no callback.
- Component ids are prefixed with the tab name (`dotaznik-rok`,
  `dotaznik-graf-vnimani`) so the Audit tab can reuse filter names later.

Cards (definitions are a proposal, see section 6):

| Card | Value |
|---|---|
| Počet respondentů | number of rows in the selection |
| Negativní vnímání | share answering "Spíše negativně" or "Velmi negativně" |
| Nedostatek příležitostí | share answering "Spíše ne" or "Ne" on availability |
| Doba hledání | the most frequent answer for search duration |

An empty selection shows "—" in the three calculated cards, never 0 %.

### `audit.py`

- `vytvor_layout()` returns the placeholder text. No callbacks. When the data
  arrives it gets its own loader in `data.py`, its own chart functions in
  `grafy.py` and its own `registruj_callbacky(app)`.

### `app.py`

Creates `app = Dash(__name__)`, sets the title, builds the header and
`dcc.Tabs` with both tab layouts placed directly in `dcc.Tab` (no callback for
switching tabs, as the course assignment recommends), calls each tab's
`registruj_callbacky(app)`, and ends with
`app.run(debug=True, use_reloader=False)` under `if __name__ == "__main__":`.

## 6. Decisions

Decided by Jozef

- Small package with course conventions (approach A).
- `@app.callback` everywhere, same format as `MDIP_public`.
- Audit tab and Pozice filter postponed; Audit tracked in a GitHub issue.
- Local only on `main`; hosting later on another branch.
- Obnovit reloads the page. Export downloads the currently filtered data.
- Data is not in git; it is hosted on the CDN.

Calls made by Claude, open to correction

- Departures from the sketch: no Pozice filter and an empty Audit tab (no
  data), chart categories taken from the data, real card values instead of
  the drawn ones.
- The sketch PDFs are copied into `docs/navrh/` and committed.
- Exploration is a console script (`pruzkum_dat.py`), not a notebook, to stay
  in the course's format; cleaning rules live in one function.
- The course textbook is summarised in our own words, with the AI assistance
  stated; no textbook text or images are stored in the repo.
- A separate `styl.py` for colours and style dicts, so `grafy.py` and
  `komponenty.py` share them without importing each other.
- Local `data/` folder takes priority over the CDN, so the app runs offline.
- Columns are renamed to short lowercase names in code; the export keeps the
  original headers.
- The card definitions in the table above. The sketch shows 35 % and 63 % as
  illustrative numbers; with these definitions the real values for all 1 200
  respondents are 45 % and 65 %.
- With one year selected in the Rok filter, charts show one series instead of
  two.
- Export format is CSV.
- No automated tests on `main`. The course verifies by "kontrolní scénáře"
  (manual checks with known numbers); `README.md` will list a few for this
  dashboard.
- This document and `CLAUDE.md` are in English; code, comments and UI text are
  in Czech like the course.

## 7. Left to the builder

- Exact colours, spacing and chart sizes, within the `Dash12` look and the
  sketch's blue/green year colours.
- Short Czech labels for long category names on chart axes.
- Wording of card explanations, footer notes and the empty-selection text.
