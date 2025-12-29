# Begrip – School Library API Lab

## Wat is het doel van dit lab?
Het doel van dit lab is begrijpen hoe een Python-script communiceert
met een externe applicatie via een API.

## Wat doet het script?
Het script stuurt HTTP-verzoeken (requests) naar een API om:
- boeken toe te voegen
- boeken te wijzigen
- boeken te verwijderen

## Waarom krijg ik een 401 Unauthorized?
De API vereist authenticatie via een API key.
De gebruikte sleutel is ongeldig of ontbreekt,
waardoor de API correct reageert met statuscode 401.

## Wat heb ik hieruit geleerd?
- Wat een API is en waarom authenticatie nodig is
- Wat HTTP statuscodes betekenen
- Dat een foutmelding ook een correct resultaat kan zijn
- Dat backend-communicatie vaak geen visuele output heeft

## Link met DevOps
Dit experiment toont hoe applicaties veilig met elkaar communiceren,
wat een basisconcept is binnen microservices en CI/CD pipelines.
