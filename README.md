# NettverkArbeidskrav4: Ansible og Python Script som setter opp SSH mulighet og config på cisco nettverksutstyr

Python Script som setter opp SSH tilkobling til cisco nettverksutstyr og Ansible Script som setter opp config på Nettverksutstyr

## Struktur

- **`sshsetup.py`**: Python script til å sette opp SSH
- **`L3Switch.yml`**: Ansible script til å sette opp config på Lag 3 Switch
- **`ruter.yml`**:  Ansible script til å sette opp config på Ruter
- **`ruter2.yml`**:  Ansible script til å sette opp config på Ruter
- **`switchnord.yml`**:  Ansible script til å sette opp config på Øvre Lag 2 Switch
- **`switchsør.yml`**:  Ansible script til å sette opp config på Nedre Lag 2 Switch
- **`variables.yaml`**: Definerer variabler

## Instruksjoner for oppsett

### Forutsetninger
- Tilgang til en linux maskin/WSL og Korrekt nettverksutstyr
- Installert Python3 og Ansible på Linux

### Nedlasting og bruk

1. **Nedlasting og klargjøring**:
- Last ned fra Github direkte eller bruk git pull kommando
- Koble sammen datamaskin og nettverksutstyr ved bruk av cisco konsoll kabel
2. **Kjøre script**
- Vi starter med og kjøre python script på Lag 3 Switchen
- ![Hvordan kjøre python script](https://github.com/user-attachments/assets/35e13b88-8b49-47c1-a5d5-8b79ed255e09)
- Når Scriptet har blitt kjørt skal du velge COM port som scriptet skal bli kjørt på. Denne er basert på hvilken du nå er koblet til Lag 3 Switchen med i mitt eksempel er der COM5 eller som du må da skrive det /dev/ttyS5
- ![Hvilken COMport skal du bruke](https://github.com/user-attachments/assets/1a4e6d57-85a8-48e0-a2e4-dec1bafd4129)


