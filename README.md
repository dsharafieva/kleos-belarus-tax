# Kleos — Belarus contractor-taxation page

A self-contained landing page explaining what a contractor in Belarus actually
keeps, with a live gross-to-net calculator across the three realistic statuses —
plus a neutral, factual briefing on the part that usually matters more than tax:
**sanctions and payment feasibility**. EN / RU toggle. Same design system as the
Romania, Spain and Serbia pages in this series.

## Files
- `index.html` — the entire page (HTML + CSS + JS, no build step, no dependencies)
- `app.py` — thin Streamlit wrapper that renders `index.html` full-bleed
- `requirements.txt` — Streamlit dependency for cloud deploy
- `README.md` — this file

## Run it

**Just open it.** `index.html` is standalone — double-click it, or open in any
browser. Nothing to install.

**As a Streamlit app (local):**
```bash
pip install streamlit
streamlit run app.py
```
`app.py` and `index.html` must sit in the same folder.

**On Streamlit Community Cloud:** push all four files to a GitHub repo (root),
then deploy `app.py` at share.streamlit.io. `requirements.txt` must be in the
repo or the build fails with `ModuleNotFoundError`.

## What the calculator models

Currency: shown in **euros** for comparability with the other country pages and
because foreign hiring is priced in EUR — but **Belarusian tax is assessed in
rubles (BYN)**. Amounts convert at an indicative `BYN_PER_EUR = 3.55`; the rate
moves. Say the word and this can be rebuilt ruble-native.

Three statuses (tabs):

1. **Self-employed (professional income tax, НПД)** — a flat **10% of revenue**
   that already bundles social contributions, no expense deduction.
   `net = invoiced × 0.90`. Income from foreign clients stays at 10%; the higher
   20% band applies only to income from Belarusian companies above 60,000 BYN.
   Simplest and cheapest — the default for a solo cross-border contractor.
2. **Entrepreneur (IP)** — 20% income tax on profit (`invoiced − expenses`),
   plus the ФСЗН social-contribution floor: 35% on a minimum base of 12× the
   monthly minimum wage (~€860/yr), which is deductible. A 30% band applies to
   very high entrepreneur income (not modelled).
3. **OOO (company)** — 20% profit tax, then 13% on distributed dividends.
   `profit = invoiced − expenses`.

Both directions work: enter an invoice to see the net, or a target net to solve
for the invoice (60-step binary search).

The **sanctions & payments** section is a neutral briefing, not a scored test:
a US/EU divergence panel plus a practical six-step readiness checklist (screen
your jurisdiction, screen the counterparty and their bank, confirm a working
rail, etc.). The checklist just counts confirmed steps — it deliberately does
**not** render a red/green "risk verdict", because trivialising sanctions
exposure would be the wrong call.

## Updating the numbers each year

All tax parameters live in one `TAX` object plus the `BYN_PER_EUR` and `MZP_BYN`
constants near the top of the `<script>` in `index.html`. To refresh:

- `BYN_PER_EUR` — indicative exchange rate
- `MZP_BYN` — monthly minimum wage (feeds the IP contribution floor)
- `npd.rate` — self-employed rate (0.10)
- `ip.rate` — entrepreneur income-tax rate (0.20); `fsznFloorEUR` recomputes from
  `MZP_BYN` automatically
- `ooo.corpRate` / `dividendRate` (0.20 / 0.13)
- `highBandBYN` — the 220,000 BYN threshold referenced in copy

You should not need to touch the engine or layout for a yearly figures refresh.

## Honest caveats (read these — Belarus needs them more than the others)

- **Sanctions and payment feasibility usually dominate the tax result.** A clean
  10% calculation is meaningless if you can't legally or practically send the
  money. The briefing is a *neutral, high-level snapshot as of 2026* and it
  changes fast; the US has been easing since late 2025 while the EU has not.
  **Screen every counterparty against your own government's current lists and
  take qualified sanctions advice before paying anyone in Belarus.** This page is
  not sanctions-compliance advice.
- **Belarusian tax rates have changed repeatedly** (the simplified system for
  entrepreneurs was abolished in 2023; the self-employed НПД was introduced in
  2023; personal, dividend and profit rates have all moved since). Treat the
  figures as a 2026 snapshot and confirm current law.
- **The IP contribution floor is a simplification** — it is the mandatory minimum
  for entrepreneurs earning above 12× the minimum wage; lower earners pay on
  actual income, and anyone can pay more voluntarily for higher pension accrual.
- **The OOO route excludes a director's salary and contributions and accounting**,
  the 25% personal band above 220,000 BYN, and any High-Tech Park relief — a real
  company's take-home differs, sometimes a lot (HTP can push it far lower).
- **EUR is indicative.** Belarusian tax is assessed in rubles; the rate moves.
- This is general information, **not tax, legal, accounting or sanctions advice.**
  Confirm the tax with a Belarusian adviser and the sanctions position with
  qualified counsel in your own jurisdiction.

Figures reflect the 2026 Belarusian rules.
