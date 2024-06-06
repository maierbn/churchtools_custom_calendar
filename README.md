# Ziel
Dieses Projekt stellt einen Web-Kalender zur Verfügung, der Termine aus einer [ChurchTools](https://church.tools/de/startseite/) Instanz lädt und formatiert darstellt. Der Kalender lässt sich dann einfach in einer Homepage einbinden. 
Der Anwender kann die Formatierung sowie Filterung von Terminen anpassen.

Siehe [Demo](https://maierbn.github.io/churchtools_custom_calendar/index.html).

# Verwendung
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

