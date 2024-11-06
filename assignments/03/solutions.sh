# Ausgabe der ersten drei Zeilen der Datei
head -n 3 "../shell-lessons/shell-lesson/exercise-data/2014-01_JA.tsv"

# Gesamtanzahl der Zeilen in jeder *.tsv-Datei zählen
wc -l "../shell-lessons/shell-lesson/exercise-data/"*.tsv

# Datei mit der meisten Zeilen finden
wc -l "../shell-lessons/shell-lesson/exercise-data/"*.tsv | sort -nr | head -n 1