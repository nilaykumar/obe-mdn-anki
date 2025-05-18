import fire
import polars as pl
import genanki as ga
from models import ReadModel, ReadDeck, SpeakDeck, SpeakModel
from utils import process_pinyin
import html


def main(vocab_file: str, output_apkg: str):
    """Generates an Anki deck from CSV vocab list.

    Arguments:
    vocab_file (str): Path to the CSV
    output_apkg (str): Path to the .apkg to be output
    """
    print("Loading models")
    read_model = ReadModel()
    speak_model = SpeakModel()
    read_deck = ReadDeck()
    speak_deck = SpeakDeck()

    df = pl.read_csv(vocab_file).fill_null("")
    print(f"Writing {len(df)} read and speak flash cards each")
    for row in df.iter_rows():
        si, tr, py, mn = row
        assert si != "", f"No simplified characters found for {row}"
        assert py != "", f"No pinyin found for {row}"
        assert mn != "", f"No meaning found for {row}"
        fields = [si, tr, process_pinyin(py), html.escape(mn), ("_ " * len(si)).strip()]
        read_note = ga.Note(read_model, fields=fields)
        read_deck.add_note(read_note)
        speak_note = ga.Note(speak_model, fields=fields)
        speak_deck.add_note(speak_note)

    pkg = ga.Package([read_deck, speak_deck])
    pkg.write_to_file(output_apkg)
    print("Done")


if __name__ == "__main__":
    fire.Fire(main)
