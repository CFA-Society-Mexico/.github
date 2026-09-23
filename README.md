# .github

Perfil y archivos de comunidad por defecto de la organización
[CFA Society México](https://github.com/CFA-Society-Mexico).

*Profile and default community files for the
[CFA Society México](https://github.com/CFA-Society-Mexico) organization.*

## Regenerar la cinta / Regenerate the ticker

Solo cuando cambian las palabras (`scripts/generate_ticker.py`).
*Only when the words change (`scripts/generate_ticker.py`).*

```bash
pip install -r scripts/requirements.txt
python scripts/generate_ticker.py
python -m pytest -q
```
