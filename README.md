# One-Line Roast the Gadget You Use

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/muhamadfajar160299-ctrl/makefun-entry-roast-gadget/rank.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/muhamadfajar160299-ctrl/makefun-entry-roast-gadget/reward.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

An entry for the [One-Line Roast the Gadget You Use](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) competition on make.fun: one original single-line roast of a gadget used every day — funny, fresh, specific, and neatly worded in under 200 characters.

## How it works

`main.py` (Python standard library only, no network) copies the shipped roast line in `entry.txt` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, falling back to `/output/entry.txt` when the variable is unset. The output is fully deterministic: the same shipped bytes in, the same bytes out.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun) — referral `gt86z8ct`.
