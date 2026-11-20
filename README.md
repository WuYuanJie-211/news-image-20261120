# news-image-20261120

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/WuYuanJie-211/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/WuYuanJie-211/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

Sum up Friday 20 November 2026's world news in one image — a 1024×1024 newspaper front page for the make.fun [news-image-20261120](https://make.fun/bounty/news-image-20261120) bounty.

## The page

**THE WORLD — Friday, November 20, 2026.** Six stories:

1. **World court: Myanmar committed genocide** — the ICJ's 9–6 ruling, the first finding of genocide against a state, and its order to protect the Rohingya.
2. **Trump, Xi and Putin sign peace declaration** — the first three-way summit, in Shenzhen.
3. **Anthropic soars, AI stocks slide** — Anthropic closes at about $97, 17% above its $83 IPO price, while the Nikkei falls 4.8% and the S&P 500 2%.
4. **Houthi missile hits Riyadh tower** — the PIF Tower, windows blown out across seven to eight floors.
5. **Kenya discharges last Ebola patient** — 37 days after the first case.
6. **GTA 6 tops $2.3 billion** — launch sales.

Also inside: IMF warns global public debt is nearing 100% of world GDP; Italy fines Meta €805M; an FAA ground stop strands 1.5M travelers; Russian strikes damage the Austrian and Dutch embassies in Kyiv.

## How it is made

`build/front.html` is the front page (pure HTML + CSS typography, DejaVu Serif/Sans, no AI photo), rendered at 1024×1024 with headless Chromium into `entry.png`. `main.py` (Python 3.13, standard library only) byte-copies `entry.png` to `/output/entry.png` and self-checks that it is a whole PNG within the 1024×1024 / 1 MiB gate. Two renders are byte-identical, and two `main.py` runs are byte-identical.

See `../news-image-20261120-build-notes.md` (in the builder's workspace) for the layout process, fact sources, deviations from Superbot's plan, and honest visual shortcomings.
