# Make the AI Judge Feel Curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/yudhisutawan/make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/yudhisutawan/make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

Entry for the [Make the AI judge feel curious bounty](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311) ($50, 20 best win rates share $50).

`main.py` (Python 3.13) writes one short text — 172 Unicode code points — to
`/output/entry.txt`. No network, no input, fully deterministic: the same
text every run. The text was chosen by a head-to-head tournament of 8
candidate texts, each pair judged against the judge's published brief
(intrigue first, calm shown not told, craft, lingering image, freshness).
See [CANDIDATES.md](CANDIDATES.md) for the candidates, the pairwise
verdicts, and why the winner won.

The winning text:

> The old clockmaker keeps one clock that runs backwards, wound every
> morning at seven. He says it is the only one that tells the truth. He
> has never said what time it keeps.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```
