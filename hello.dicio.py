
"""Hello world multi linguas.

Dependendo da lingua configurada no ambiente o programa
exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

  export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__="0.0.1"
__author__="David Bengui"
__licence__="unlicense"

import os 

current_language = os.getenv("LANG", "en_US")[:5]


msg = {
    "en_US": "Hello, World",
    "pt_BR": "Ola, Mundo",
    "it_IT": "Ciao, Mondo",
    "fr_FR": "Bonjour, Monde",

    }

# O(1) - constante
print (msg[current_language])

