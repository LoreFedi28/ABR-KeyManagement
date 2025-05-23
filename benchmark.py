import time
import random

from abr_normale import ABR as ABRNormale
from abr_flag import ABR as ABRFlag
from abr_lista import ABR as ABRLista


def genera_dati(n, con_duplicati=False):
    dati = [random.randint(1, n // 2 if con_duplicati else 10 * n) for _ in range(n)]
    random.shuffle(dati)
    return dati


def misura_tempo(ABRClass, dati, n_test=100):
    abr = ABRClass()

    # Tempo di inserimento
    t0 = time.time()
    for valore in dati:
        abr.insert(valore)
    t1 = time.time()
    tempo_inserimento = t1 - t0

    # Tempo di ricerca
    chiavi_da_cercare = random.sample(dati, min(n_test, len(dati)))
    t0 = time.time()
    for chiave in chiavi_da_cercare:
        abr.cerca(chiave)
    t1 = time.time()
    tempo_ricerca = t1 - t0

    return tempo_inserimento, tempo_ricerca


def esegui_test():
    classi = [
        ("Normale", ABRNormale),
        ("Flag", ABRFlag),
        ("Lista", ABRLista)
    ]

    dimensioni = [1000, 5000, 10000, 50000]

    print(f"{'Implementazione':<10} | {'N':>6} | {'Inserimento (s)':>16} | {'Ricerca (s)':>12}")
    print("-" * 52)

    for nome, classe in classi:
        for N in dimensioni:
            dati = genera_dati(N, con_duplicati=True)
            tin, tric = misura_tempo(classe, dati)
            print(f"{nome:<14} | {N:6} | {tin:16.5f} | {tric:12.5f}")


if __name__ == "__main__":
    esegui_test()
