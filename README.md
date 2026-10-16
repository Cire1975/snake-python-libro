# Snake in Python — gioco classico e sfida contro IA

Codice sorgente del progetto pratico del **Capitolo 7** del libro *Python per Principianti: Dalle Basi ai Giochi Intelligenti*.

Contiene due modalità giocabili con **Pygame**:

- **Snake classico** — guida il serpente, raccogli le mele e cerca di non morderti la coda.
- **Snake contro IA** — gareggia con un altro serpente che cerca la mela utilizzando l'algoritmo **A*** (A-star).

Il codice è organizzato in sei file `.py`, così è possibile leggere e modificare separatamente la logica del gioco, la mela, il serpente e l'intelligenza artificiale.

## Requisiti

- Python 3 (consigliato Python 3.10 o successivo)
- Pygame (vedi `requirements.txt`)
- Un computer Windows, macOS o Linux con una finestra grafica

## Scaricare il progetto

Apri il repository su GitHub, seleziona **Code → Download ZIP**, poi estrai lo ZIP in una cartella sul computer. Non è necessario avere Git installato.

## Installazione

Apri il terminale o prompt dei comandi **nella cartella dove si trovano i file `.py`**.

```bash
python -m pip install -r requirements.txt
```

Su Windows, se il comando `python` non è riconosciuto, prova `py` al suo posto. Su alcuni computer macOS o Linux il comando è `python3`.

## Avvio dei giochi

**Snake classico**:

```bash
python main.py
```

**Snake contro il computer**:

```bash
python main_ia.py
```

Se usi `py` o `python3` per installare Pygame, usa lo stesso comando per avviare i giochi.

## Comandi

- Frecce della tastiera oppure **W A S D**: cambia direzione del tuo Snake.
- **Esc**: esci dal gioco.
- È previsto anche il supporto di base per joypad compatibili, a seconda del sistema.

**Regole**: puoi attraversare i bordi dello schermo e riapparire dal lato opposto. La partita termina quando raggiungi il punteggio richiesto o avviene una collisione.

## Come regolare la velocità

Apri `config.py` e cerca:

```python
FPS = 5
```

Più il valore è basso, più lento sarà il movimento. Per iniziare si consiglia **5**; prova **3** per rallentare ulteriormente oppure **7** per aumentare la difficoltà.

Nello stesso file trovi `TARGET_SCORE`, il punteggio da raggiungere, e le dimensioni della griglia.

## Quale file contiene cosa?

| File | Funzione |
| --- | --- |
| `main.py` | Avvio e ciclo del gioco classico |
| `main_ia.py` | Avvio della sfida contro lo Snake IA |
| `snake.py` | Corpo, direzione, movimento, crescita e collisioni |
| `snake_ia.py` | Ricerca del percorso con A* e scelta del movimento |
| `apple.py` | Creazione della mela nelle celle libere |
| `config.py` | Dimensioni, colori, velocità e punteggio obiettivo |
| `requirements.txt` | Dipendenza da installare |

## Problemi comuni

**`ModuleNotFoundError: No module named 'pygame'`**: installa le dipendenze con il comando nella sezione *Installazione*, utilizzando lo stesso interprete Python con cui avvii il programma.

**La finestra si chiude subito**: apri un terminale nella cartella del progetto ed esegui il gioco da lì, così potrai leggere eventuali messaggi d'errore.

**Il gioco è troppo veloce**: riduci `FPS` in `config.py`.

## Nota sulla pubblicazione

Questo progetto accompagna un libro didattico. Prima di renderlo pubblico, l'autore deve scegliere e aggiungere un file `LICENSE` se desidera concedere esplicitamente diritti di utilizzo, modifica o ridistribuzione del codice. **Non è stata selezionata automaticamente una licenza.**
