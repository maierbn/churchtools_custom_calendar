# Ziel
Dieses Projekt stellt einen Web-Kalender zur Verfügung, der Termine aus einer [ChurchTools](https://church.tools/de/startseite/) Instanz lädt und formatiert darstellt. Der Kalender lässt sich dann einfach in einer Homepage einbinden. 
Der Anwender kann die Formatierung sowie Filterung von Terminen anpassen.

Siehe [Demo](https://maierbn.github.io/churchtools_custom_calendar/index.html).

# Verwendung
Der Kalender kann direkt über folgendes iframe auf der Website eingebunden werden:
```html
<iframe src="https://maierbn.github.io/churchtools_custom_calendar/index.html">
```

Es sind auch einige Anpassungen möglich:

| Name | Standard-Wert | Beschreibung
| --- | --- | --- |
| `number-max-entries` | 10 | Maximale Anzahl Termine die angezeigt werden, maximal bis ein Jahr im Voraus. |
| `bg-color` | `#f9e3c8` | Hintergrundfarbe |
| `primary-color` | `#557e76` | Schrift- and Rahmenfarbe |

```html
<iframe src="https://maierbn.github.io/churchtools_custom_calendar/index.html?number-max-entries=10&bg-color=#f9e3c8&primary-color=#557e76&regex_caption=.*&regex_calendar=.*&regex_text=.*">
```