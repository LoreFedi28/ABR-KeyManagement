from abr_normale import ABR as ABRNormale
from abr_flag import ABR as ABRFlag
from abr_lista import ABR as ABRLista

def test_abr_normale():
    abr = ABRNormale()
    chiavi = [10, 5, 15, 3, 7, 12, 18, 5, 10]
    for c in chiavi:
        abr.insert(c)
    risultato = abr.in_ordine()
    assert risultato == [3, 5, 7, 10, 12, 15, 18], f"ABR normale: risultato errato {risultato}"
    assert abr.cerca(7)
    assert not abr.cerca(4)
    print("Test ABR normale superato")

def test_abr_flag():
    abr = ABRFlag()
    chiavi = [10, 5, 15, 3, 7, 12, 18, 5, 10]
    for c in chiavi:
        abr.insert(c)
    risultato = abr.in_ordine()
    attesi = {
        3: False,
        5: True,
        7: False,
        10: True,
        12: False,
        15: False,
        18: False,
    }
    for chiave, duplicato in risultato:
        assert attesi[chiave] == duplicato, f"ABR flag: errore su {chiave} (atteso duplicato={attesi[chiave]})"
    assert abr.cerca(15)
    assert not abr.cerca(4)
    print("Test ABR con flag superato")

def test_abr_lista():
    abr = ABRLista()
    chiavi = [10, 5, 15, 3, 7, 12, 18, 5, 10, 10]
    for c in chiavi:
        abr.insert(c)
    risultato = abr.in_ordine()
    attesi = {
        3: 1,
        5: 2,
        7: 1,
        10: 3,
        12: 1,
        15: 1,
        18: 1,
    }
    for chiave, occorrenze in risultato:
        assert attesi[chiave] == occorrenze, f"ABR lista: errore su {chiave} (attese occorrenze={attesi[chiave]}, trovate={occorrenze})"
    assert abr.cerca(5)
    assert not abr.cerca(999)
    print("Test ABR con lista superato")

if __name__ == "__main__":
    print("Esecuzione test unificati:\n")
    test_abr_normale()
    test_abr_flag()
    test_abr_lista()
