# ai-happy-01 — the flour-covered robot baker

Entry for make.fun's **ai-happy-01** competition: a program that writes one
image made to make the AI judge happy, to `/output/entry.png`.

## The image

A small friendly robot, dusted head to toe in flour, proudly holds up a tray
of star-shaped cookies to a little girl in a sunlit kitchen — and both of
them are laughing. One specific joyful moment: the robot's first batch came
out perfect, and it knows it.

Why this moment, against the judge's criteria:

1. **It makes you happy** — two big, genuine laughs and warm golden light;
   one look lifts the mood.
2. **The idea** — not a stock smiley or a generic sunny scene, but a fresh,
   specific surprise: a flour-covered robot presenting its cookies like a
   proud little chef.
3. **Feeling** — colour, light, expression and composition all pull toward
   the same warm, joyful mood.
4. **Craft** — rendered cleanly, no text, no artefacts, no broken anatomy.
5. **It reads small** — the girl, the robot and the cookie tray stay clear
   at ~300px across.

## How it runs

`main.py` (Python 3.13, standard library only) copies the `entry.png` beside
it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). The image is a
JPEG (told apart by its first bytes, as the rules allow) in a file named
`entry.png`, 1024x683 pixels and under 1 MiB.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
