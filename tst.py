import time
import sys


##ne sert à rien pour le moment

def blink_text(text, delay=0.5, num_blinks=5):
    for _ in range(num_blinks):
        sys.stdout.write(f"{text}\r")
        sys.stdout.flush()
        time.sleep(delay)

# Texte à clignoter
texte = "Patientez..."

# Effectuez le clignotement
blink_text(texte)



