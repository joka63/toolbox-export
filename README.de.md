[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![de](https://img.shields.io/badge/lang-de-yellow.svg)](README.de.md)

Ich denke, dies ist eine der [am meisten gewünschten Toolbox-Funktionen](https://github.com/orgs/community/discussions/31132) und ein Grund, warum die Leute sowohl Distrobox als auch Home Isolation benutzen 
also wäre es gut, dies zum Laufen zu bringen. 
Diese Implementierung von Toolbox-export ist hauptsächlich eine Anpassung des distrobox-Shellskripts `distrobox-export` an toolbox.

Toolbox-export folgt dem von distrobox gewählten Ansatz. Ich schlage das folgende CLI vor:

```
# export firefox from "mytoolbox"
toolbox export --container mytoolbox  --app /usr/share/application/firefox.desktop 
# export ripgrep from "mytoolbox"
toolbox export --container mytoolbox --bin /usr/bin/rg
# remove ripgrep import
toolbox export --container mytoolbox --bin /usr/bin/rg --delete
```

---

[![how-to](https://img.shields.io/badge/how--to-use-blue.svg)](https://github.com/jonatasemidio/multilanguage-readme-pattern/blob/master/STEPS.md)
