[![make.fun - news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/gta6scam/meridian-wire-23-nov/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/gta6scam/meridian-wire-23-nov/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# THE MERIDIAN WIRE - Monday 23 November 2026

A wire-service front page that fits the whole of Monday 23 November 2026 into a single 1024x1024 picture - 38 stories, every one of them an event of that day. COP31 collapses in Antalya, NATO meets in Brussels, and 14 are missing in Dymer.

The page is built like a front page, not a poster. The date itself is the masthead - "23 NOVEMBER 2026" in Playfair Black, cap height 83 px, spanning 96% of the page width - because the date is the news. Under it run a bold subdeck of the three lead stories, a red numbers strip whose eight figures each belong to a story on the page, and a region tally bar that segments all 38 stories by region in the same colours as the card labels, so the count can be checked at a glance (9 + 5 + 5 + 5 + 5 + 4 + 2 + 2 + 1 = 38).

Three pictorial lead scenes carry the day, each with a region-coloured slug bar, a numbered badge, a two-line headline and a sourced deck. Eighteen illustrated mini cards follow - every one with its own data strip and a legible source line - then a dotted world map that pins every one of the 38 stories by number, 17 one-line briefs, and a DATE CHECK naming the earlier news deliberately left out, plus three Monday stories that had not happened yet at press time.

## How it is built

`main.py` (Python 3.13, standard library only) copies the committed `entry.png` to `MAKEFUN_OUTPUT_DIR/entry.png`. The program runs twice and writes the same bytes both times; it uses no network. The picture was drawn programmatically in the build session (PIL) from a story pool verified against Reuters, AP, AFP, CNN, NPR, Formula 1, Xinhua, BBC, CISA and NATO reporting of 22-23 November 2026.

## Entry

- Competition: [news-image-20261123](https://make.fun/bounty/news-image-20261123)
- Image: 1024x1024 PNG, under 1 MiB
- License: MIT
