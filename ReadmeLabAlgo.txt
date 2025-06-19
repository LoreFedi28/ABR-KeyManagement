Fedi, Lorenzo, 7075327

Esercizio:
Vogliamo confrontare tre approcci alternativi per gestire chiavi duplicate all’interno di un Albero Binario di Ricerca (ABR):
– implementazione “normale”, che ignora i duplicati
– utilizzo di un flag booleano per segnalare la presenza di un duplicato
– utilizzo di una lista di valori associata alla stessa chiave

Per fare questo dovremo:
– Scrivere i programmi Python che implementano le tre versioni di ABR
– Progettare ed eseguire un insieme di test e benchmark per confrontare le strategie
– Misurare e confrontare i tempi di inserimento e ricerca per insiemi di dati con chiavi duplicate
– Redigere una relazione che descriva le scelte progettuali, i risultati sperimentali e un’analisi critica delle strategie adottate

------------------------------------------------

ISTRUZIONI PER L’ESECUZIONE

1. Requisiti:
- Python 3.10 o superiore
- I seguenti pacchetti devono essere installati nel virtual environment:
    - matplotlib
    - statistics (già incluso nella libreria standard)

2. File principali:
- `abr_normal.py`: implementazione ABR normale
- `abr_flag.py`: implementazione con flag booleano
- `abr_list.py`: implementazione con lista di occorrenze
- `benchmark.py`: script principale per generare i risultati
- `test_abr.py`: contiene i test unitari

3. Per eseguire il programma principale ed ottenere i risultati:

Aprire un terminale nella directory del progetto e lanciare:

```bash
python benchmark.py
