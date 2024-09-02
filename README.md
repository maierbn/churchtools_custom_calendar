# Motivation
[ChurchTools](https://church.tools/de/startseite/) bietet einen rudimentären online Kalender an, der auch in eine Gemeindehomepage eingebunden werden kann. Die Möglichkeiten sind dabei jedoch sehr begrenzt. Zum Beispiel kann kein Bild angezeigt werden. Das Design ist weniger ansprechend als bei der Alternative amosWEB.

Dieses Projekt stellt nun einen Web-Kalender zur Verfügung, der die Termine aus einer [ChurchTools](https://church.tools/de/startseite/) Instanz lädt und mit ansprechender Formatierung darstellt. Der Kalender lässt sich dann einfach in einer Homepage einbinden. Das Aussehen ist an amosWEB angelehnt, sodass es visuell nur eine kleine Änderung ist.

Der Anwender kann die Formatierung sowie Filterung von Terminen anpassen. So können unterschiedliche Kalender-Ausgaben an verschiedenen Stellen auf der Homepage angelegt werden.

Für die Standard-Einstellungen, siehe [Demo](https://maierbn.github.io/churchtools_custom_calendar/index.html).

Die Termine werden immer zur vollen Stunde aus Churchtools aktualisiert. Die Aktualisierung geschieht durch eine Github Action. Es wird die aktuelle Ausgabe aus der API von churchtools als JSON-Datei heruntergeladen. :page_with_curl: Der Kalender ist mithilfe von Github Pages gehostet und stellt die Termine durch javascript-Code dar.

# Verwendung
:heavy_exclamation_mark: Achtung, dieser Code funktioniert nur für die Termine der [Evang. Kirchengemeinde Malmsheim](https://www.malmsheim-evangelisch.de). Anpassung für andere Gemeinde sind nach Absprache möglich (Repo forken und API endpoint anpassen :wrench:).

Der Kalender kann direkt über folgendes iframe auf der Website eingebunden werden:
```html
<iframe src="https://maierbn.github.io/churchtools_custom_calendar/index.html"></iframe>
```

Es sind auch einige Anpassungen möglich. Dafür können der URL Parameter übergeben werden. Im folgenden sind alle möglichen Parameter gesetzt:

```html
<iframe src="https://maierbn.github.io/churchtools_custom_calendar/index.html?number-max-entries=10&bg-color=#f9e3c8&primary-color=#557e76&regex-caption=.*&regex-calendar=.*&regex-text=.*"></iframe>
```

Es können jedoch auch Parameter weggelassen werden, dann werden die Standard-Werte verwendet.

Folgende Einstellungen sind möglich:

| Parameter | Standard-Wert | Beschreibung
| :--- | :--- | :--- |
| `number-max-entries` | 10 | Maximale Anzahl Termine die angezeigt werden, maximal bis ein Jahr im Voraus. |
| `bg-color` | `#f9e3c8` | Hintergrundfarbe |
| `primary-color` | `#557e76` | Schrift- and Rahmenfarbe |
| `regex-caption` | `.*` | Überschrift-Filter (als regulärer Ausdruck), zeigt nur entsprechende Termine an bei denen die Überschrift passt. |
| `regex-calendar` | `.*` | Kalendername-Filter (als regulärer Ausdruck), zeigt nur entsprechende Termine aus dem angegebenen Kalender an. |
| `regex-text` | `.*` | Allgemeiner Filter, zeigt nur entsprechende Termine an, bei denen entweder die Überschrift, die Beschreibung oder der Ortsname zum Filter passt. |

Die `regex-*` Variablen sind [reguläre Ausdrücke](https://www.regexe.de/hilfe.jsp). Die einfachste Verwendung ist jedoch als Filter, d.h. einfach ein Wort angeben, dass in dem Termin enthalten sein soll:

Beispiel:

* Nur Termine mit `Gottesdienst` im Titel: `regex-caption=Gottesdienst`
* Nur Termine die `Gemeindehaus` irgendwo in der Beschreibung haben: `regex-text=Gemeindehaus`
* Nur aus dem Kalender `Erwachsene`: `regex-calendar=Erwachsene`
 