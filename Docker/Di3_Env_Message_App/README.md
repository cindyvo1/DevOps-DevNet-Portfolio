# Di3 – Eigen Docker Image 2 (Environment-configurable)

## Doel
Dit experiment bouwt verder op Di2, maar toont nu hoe je een Docker container
via **environment variables** kan configureren.

In plaats van een vaste boodschap, leest de applicatie de waarden van:
- `NAME`
- `ENVIRONMENT`

Zo kan hetzelfde image in verschillende omgevingen anders reageren (bv. dev/test/prod).

---


### `app.py`
Een kleine Python-applicatie die env vars uitleest:

```python
import os

name = os.environ.get("NAME", "DevOps student")
environment = os.environ.get("ENVIRONMENT", "local")
