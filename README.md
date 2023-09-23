# Dibistan wiki colors generator

This script aims to generate a big CSS line to put in https://dibistan.fandom.com/fr/wiki/MediaWiki:Common.css so that the pages have custom accent colors.

## Usage

- Install the dependencies with `python -m pip install -r requirements.txt`
- Put your colors in the format `Page name: "#000000"` in `colors.yml`
- Execute `python .`

## This is ugly isn't it?

This is awful. However, as Fandom by default doesn't have the possibility of changing colors on a per-page basis, this is the only solution.
