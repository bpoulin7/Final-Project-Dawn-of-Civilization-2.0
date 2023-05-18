

# troy     | hattusa | []        | MMM        | MMM       | MMM      | MMM    | WWW  | WWW
# apasa    | []      | meliddu   | MMM        | MMM       | MMM      | MMM    | WWW  | WWW
# lukka    | adana   | karkemish | washukanni | nineveh   | erbil    | MMM    | MMM  | MMM
# WWW      | ugarit  | emar      | tarqa      | ashur     | arrapkha | MMM    | MMM  | MMM
# WWW      | byblos  | palmyra   | ~~~        | kurigalzu | upi      | MMM    | MMM  | MMM
# WWW      | tyre    | ~~~       | ~~~        | sippar    | []       | MMM    | MMM  | MMM
# WWW      | ascalon | jericho   | ~~~        | babylon   | kish     | nippur | susa | warashi
#heliopolis| tjaru   | ~~~       | ~~~        | ~~~       | ~~~      | uruk   | WWW  | liyan
# memphis  | ~~~     | ~~~       | ~~~        | ~~~       | ~~~      | ur     | WWW  | anshan

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

class Mountains:
  """Mountain ranges impossible to traverse."""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.name = "mountains"
    self.desc = """ """

class Civilization:
  """A civilization that controls locations on the map."""
  def __init__(self, name, adjective, capx, capy):
    self.name = None
    self.adjective = None
    self.desc = None
    self.capx = None
    self.capy = None
  def __str__(self):
    return self.name

# Civilizations # ------------------------------------------------------------
trojans = Civilization("Troy", "Trojan", 0, 0)
hittites = Civilization("Hittite Empire", "Hittite", 1, 0)
arzawa = Civilization("Arzawa", "Arzawan", 0, 1)
mitanni = Civilization("Mitanni Empire", "Mitanni", 3, 2)
assyria = Civilization("Assyria", "Assyrian", 4, 3)
egypt = Civilization("Egypt", "Egyptian", 0, 8)
suteans = Civilization("Suteans", "Sutean", 3, 3)
babylonia = Civilization("Babylon", "Babylonian", 3, 4)
elamites = Civilization("Elam", "Elamite", 7, 6)

# Cities # -------------------------------------------------------------------
troy = Location(0, 0)
troy.name = "Troy"
troy.owner = trojans
troy.desc = "the legendary city-state on the Dardanelles Strait"

hattusa = Location(1, 0)
hattusa.name = "Hattusa"
hattusa.owner = hittites
hattusa.desc = "the great capital of the Hittite Empire"

apasa = Location(0, 1)
apasa.name = "Apasa"
apasa.owner = arzawa
apasa.desc = "an enigmatic city in Asia Minor"

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
karkemish.desc = "a legendary city on the upper ___ River"

washukanni = Location(3, 2)
washukanni.name = "Washukanni"
washukanni.owner = mitanni
washukanni.desc = "the capital of the Mitanni Empire"

nineveh = Location(4, 2)
nineveh.name = "Nineveh"
nineveh.owner = assyria
nineveh.desc = "an ancient city ..."

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
emar.desc = "???"

tarqa = Location(3, 3)
tarqa.name = "Tarqa"
tarqa.owner = suteans
tarqa.desc = "???"

ashur = Location(4, 3)
ashur.name = "Ashur"
ashur.owner = assyria
ashur.desc = "the capital of Assyria! Now you know that"

arrapkha = Location(5, 3)
arrapkha.name = "Arrapkha"
arrapkha.owner = assyria
arrapkha.desc = "???"

byblos = Location(1, 4)
byblos.name = "Byblos"
byblos.owner = egypt
byblos.desc = "???"

palmyra = Location(2, 4)
palmyra.name = "Palmyra"
palmyra.owner = egypt
palmyra.desc = "???"

kurigalzu = Location(3, 4)
kurigalzu.name = "Dur-Kurigalzu"
kurigalzu.owner = babylonia
kurigalzu.desc = "the newly-built capital of Babylonia under the Kassite dynasty"

upi = Location(4, 4)
upi.name = "Upi"
upi.owner = babylonia
upi.desc = "???"

tyre = Location(1, 5)
tyre.name = "Tyre"
tyre.owner = egypt
tyre.desc = "a Phoenician port city now under Egyptian control"

sippar = Location(4, 5)
sippar.name = "Sippar"
sippar.owner = babylonia
sippar.desc = "???"

ascalon = Location(1, 6)
ascalon.name = "Ascalon"
ascalon.owner = egypt
ascalon.desc = "???"

jericho = Location(2, 6)
jericho.name = "Jericho"
jericho.owner = egypt
jericho.desc = "perhaps the oldest city in the world, ???"

babylon = Location(4, 6)
babylon.name = "Babylon"
babylon.owner = babylonia
babylon.desc = "the legendary city, with its great walls ???"

kish = Location(5, 6)
kish.name = "Kish"
kish.owner = babylonia
kish.desc = "???"

nippur = Location(6, 6)
nippur.name = "Nippur"
nippur.owner = babylonia
nippur.desc = "???"

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
tjaru.name = "Tjaru"
tjaru.owner = egypt
tjaru.desc = "an Egyptian prisoner colony on the frontier of the Arabian Desert"

uruk = Location(6, 7)
uruk.name = "Uruk"
uruk.owner = babylonia
uruk.desc = "???"

liyan = Location(8, 7)
liyan.name = "Liyan"
liyan.owner = elamites
liyan.desc = "one of the few Elamite cities between Susa and Anshan"

memphis = Location(0, 8)
memphis.name = "Memphis"
memphis.owner = egypt
memphis.desc = "the seat of the ___th Dynasty of Egypt, ???"

ur = Location(6, 8)
ur.name = "Ur"
ur.owner = babylonia
ur.desc = "a Sumerian city on the coast of the flooded Persian Gulf"

anshan = Location(8, 8)
anshan.name = "Anshan"
anshan.owner = elamites
anshan.desc = "the southern of the two Elamite cities, perpetually suspicious of its northern competitor"