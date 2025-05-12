import genanki as ga

# the note fields are shared between the read and speak models
FIELDS = [
    {"name": "simplified"},
    {"name": "traditional"},
    {"name": "pinyin"},
    {"name": "meaning"},
    {"name": "silhouette"},
]


class ReadModel(ga.Model):
    MODEL_ID = 1737305106
    NAME = "OBE MDN Read"
    TEMPLATE_FILE = "templates/read.yaml"
    STYLE_FILE = "templates/style.css"

    def __init__(self):
        with open(ReadModel.TEMPLATE_FILE, "r") as tmpl_f:
            templates = tmpl_f.read()
        with open(ReadModel.STYLE_FILE, "r") as style_f:
            css = style_f.read()
        super().__init__(
            ReadModel.MODEL_ID,
            ReadModel.NAME,
            fields=FIELDS,
            templates=templates,
            css=css,
        )


class SpeakModel(ga.Model):
    MODEL_ID = 1898816446
    NAME = "OBE MDN Speak"
    TEMPLATE_FILE = "templates/speak.yaml"
    STYLE_FILE = "templates/style.css"

    def __init__(self):
        with open(SpeakModel.TEMPLATE_FILE, "r") as tmpl_f:
            templates = tmpl_f.read()
        with open(SpeakModel.STYLE_FILE, "r") as style_f:
            css = style_f.read()
        super().__init__(
            SpeakModel.MODEL_ID,
            SpeakModel.NAME,
            fields=FIELDS,
            templates=templates,
            css=css,
        )


class ReadDeck(ga.Deck):
    DECK_ID = 1873878201
    NAME = "OBE MDN::OBE MDN 101::Read"

    def __init__(self):
        super().__init__(ReadDeck.DECK_ID, ReadDeck.NAME)


class SpeakDeck(ga.Deck):
    DECK_ID = 1842445030
    NAME = "OBE MDN::OBE MDN 101::Speak"

    def __init__(self):
        super().__init__(SpeakDeck.DECK_ID, SpeakDeck.NAME)
