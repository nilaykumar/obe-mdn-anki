# OBE MDN 101: Anki flashcard deck

The list of vocabulary words is stored in [this
spreadsheet](https://docs.google.com/spreadsheets/d/1gymnnzxc6ZOckzV_hwzx9SG2Yco3EqO4AGoxr7ir0AQ/edit?usp=sharing).
I will try to keep it up-to-date, but contributors are welcome. Note that the
pinyin need not be already typeset (the number format should suffice).

The Anki deck can be found
[here](https://github.com/nilaykumar/obe-mdn-anki/raw/refs/heads/main/obe-mdn-101.apkg)
(this is just a link to the `.apkg` file found at the root of the repository).

The code in this repository generates the Anki deck from (a CSV export of) the
spreadsheet linked above.

## Flashcards

The structure and styling of the flashcards is adapted from the popular HSK
decks here: https://ankiweb.net/shared/info/1598233731.

Each vocabulary term corresponds to two cards: a `read` card and a `speak` card.
The `read` card consists of written Mandarin to be read (reading and meaning),
while the `speak` card consists of English to be translated into Mandarin.

## Usage

Clone the repo and install the dependencies. If using `uv`, for instance:
```sh
uv sync
```

Then, generate the Anki deck `output.apkg` from an input `data-file.csv` using:
```sh
uv run obe_mdn_anki/generate_deck.py data-file.csv output.apkg
```
