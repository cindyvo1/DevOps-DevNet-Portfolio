# Pf2 – Password Evolution (Lab 6.5.10)


## Context & Doel
Dit experiment toont de evolutie van wachtwoordsystemen in webapplicaties.
We bouwen een Flask API die 2 methodes ondersteunt:

1. **v1 – Plain Text Passwords**
2. **v2 – Hashed Passwords (SHA256)**

Het doel is om te begrijpen waarom veilige wachtwoordopslag noodzakelijk is

## Deel 1 – Plain Text Passwords (v1)
Bij `v1` wordt het wachtwoord letterlijk in de database opgeslagen.

Voorbeeld:

| username | password        |
|---------|-----------------|
| alice   | myalicepassword |

### Probleem:
- wachtwoorden leesbaar in database
- geen bescherming bij datalek
- geen bescherming tegen insider threats
- geen standaard beveiliging

Conclusie: **onveilig**

---

## Deel 2 – Hashed Passwords (v2)
Bij `v2` wordt een **one-way cryptografische hash** gebruikt:
hash = SHA256(password)

Voorbeeld:

| username | hash |
|---|---|
| rick | 4d52f…e38 |

### Eigenschappen van hashing
- **one-way**: niet terug te berekenen
- **deterministisch**: zelfde input → zelfde output
- **compare-only**: bij login wordt hash vergeleken

Dit verhoogt de beveiliging aanzienlijk.

---

## Waarom hashing beter is
| Eigenschap | v1 Plain | v2 Hash |
|---|---|---|
| leesbaar in DB | ✔ | ✘ |
| werkt zonder decryptie | ✘ | ✔ |
| veilig bij datalek | ✘ | ✔ |
| standaard in industrie | ✘ | ✔ |

---

## Security Terminologie
- **Hashing** ≠ encryptie  
- Encryptie = terug omkeerbaar → hashing = niet omkeerbaar

---

## DevOps Relevantie
Dit lab illustreert dat DevOps engineers:

✓ webservices moeten kunnen testen  
✓ security best-practices moeten begrijpen  
✓ verkregen API's kunnen integreren  
✓ databanken kunnen aansturen via code  

---

## Pf2 Evaluation Mapping
Dit lab voldoet aan:

✔ Pf2 – Logon page experiment  
✔ Flask microservice  
✔ DB connectie (SQLite)  
✔ HTTP endpoints  
✔ Security concepts  



Flask webservice met:
- plaintext login (v1)
- hashed password login (v2)
- opslag in SQLite `test.db`

Endpoints:
- `GET /`                        → welkomstbericht
- `POST /signup/v1` + `/login/v1` → plaintext
- `POST /signup/v2` + `/login/v2` → hashed

Testen met curl:
- zie lab 6.5.10 opdrachten
