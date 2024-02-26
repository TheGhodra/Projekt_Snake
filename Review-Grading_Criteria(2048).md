# Bewertung für das Projekt 2048

# Möglichkeiten zur Verbesserung:
- Wenn ich eine Taste drücke, zeigt es direkt an "Game Over!" und "Press Enter to Restart" an, wobei nichts passiert wenn ich Enter drücke, da das Spiel noch nicht verloren ist
- Wenn das Spiel tatsächlich verloren ist da ich mich nicht mehr bewegen kann, schließt es sich das spiel direkt, ohne dass vorher "Game Over!" und "Press Enter to Restart" angezeigt wird (Kann aber auch daran liegen, dass es über das angezeigt wird, dass die ganze Zeit da steht)
- Wenn ich andere Tasten drücke, die nicht die Pfeiltasten sind, spawnen neue Zahlenfelder.
- Manchmal wenn ich 2 Felder kombinieren möchte oder allgemein Felder verschiebe, verschwindet eines einfach, ohne dass sie addiert werden oder an dem Ort auftaucht an dem es nach dem Zug sein sollte.
- Manchmal wenn ich 2 Felder kombiniere werden Sie addiert, doch dann haben beide Felder die höhere Zahl und so geht das weiter, bis ich 2x 2048 habe
- Wenn ich 2048 gesammelt habe passiert nichts und wenn ich zwei 2048 Zahlenfelder kombiniere stürzt das Spiel ab
- das Start Menü (Z. 101 "def startMenu(self)") wird noch nicht angezeigt

# Grading Criteria, die wir bewerten können:

# FACHKOMPETENZ (40 Punkte)

## Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

### - Algorithmenbeschreibung (Vorhanden)
Sie haben Algorithmen benutzt um zu die verschiedenen Verschiebungen der Felder durch Eingabe von WASD zu erzeugen. In diesen Algorithmen steht auch noch, dass Felder kombiniert werden, wenn man sie ineinander schiebt und ihre Values die selben sind.

### - Datentypen (Vorhanden)
Sie haben verschiedene Datentypen benutzt. Beispielsweise Integers um die Positionen auf dem Feld darzustellen und boolische Werte um festzustellen, ob man sich noch bewegen kann

### - E/A-Operationen und Dateiverarbeitung (Vorhanden)
Sie haben E/A-Operationen durch die Pfeiltasten benutzt, um zu kontrollieren, in welche Richtung man sich bewegen möchte.

### - Operatoren (Vorhanden)
Sie haben mit vielen Vergleichsoperatoren wie '==', '>' oder '!=' in ihren if-Statements gearbeitet.
Außerdem haben Sie mit Zuweisungsoperatoren wie '=' und '+=' gearbeitet.

### - Kontrollstrukturen (Vorhanden)
Sie haben viel mit if Statements gearbeitet, z.B. für die Richtungseingabe. Außerdem haben sie for- und while-Schleifen benutzt, die z.B. dazu dienen, dass das Spiel solange läuft, bis es beendet wird.

### - Funktionen (Vorhanden)
Sie haben für fast jedes Menü oder jede Funktion des Programmes eine eigene Funktion erstellt, so gibt es eine, die feststellt, welche Taste gedrückt wurde ("def getKeyPressed()") oder eine, die das Spiel beendet und dafür sorgt, dass das Spielfeld geleert wird ("def endGame", die "def resetGame" aufruft).

### - Stringverarbeitung (Vorhanden)
Sie zeigen beispielsweise durch Strings einen Text "Game over!" und "Press Enter to Restart" an, wenn man verloren hat.

### - Strukturierte Datentypen (Vorhanden)
Sie benutzen Arrays als strukturierten Datentypen, um das Spielfeld als eine leere 4x4 Matrix zu erstellen. Außerdem nutzen sie noch ein dictionary um verschiedene Farben den verschiedenen Zahlenwerten zuzuordnen.

## Sie können die Syntax und Semantik von Python (10) (Vorhanden)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->
Es ist alles gut lesbar und es waren keine Syntaxfehler zu finden, dadurch läuft das Programm auch gut.


## Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10) (Vorhanden)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
Sie haben beide ungefähr gleichviel dem Projekt beigetragen. Das sieht man auch an den commits des Projektes.


## Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10) (Vorhanden)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->
Sie haben eine Liste benutzt um die einzelnen Felder des Spielfeldes darzustellen



# METHODENKOMPETENZ (10 Punkte) (Vorhanden)

## Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

Sie haben GitHub benutzt um miteinander zu arbeiten, dass sieht man auch an den verschiedenen Commits
