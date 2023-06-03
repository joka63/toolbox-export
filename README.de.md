[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![de](https://img.shields.io/badge/lang-de-yellow.svg)](README.de.md)

Toolbox-export ist ein kleines Projekt, dass eine kleine Lücke in [Fedoras Toolbox](https://docs.fedoraproject.org/en-US/fedora-silverblue/toolbox/) schließen will. 

Eine immer mal wieder  [nachgefragtes Toolbox-Feature](https://github.com/orgs/community/discussions/31132) ist der Export von Application-Startern. Dieses Mini-Projekt möchte das fehlende Feature bereitstellen.
 
Toolbox-export ist im Wesentlichen eine Anpassung des distrobox-Shellskripts `distrobox-export` an toolbox. Es übernimmt so weit wie möglich dessen Optionen und Aufrufsyntax.

## Beispiele:

### Export einer App:

```
toolbox-export --app texstudio
```

Dieses Kommando kopiert die Original .desktop-Dateien mit den nötigen Icons und fügt einen Prefix `toolbox run -c _Container-Name_ zum Starter hinzu und sichert die Dateien im Homeverzeichnis so, dass sie wie andere Apps z.B. von GNOME gefunden werden können.

### Export eines Binary:

```
toolbox-export --bin /usr/bin/gview --export-path $HOME/.local/bin
```

erzeugt einen Wrapper, der es ermöglicht, gview sowohl innerhalb als auch außerhalb des Toolbox-Containers zu starten. Die Option `--export-path` ist optional; die Wrapper werden nach `$HOME/.local/bin` installiert, wenn man die Option weglässt.

### Löschen exportierter App-Starter und Binary-Wrapper:

```
toolbox-export --app texstudio --delete
toolbox-export --bin /usr/bin/gview --export-path $HOME/.local/bin --delete
```

Den Export kann man rückgängig machen, indem man das gleiche Kommando mit der zusätzlichen Option `--delete` aufruft.

## Unterschiede zu distrobox-export

- Toolbox basiert (laut offizieller Dokumentation) ausschließlich auf rootless-Podman-Containern. Daher kann toolbox-export keine Optionen für privilegierte Container mit Root-Rechten unterstützen. Exportierte Binaries dürfen nicht von root oder mit sudo aufgerufen werden, das könnte den Toolbox-Container unbrauchbar machen! Die generierten Wrapper enthalten daher einen Check, der einen versehentlichen Aufruf als Root (vom Host aus) blockiert:

- ```
$ sudo ~/.local/bin/gview /etc/passwd
You must not run  gview as root in a toolbox container!
```


- Im Gegensatz zu `distrobox-export` wird `toolbox-export` auf dem Host und nicht in den Containern aufgerufen, daher gibt es noch eine zusätzliche Option `--container` oder kurz `-c`, zum Beispiel:

- ```
# export firefox from "mytoolbox"
toolbox-export --container mytoolbox --app /usr/share/application/firefox.desktop 
# export ripgrep from "mytoolbox"
toolbox-export -c mytoolbox --bin /usr/bin/rg
# remove ripgrep import
toolbox-export --container mytoolbox --bin /usr/bin/rg --delete
```



## Installation

toolbox-export wurde auf und für Fedora Silverblue 38 entwickelt und getestet. Auf anderen Linux-Distributionen, die toolbox (bzw. podman-toolbox) unterstützen, sind wahrscheinlich noch Anpassungen erforderlich.

### Abhängigkeiten

- coreutils
- toolbox
- make
- asciidoctor

### Installation per git clone:

```
git clone https://github.com/joka63/toolbox-export
cd toolbox-export
make
PREFIX=~/.local make install 	
```

### Manuelle Installation

Einfach das Shell-Skript [toolbox-export](toolbox-export) in ein beliebiges Verzeichnis in PATH kopieren, ich empfehle `$HOME/.local/bin`.

## Manpage

[toolbox-export(1)](doc/toolbox-export.1.asciidoc)

## Lizenz

**Toolbox-export** ist freie Software, verfügbar unter der [GNU General Public License, Version 3](https://www.gnu.org/licenses/gpl.html).
