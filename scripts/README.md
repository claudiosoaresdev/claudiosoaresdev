# scripts

Geradores dos assets visuais do perfil (`docs/*.svg`).

O texto é convertido para *path* SVG a partir da **Orbitron Bold**, então o header e os
cards renderizam idênticos em qualquer lugar — GitHub não carrega webfonts dentro de `<img>`.

```bash
python3 -m venv venv && ./venv/bin/pip install fonttools
./venv/bin/python scripts/gen_header.py docs
./venv/bin/python scripts/gen_cards.py docs
```

`FONT` aponta para um `Orbitron-Bold.ttf` local ([SIL Open Font License](https://openfontlicense.org/),
disponível no [Google Fonts](https://fonts.google.com/specimen/Orbitron)). A fonte não é versionada aqui.

Paleta: `#0A0A0A` fundo · `#F2F2F0` texto · `#A9FE00` destaque · `#C9C7BB` apoio.
