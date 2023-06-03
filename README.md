[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![de](https://img.shields.io/badge/lang-de-yellow.svg)](README.de.md)

I think this is one of the [most requested toolbox features](https://github.com/orgs/community/discussions/31132) and reasons why people use distrobox as well as home isolation 
so it would be good to get this going. 
This implementation of Toolbox-export is mainly an adaptation of the distrobox shell script `distrobox-export` to toolbox.

Toolbox-export follows the approach taken by distrobox. I propose the following CLI:

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
