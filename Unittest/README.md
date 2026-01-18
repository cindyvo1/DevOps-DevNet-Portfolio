# Python Unit Test Lab — Recursive JSON Search

Deze lab demonstreert hoe Python gebruikt kan worden om een JSON-structuur recursief te doorzoeken, en hoe het `unittest` framework gebruikt wordt om de functionaliteit automatisch te testen.

---

## Doel van de lab

De doelstellingen van deze lab zijn:

- begrijpen van **unit testing** in Python
- gebruik van het **unittest framework**
- werken met **recursie** in data parsing
- bug-fixing aan de hand van testresultaten
- schrijven van testbare code

---

## Gebruikte technologieën

- Python 3
- `unittest` standaardmodule
- JSON-achtige datastructuren
- Recursie

---

##  `test_data.py`

Bevat gesimuleerde JSON output van een API, inclusief nested dictionary en list structuren.  
Inclusief voorbeeldkeys `key1` (bestaat) en `key2` (bestaat niet) voor testscenario's.

---

##  `recursive_json_search.py`

Dit script implementeert:

- een functie `json_search(key, input_object)` die een JSON-object doorzoekt
- recursieve verwerking van zowel `dict` als `list`
- returnwaarde: een **lijst** van `{key: value}` matches

Initieel bevatte deze implementatie 2 bugs:

1. `ret_val` werd telkens herstart in recursieve calls
2. `ret_val` werd globaal en niet gereset tussen aanroepen

Beide problemen werden opgelost met een **inner function** en lokale scoping.

---
## `test_json_search.py`

Bevat unit tests die controleren of:

✔ een bestaande key wordt gevonden  
✔ een niet-bestaande key geen resultaten geeft  
✔ de returnwaarde van `json_search()` altijd een lijst is  

Voorbeeld testcases:

```python
self.assertTrue([] != json_search(key1, data))
self.assertTrue([] == json_search(key2, data))
self.assertIsInstance(json_search(key1, data), list)

## Runnen kan op twee manieren:

1. Direct:
python3 test_json_search.py

2. Via unittest test runner:
python3 -m unittest -v

## Na correcte implementatie geeft unittest:

----------------------------------------------------------------------
Ran 3 tests in ...s
OK

## Wat heb ik geleerd

Tijdens deze lab heb ik geleerd:

hoe unit tests geschreven en uitgevoerd worden in Python

hoe recursieve datastructuren werken in JSON

hoe bugs geïdentificeerd kunnen worden via test failures

waarom global state foutgedrag veroorzaakt

hoe inner functions gebruikt kunnen worden voor scoping control
