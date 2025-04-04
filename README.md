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
- Jeg vill påpeke at dette oppsettet går ut på å først sette opp SSH mulighet på en enhet for å så kjøre ansible script på samme enhet før man går videre til neste enhet. Oppsettet starter øverst med Lag 3 switchen og går nedover til Lag 2 switchen med Etherchanneling.
2.1 Vi starter med og kjøre python script på Lag 3 Switchen
- ![Hvordan kjøre python script](https://github.com/user-attachments/assets/35e13b88-8b49-47c1-a5d5-8b79ed255e09)

2.2 Når Scriptet har blitt kjørt skal du velge COM port som scriptet skal bli kjørt på. Denne er basert på hvilken du nå er koblet til Lag 3 Switchen med i mitt eksempel er der COM5 eller som du må da skrive det /dev/ttyS5
- ![Hvilken COMport skal du bruke](https://github.com/user-attachments/assets/1a4e6d57-85a8-48e0-a2e4-dec1bafd4129)
  
2.3 Neste steget er å velge Baud Rate som er hastigheten på tilkoblingen via konsoll kabel. Her velger jeg 9600
- ![Hvilken Baud rate](https://github.com/user-attachments/assets/e61979a1-0cb9-4072-96d5-69727475d087)

2.4 Nå skal det settes et brukernavn og passord for ssh tilkobling. Her er viktig at du bruker **cisco** til begge siden ansible hosts filen bruker dette til ssh
- ![Brukernavn og Passord til ssh tilkobling](https://github.com/user-attachments/assets/97dd6f1b-c29e-4d4a-a334-865dd9bca79d)

2.5 Når du skal velge et interface som skal få IP slik at du kan SSH inn spørs det på om du setter opp Switch eller Ruter. Siden denne switchen skal bli ruter senere bruker jeg nå vlan 1 for dette steget
- ![Switch VLAN interface](https://github.com/user-attachments/assets/5c020107-2455-41f0-bdf3-570fe9c93db3)

2.6 Hostname for nettverksutstyr kan du velge helt selv her bruker jeg en definisjon av slags utstyr det er og M på slutten for mitt navn 
- ![Hostname for switch](https://github.com/user-attachments/assets/d22f153c-7e22-47f6-86fe-652f7028c270)

2.7 Når det kommer til å sette en IP adresser bruker jeg en adresse som ikke skal brukes senere i oppsettet og er del av et helt annet nettverk hvis du ikke vil redigere i hostsfilen er det best å bruke samme adresse som meg.
- ![Temp IP for L3 switch + subnetmaske](https://github.com/user-attachments/assets/883d724e-b202-46db-aaa0-4633614601d2)
- Til slutt kommer scriptet til å Spørre deg hva slags utstyr som blir satt opp her er blir **Switch/switch** og **Ruter/ruter/Router/router** akseptert av scriptet til å jobbe videre på konfigurasjonen
2.8 Når den spør deg her kan du ta hvilken som helst port for dette uten gig1/0/1-3 siden de brukes senere i ansible scriptet. Jeg valgte å bruke gig1/0/7 med VLAN ID 1 som er samme som du satt som interface tidligere i scriptet her setter jeg også switchport mode trunk.
- ![Unik config for Switch](https://github.com/user-attachments/assets/5594a26d-b263-425b-8827-8f1a2a5a7ab0)

2.9 Hvis SSH scriptet ikke møtte på noen tilkoblingsproblemer skal du se dette
- ![Succesfull ssh config](https://github.com/user-attachments/assets/7358f941-ff71-46e7-9f34-2a6d4e9a1680)

2.10 For å SSH inn på Lag 3 Switchen må du endre IP adressen til datamaskinen din
- ![IP config for L3 SSH tilkobling](https://github.com/user-attachments/assets/707f5048-b0a8-4c80-9e0f-22daab236f08)

2.11 Når du skal kjøre ansible scriptene bruker du ansible-playbook **navnet til ansible script** -K
- ![L3Switch ansible script](https://github.com/user-attachments/assets/47564226-e38e-4299-90b4-a7154fbd5f21)

2.12 Etter Ansible scriptet har blitt kjørt på Lag 3 switchen kan du endre IP adressen på datamaskinen din for siste gang
- ![IP config for resten av oppsettet](https://github.com/user-attachments/assets/f7cde40c-2224-404e-9858-574825fd666b)

2.13 Når du skal sette opp SSH på ruterene er det du skal inputte i python scriptet for det meste likt. De viktigste tingene å peke ut som forskjellig er at når du skal velge interface så skriver du et standard interface som i mitt eksempel er gig0/0/0 og at når du blir spurt hva slags utstyr du skal konfigurere skriver du ruter.
- ![Full ssh ruter config](https://github.com/user-attachments/assets/4a2dff2d-dc3c-4389-b041-585887522a7a)

2.14 Når du har skrevet ruter som utstyrs type ber den deg lage en static route slik at du kan ssh inn ved å gå gjennom lag 3 switchen. Her bruker du Nett-ID til Switchen som ble satt opp i ansible scriptet.
- ![Static IP Route](https://github.com/user-attachments/assets/158a2c63-2f0e-4920-bcea-79720a531ab9)

2.15 For ruter 2 er det veldig likt oppsett men med forskjellige IP adresser
- ![Full ssh ruter2 config](https://github.com/user-attachments/assets/ff1b121c-a9ba-4c86-a2b0-bf0fd68641cc)
- For de to switchene er det også veldig likt oppsett viktigste å påpeke her er at du må kjøre ansible script switchnord.yml før du kjører switchsør.yml dette er fordi switchsør.yml setter opp Etherchanneling og noen access porter for datamaskinene. Siden ansible scriptene bruker en direkte host tilkobling til den IPen jeg har brukt på switchene bør du følge rekkefølgen som står her.
2.16 Switchnord SSH script:
- ![Full ssh SwitchNord Config](https://github.com/user-attachments/assets/b38ac1a2-ed15-4f6e-8907-a946359564e4)

2.17 Switchsør SSH script:
- ![Full ssh SwitchSør Config](https://github.com/user-attachments/assets/c459a657-69ea-46d9-a7af-02067c6de290)
