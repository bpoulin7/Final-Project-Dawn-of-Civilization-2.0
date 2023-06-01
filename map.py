

class Location:
  """A place around the map."""
  def __init__(self, x, y):
    self.x = 0
    self.y = 0
    self.name = None
    self.owner = None
    self.desc = None
  def __str__(self):
    return self.name

class Mountains(Location):
  """Mountain ranges impossible to traverse."""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.name = "mountains"


class Desert(Location):
    """Deserts that hinder travel."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "desert"


class Sea(Location):
    """The sea, impossible to traverse."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "sea"


class Civilization:
  """A civilization that controls locations on the map."""
  def __init__(self, name, adjective, prestige):
    self.name = name
    self.adjective = adjective
    self.desc = None
    self.prestige = prestige
  def __str__(self):
    return self.name

# Civilizations # ------------------------------------------------------------
trojans = Civilization("Troy", "Trojan", 5)
trojans.desc = """the strategically-located city-state that would go on to
                  fight the Greeks in the legendary Trojan War."""
hittites = Civilization("Hittite Empire", "Hittite", 25)
hittites.desc = """the first great empire of Anatolia, increasing in power
                   by the decade."""
arzawa = Civilization("Arzawa", "Arzawan", 0)
arzawa.desc = """a basically unknown federation on the western coast of
                 Anatolia, allied with the Ancient Greeks."""
mitanni = Civilization("Mitanni Empire", "Mitanni", 25)
mitanni.desc = """a young empire in Upper Mesopotamia, """
assyria = Civilization("Assyria", "Assyrian", 25)
assyria.desc = """the northern rival of Babylonia, and one of the most
                  successful empires in history so far."""
egypt = Civilization("Egypt", "Egyptian", 50)
egypt.desc = """the New Kingdom era of the famous civilization along the
                Nile River, whose sphere of influence now spreads north
                along the Levantine coast."""
suteans = Civilization("Suteans", "Sutean", 0)
suteans.desc = """a decentralized, nomadic culture found in the now-abandoned
                  cities of the Arabian Desert."""
babylonia = Civilization("Babylon", "Babylonian", 25)
babylonia.desc = """the southern rival of Assyria, centered around the
                    legendary city of Babylon."""
sumer = Civilization("Sumer", "Sumerian", 15)
sumer.desc = """the oldest civilization in the world, located at the mouth
                of Mesopotamia."""
elamites = Civilization("Elam", "Elamite", 15)
elamites.desc = """the easternmost polity in Mesopotamian civilization,
                   protected by the Zagros Mts. and the Persian Gulf."""

# Cities # -------------------------------------------------------------------
troy = Location(0, 0)
troy.name = "Troy"
troy.owner = trojans
troy.desc = "the legendary city-state on the Dardanelles Strait"

hattusa = Location(1, 0)
hattusa.name = "Hattusa"
hattusa.owner = hittites
hattusa.desc = "the ancient capital of the Hittite Empire"

samuha = Location(2, 0)
samuha.name = "Samuha"
samuha.owner = hittites
samuha.desc = "the secondary capital of the Hittite Empire"

apasa = Location(0, 1)
apasa.name = "Apasa"
apasa.owner = arzawa
apasa.desc = "an enigmatic city in Asia Minor"

kummanni = Location(1, 1)
kummanni.name = "Kummanni"
kummanni.owner = hittites
kummanni.desc = "an insignificant region of central Anatolia"

meliddu = Location(2, 1)
meliddu.name = "Meliddu"
meliddu.owner = hittites
meliddu.desc = "an ancient city on the edge of Hittite sphere of influence"

lukka = Location(0, 2)
lukka.name = "Lukka"
lukka.owner = arzawa
lukka.desc = "now an insignificant corner of Anatolia, soon to be a major kingdom of its own"

adana = Location(1, 2)
adana.name = "Adana"
adana.owner = hittites
adana.desc = "one of the oldest continuously-inhabited cities in Anatolia"

karkemish = Location(2, 2)
karkemish.name = "Karkemish"
karkemish.owner = mitanni
karkemish.desc = "a legendary city on the upper Euphrates River"

washukanni = Location(3, 2)
washukanni.name = "Washukanni"
washukanni.owner = mitanni
washukanni.desc = "the capital of the Mitanni Empire"

nineveh = Location(4, 2)
nineveh.name = "Nineveh"
nineveh.owner = assyria
nineveh.desc = "an ancient and legendary city on the upper Tigris River"

erbil = Location(5, 2)
erbil.name = "Erbil"
erbil.owner = assyria
erbil.desc = "an enigmatic city on the edge of civilization"

ugarit = Location(1, 3)
ugarit.name = "Ugarit"
ugarit.owner = egypt
ugarit.desc = "a port city that once had its own empire, now under Egyptian control"

emar = Location(2, 3)
emar.name = "Emar"
emar.owner = mitanni
emar.desc = "a crucial Bronze Age trade hub at the crossroads of civilization"

tarqa = Location(3, 3)
tarqa.name = "Tarqa"
tarqa.owner = suteans
tarqa.desc = "a small city bridging the Levant to Mesopotamia"

ashur = Location(4, 3)
ashur.name = "Ashur"
ashur.owner = assyria
ashur.desc = "the capital of Assyria! Now you know that"

arrapkha = Location(5, 3)
arrapkha.name = "Arrapkha"
arrapkha.owner = assyria
arrapkha.desc = "an Assyrian city on the edge of the civilized world"

byblos = Location(1, 4)
byblos.name = "Byblos"
byblos.owner = egypt
byblos.desc = "a Phoenician trading port on the Mediterranean coast"

palmyra = Location(2, 4)
palmyra.name = "Palmyra"
palmyra.owner = egypt
palmyra.desc = "one of the few significant settlements in the Arabian desert"

kurigalzu = Location(3, 4)
kurigalzu.name = "Dur-Kurigalzu"
kurigalzu.owner = babylonia
kurigalzu.desc = "the newly-built capital of Babylonia under the Kassite dynasty"

eshnunna = Location(4, 4)
eshnunna.name = "Eshnunna"
eshnunna.owner = babylonia
eshnunna.desc = "a border city between Assyria and Babylon"

tyre = Location(1, 5)
tyre.name = "Tyre"
tyre.owner = egypt
tyre.desc = "a Phoenician port city now under Egyptian control"

sippar = Location(4, 5)
sippar.name = "Sippar"
sippar.owner = babylonia
sippar.desc = "an important wool-producing city in Mesopotamia"

upi = Location(5, 5)
upi.name = "Upi"
upi.owner = babylonia
upi.desc = "an elusive and insignificant Babylonian settlement"

ascalon = Location(1, 6)
ascalon.name = "Ascalon"
ascalon.owner = egypt
ascalon.desc = "the only major south Levantine port"

jericho = Location(2, 6)
jericho.name = "Jericho"
jericho.owner = egypt
jericho.desc = "the oldest city in the world, with magnificent protective walls"

babylon = Location(4, 6)
babylon.name = "Babylon"
babylon.owner = babylonia
babylon.desc = "the legendary city, currently the most populous in the world"

kish = Location(5, 6)
kish.name = "Kish"
kish.owner = babylonia
kish.desc = "a symbolically important city with ties to the rise of Sumer"

nippur = Location(6, 6)
nippur.name = "Nippur"
nippur.owner = babylonia
nippur.desc = "a strategically important city disputed between Babylonian and Sumerian control"

susa = Location(7, 6)
susa.name = "Susa"
susa.owner = elamites
susa.desc = "the northern of the two Elamite cities, considered an imposter by its southern competitor"

warashi = Location(8, 6)
warashi.name = "Warahshi"
warashi.owner = elamites
warashi.desc = "an enigmatic region on the eastern edge of civilization, perhaps connected to Central Asia"

heliopolis = Location(0, 7)
heliopolis.name = "Heliopolis"
heliopolis.owner = egypt
heliopolis.desc = "the future sight of Cairo, a magnificent city at the head of the Nile Delta"

tjaru = Location(1, 7)
tjaru.name = "Avaris"
tjaru.owner = egypt
tjaru.desc = "a crucial trade city on the lower Nile"

uruk = Location(6, 7)
uruk.name = "Uruk"
uruk.owner = sumer
uruk.desc = "the most important city in Sumerian history"

liyan = Location(8, 7)
liyan.name = "Liyan"
liyan.owner = elamites
liyan.desc = "one of the few Elamite cities between Susa and Anshan"

memphis = Location(0, 8)
memphis.name = "Memphis"
memphis.owner = egypt
memphis.desc = "the seat of the Pharaoh of Egypt, and one of the most important cities in the world"

ur = Location(6, 8)
ur.name = "Ur"
ur.owner = sumer
ur.desc = "a Sumerian city on the coast of the flooded Persian Gulf"

anshan = Location(8, 8)
anshan.name = "Anshan"
anshan.owner = elamites
anshan.desc = "the southern of the two Elamite cities, perpetually suspicious of its northern competitor"

map_tiles = [
    [troy, hattusa, samuha, Mountains(3, 0), Mountains(4, 0), Mountains(5, 0),
     Mountains(6, 0), Sea(7, 0), Sea(8, 0)],
    [apasa, kummanni, meliddu, Mountains(3, 1), Mountains(4, 1), Mountains(5, 1),
     Mountains(6, 1), Sea(7, 1), Sea(8, 1)],
    [lukka, adana, karkemish, washukanni, nineveh, erbil, Mountains(6, 2),
     Mountains(7, 2), Mountains(8, 2)],
    [Sea(0, 3), ugarit, emar, tarqa, ashur, arrapkha, Mountains(6, 3),
     Mountains(7, 3), Mountains(8, 3)],
    [Sea(0, 4), byblos, palmyra, Desert(3, 4), kurigalzu, eshnunna, Mountains(6, 4),
     Mountains(7, 4), Mountains(8, 4)],
    [Sea(0, 5), tyre, Desert(2, 5), Desert(3, 5), sippar, upi, Mountains(6, 5),
     Mountains(7, 5), Mountains(8, 5)],
    [Sea(0, 6), ascalon, jericho, Desert(3, 6), babylon, kish, nippur, susa,
     warashi],
    [heliopolis, tjaru, Desert(2, 7), Desert(3, 7), Desert(4, 7), Desert(5, 7),
     uruk, Sea(7, 7), liyan],
    [memphis, Desert(1, 8), Desert(2, 8), Desert(3, 8), Desert(4, 8),
     Desert(5, 8), ur, Sea(7, 8), anshan]
]

def location(x, y):
    """Funtion to return map location at a given coordinate."""
    if x < 0 or y < 0:
        return None
    try:
        return map_tiles[y][x]
    except IndexError:
        return None