# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/861ac845-ccab-417b-a0df-bdd69c68fefe)

Wir haben für unser Snake Game viel mit Funktionen und Klassen gearbeitet, sodass alles strukturiert und geordnet dargestellt werden kann. Als Beispiel findet man in unserem Code einen Algorithmus, der dafür sorgt, dass Früchte random auf dem Spielfeld gespawnt werden. 

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/9460369e-730e-4c1f-a0e6-83395a25b32f)

Für die Darstellung des Körpers der Schlange haben wir beispielsweise Vektoren benutzt, um die jeweiligen Bilder der Körperteile an die richtige Stelle des Körpers zu positionieren. Je nachdem in welche Richtung sich die Schlange bewegt, wird die Grafik der Körperteile angepasst.

Für die prozedurale Programmierung existieren außerdem einige Funktionen in unserem Code, die wiederum auf die main-Class zurückgreifen. Das hat den Vorteil, dass man nicht nochmal zusätzlich in die play-Loop Code reinschreiben muss und man dadurch Zeit und Speicherplatz spart.   


# Sie können die Syntax und Semantik von Python (10)
![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/cec64aad-44aa-4dfb-bf2d-096515b05f02)
![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/2e115d8e-5e8d-47cc-b1d9-b7f0e4ab130a)

Diese Funktion wird in unserem dritten Level aufgerufen. Sie sorgt dafür, dass sich die Tastenkombination der Steuerung alle 10 Sekunden ändert. Damit das funktioniert, muss für die Steuerung wieder auf die main-Class zugegriffen werden, weil sich die Schlange sonst nicht bewegen könnte. Daraufhin folgen die if-Sätze, die festlegen in welche Richtung sich die Schlange bei der jeweiligen Taste bewegen soll. Wenn man sich in Level 1 und 2 befindet, passiert zunächst nichts und die Steuerung bleibt in ihrem ursprünglichen Zustand, aber wenn man in Level 3 ist, wird das Bild jede Sekunde 60 mal geupdatet und um einen Countdown von 10 Sekunden zu erhalten muss man diesen dann auf 600 festlegen. Nach Ablauf der 10 Sekunden wird dann die Tastenkombination umgekehrt und verhalten sich nun Spiegelverkehrt zum ursprünglichen Zustand.


# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

 Hier eine Auflistung, wer was programmiert hat:

Jonas:
- class Frucht
- def Kollisionen
- def Gras_Feld
- def play_upside_down
- def laden
- def unlock_screen
- def ton_aendern
- def reset_highscore (reset button)
- def unlock3
- class hindernisse
- def restart

Dennis:
- class Schlange
- def check_fail und def Tod
- def play
- def main_menu
- def options
- def skins
- def level
- def sterne
- Sprites und Hintergründe ausgesucht


# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/b98b8a5d-682b-43df-b116-21ec60ef7eb0)

Wir haben hauptsächlich auch als zusammengesetzte Datenstrukturen Listen mit Vektoren verwendet. Ein Beispiel hierfür findet man in "def random_hindernisse()". In dieser Funktion werden die Hindernisse random auf dem Spielfeld gespawnt, falls diese in der Schlange oder Frucht liegen werden sie erneut randomized. Danach wird der finale Wert der Liste zugeordnet, welche später auf den Bildschirm gezeichnet wird.

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/9bddbeb3-417b-4217-b17a-282054aee40b)

Außerdem haben wir primitive Datenstrukturen in Form von Strings, Integers, booleans verwendet. Die Funktion "def unlock_screen()" zeigt z.B. die Ausgabe von Text/Sätzen.

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/646033b7-b982-4ded-8e42-50a3aed21c08)

Integers haben wir fast überall in unserem Code verwendet. Diese sorgen dafür, dass man Objekte auf die richtige Position platzieren kann.

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/93c6cbad-f44b-4904-aeda-f24fe6c2e07f)
![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/96d5763c-dd50-477a-a1a7-2133150fb259)

Booleans haben wir in ist_ton_an (z.B. in "def ton_aendern()") um festzustellen ob der Ton an- oder ausgeschaltet ist.


## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/b735dbc1-34a5-4b0d-807d-36613ef151d3)
![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/ad3cb873-788a-403e-96f1-9fb72d426cd6)

Für unser Projekt haben wir mit Visual Studio Code gearbeitet. Um gemeinsam am Projekt arbeiten zu können, haben wir zusätzlich noch eine "Live Share"-Extension runtergeladen, sodass wir in der gleichen Datei jeweils unseren Code verfassen konnten. Uns hat die Live Share Extension ziemlich gut gefallen, da man sich so nicht in die Quere kommen konnte und man evtl. den Code der anderen Person verbessern, oder sich gegenseitig helfen konnte, falls es zu Problemen kam.

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/37d880d9-6a82-42d5-aa4c-f9d14f0d56f6)

Wenn wir mit unserem jeweiligen Code fertig waren, haben wir ihn in unser Repository committed.


## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)

Das Projekt war im Großen und Ganzen eine wirklich tolle Erfahrung, da wir eine Menge neuer Dinge wie z.B. Teamarbeit, Zeitmanagement, aber auch neue Kenntnisse in Python und im Programmieren erlangen konnten.

Gegenseitige Hilfe im Projekt war ein wichtiger Bestandteil, sodass man sein Wissen um einiges erweitern konnte.

Jonas half Dennis bei folgenden Dingen:
- Ich hatte anfangs Probleme, die Buttons in Pygame darzustellen bzw. erscheinen lassen zu können. Jonas hat mir dabei geholfen und gezeigt, wie man Buttons auch in der GUI darstellen lassen kann
- Jonas hat mir dabei geholfen meine Kenntnisse über Pygame zu erweitern, da er zuvor in seiner Schulzeit schon viel mit Python zu tun hatte. Somit konnte ich neu erlerntes auch für unser Projekt erfolgreich umsetzen
- Wenn ich mal an einem Punkt nicht weiterwusste hat mir Jonas immer geholfen und erklärt, wie ich was umsetzen kann

Dennis half Jonas bei folgenden Dingen:
- Ich wusste zu Beginn noch nicht wirklich wie ich ein Menü für unser Game kreieren konnte. Dennis hatte vor mir bereits unser Main Menü erstellt und hat mir mit diesem gezeigt, wie ich das Exit Menü designen und anpassen konnte. 
- Dennis hat mir dabei geholfen, den Ton richtig abspielen zu lassen, da ich Ton an und aus anfangs verkehrt herum zugeordnet habe, und deswegen der Ton bei "Ton aus" immer an war und bei "Ton an" immer aus. 

Generell konnten wir uns in dem Projekt viel gegenseitig unterstützen und ergänzen. Wenn jemand eine neue Idee oder Erweiterung für das Spiel vorgeschlagen hat, haben wir uns sofort hingesetzt und den Vorschlag in die Tat umgesetzt. Es hat sehr viel Spaß gemacht zu sehen, wie das Programm größer und größer wurde und wir sind sehr stolz auf das Ergebnis.

# Sie können existierenden Code analysieren und beurteilen. (5)

Wir haben das Projekt "2048" von Leonie und Carolina bewertet. 
Hier geht es zu unserer Grading Criteria für die Beiden:
https://github.com/TheGhodra/Projekt_Snake/wiki/Grading-Criteria-anderes-Projekt-(2048)

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
 
- Zur Einarbeitung in Pygame hatten wir und zuvor ein paar Videos und Tutorials angeschaut, wie genau man bei der Entwicklung eines Spieles vorgehen muss und was man zu beachten hat. Die Seite [W3Schools](https://www.w3schools.com/python/), die wir unter anderem auch in der Vorlesung kennengelernt hatten, hat uns dabei geholfen unter anderem Klassen und Funktionen zu erstellen. Auch wie man Maus- und Tastatureingaben implementieren kann, haben wir uns durch das Anschauen von verschiedenen Videos auf [YouTube](https://www.youtube.com/watch?v=Hujzny-gkEk) beibringen können. 

- Durch die Verwendung von Klassen, die für die Erstellung unserer Objekte dienen, konnten wir uns gut in das objektorientierte Programmieren einarbeiten und somit ein überschaubares Programm entwickeln.

- Wir haben in unserem Projekt viele interaktive Elemente wie beispielsweise Buttons, Tastatur- und Mauseingaben für die Benutzeroberfläche implementiert. Um diese mit einzubinden mussten wir uns erst einmal informieren, wie man solche interaktiven Technologien in Python mit einbinden kann.


## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

Welche Probleme gab es?
Zu Beginn hatten wir starke Probleme bei der Erstellung von Level 2, da hier Kakteen als Hindernisse hinzukamen und man stirbt, wenn man diese berührt. Das Schwierige daran war, dass die Kakteen immer wieder an der gleichen Position wie die Frucht gespawnt sind. Wir waren an dieser Stelle für einige Zeit ziemlich verzweifelt, weil wir ja eigentlich bereits definiert haben, dass die Kakteen nicht an der selben Stelle wie die Frucht platziert werden darf. Trotzdem haben wir uns dann nicht davon unterkriegen lassen und haben noch eine Lösung für das Problem gefunden. Unsere Lösung war dann, dass wir eine Fruchtliste erstellt haben, dann haben wir beim Start 2 Früchte generieren lassen, diese der Liste angehängt und immer beim Spawn einer Frucht die Frucht mit dem Index -2 spawnen lassen. Während die für den Index -1 immer gilt, dass diese nicht in den Kakteen spawnen kann.

Der oben beschriebene Code befindet sich in den Zeilen 178 (class frucht) bis 232 (class hindernisse) und in Zeile 280.

Bei der Implementation hatten wir ab und zu Klammern vergessen oder "=" statt "==". Beim Einfügen von Dateien wurde auch manchmal das falsche Format geschrieben. Funktionen wurden manchmal nicht aufgerufen und man wunderte sich warum das Programm nicht funktionierte :-)

Wie hat das Zeitmanagement geklappt?
Vom Zeitmanagement hat alles gut funktioniert. Meistens haben wir uns nach den Vorlesungen auf den Weg nach Hause gemacht und uns direkt online im Discord wieder getroffen, um unser Projekt zu erweitern. Wir haben, bevor wir mit dem Coden angefangen haben, ausgemacht wer was machen will und es dann genau so umgesetzt. Somit  wusste jeder was er zu tun hatte und es gab diesbezüglich nie irgendwelche Probleme oder Streitigkeiten. Durch die genaue Planung kamen wir recht zügig voran und konnten unser Projekt fristgerecht abschließen.

Auf was sind wir stolz?
Besonders stolz sind wir auf den Aufbau und die Funktion unseres Spiels. Man kann zwischen 2 verschiedenen Skins wählen und für die verschiedenen Level muss man jeweils 3 Sterne erreichen um das dritte Level freizuschalten. Das gibt dem Spiel letztendlich ein "Ziel", welches vom Spieler erreicht werden soll.  


## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/0b2fc252-1835-49b8-85eb-7cac600e9550)


# - Datentypen

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/0fa98a1a-0238-4b9a-839f-b0924ee8fe47)
![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/56af46cc-4cbb-44cf-a824-6e96d64441cf)


# - E/A-Operationen und Dateiverarbeitung

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/5a200196-d2e9-4ce7-8b25-6b9a7d8d9b19)


# - Operatoren

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/797716ef-0cba-4f87-8169-b8869372c1c1)


# - Kontrollstrukturen

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/31dd0bef-d6d4-49b0-b7c6-3646f1e0e95d)


# - Funktionen

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/80a0ea46-03fd-4fe6-98d5-b59b6eafc254)


# - Stringverarbeitung

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/3964ca2d-11be-434e-8912-5009b208fab6)


# - Strukturierte Datentypen

![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/567bebf4-faaf-491c-b100-07bf521126d6)
![image](https://github.com/TheGhodra/Code-Spaces-Jupyter/assets/152898751/1ad10069-3420-4dd7-b799-fda72d9b9a20)
