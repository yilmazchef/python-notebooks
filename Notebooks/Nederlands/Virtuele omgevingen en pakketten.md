---
created: 13-09-222022
tags: []
source: https://github.com/yilmazchef/repo
author: Yilmaz Mustafa
---

# 12. Virtuele omgevingen en pakketten — Python 3.10.7 documentatie

> ## Excerpt

> Python toepassingen zullen vaak pakketten en modules gebruiken die niet
deel uitmaken van de standaard bibliotheek.  Toepassingen zullen soms
een specifieke versie van een bibliotheek nodig hebben, omdat de toepassing
vereist dat een bepaalde bug hersteld is of de toepassing kan geschreven zijn
geschreven is met een verouderde versie van de interface van de bibliotheek.

---

## 12\. Virtual Environments and Packages[¶](https://docs.python.org/3/tutorial/venv.html#virtual-environments-and-packages "Permalink to this headline")

## 12.1. Introduction[¶](https://docs.python.org/3/tutorial/venv.html#introduction "Permalink to this headline")

Python toepassingen zullen vaak packages en modules gebruiken die geen deel uitmaken van de standaard bibliotheek. Toepassingen zullen soms een specifieke versie van een bibliotheek nodig hebben, omdat de toepassing kan vereisen dat een bepaalde bug hersteld is of omdat de toepassing geschreven kan zijn met een verouderde versie van de interface van de bibliotheek.

Dit betekent dat één Python-installatie misschien niet aan de eisen van elke toepassing kan voldoen. Als applicatie A versie 1.0 van een bepaalde module nodig heeft, maar applicatie B heeft versie 2.0 nodig, dan zijn de vereisten in conflict en zal het installeren van versie 1.0 of 2.0 ervoor zorgen dat één applicatie niet kan draaien.

De oplossing voor dit probleem is het maken van een [virtuele omgeving](https://docs.python.org/3/glossary.html#term-virtual-environment), een op zichzelf staande mapstructuur die een Python-installatie bevat voor een bepaalde versie van Python, plus een aantal aanvullende pakketten.

Verschillende toepassingen kunnen dan verschillende virtuele omgevingen gebruiken. Om het eerdere voorbeeld van conflicterende vereisten op te lossen, kan applicatie A zijn eigen virtuele omgeving hebben met versie 1.0 geïnstalleerd, terwijl applicatie B een andere virtuele omgeving heeft met versie 2.0. Als applicatie B vereist dat een bibliotheek wordt opgewaardeerd naar versie 3.0, heeft dit geen invloed op de omgeving van applicatie A.

## 12.2. Creating Virtual Environments[¶](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments "Permalink to this headline")

De module die gebruikt wordt om virtuele omgevingen te creëren en te beheren heet [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Aanmaken van virtuele omgevingen."). [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") zal gewoonlijk de meest recente versie van Python installeren die u beschikbaar heeft. Als u meerdere versies van Python op uw systeem heeft, kunt u een specifieke Python-versie selecteren door `python3` uit te voeren of welke versie u maar wilt.

Om een virtuele omgeving aan te maken, kiest u een directory waar u deze wilt plaatsen, en voert u de [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") module als een script met het directory pad:

```
python3 -m venv tutorial-env

```

Dit maakt de directory aan als die nog niet bestaat, en maakt er ook directories in aan met daarin een kopie van de Python interpreter en diverse ondersteunende bestanden.`tutorial-env`

Een gebruikelijke directory locatie voor een virtuele omgeving is . Deze naam houdt de directory meestal verborgen in je shell en dus uit de weg, terwijl het een naam geeft die verklaart waarom de directory bestaat. Het voorkomt ook botsingen met omgevingsvariabele definitiebestanden die sommige tooling ondersteunt.`.venv``.env`

Als u eenmaal een virtuele omgeving heeft aangemaakt, kunt u deze activeren.

On Windows, run:

```
tutorial-env\Scripts\activate.bat

```

On Unix or MacOS, run:

```
source tutorial-env/bin/activate

```

(Dit script is geschreven voor de bash shell. Als je de **csh** of **fish** shells gebruikt, zijn er alternatieven en scripts die je in plaats daarvan zou moeten gebruiken.)`activate.csh``activate.fish`

Het activeren van de virtuele omgeving zal de prompt van je shell veranderen om te laten zien welke virtuele omgeving je gebruikt, en zal de omgeving zo aanpassen dat het uitvoeren ervan je die specifieke versie en installatie van Python zal opleveren. Bijvoorbeeld: `python`

```
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>

```

## 12.3. Pakketten beheren met pip[¶](https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip "Permalink to this headline")

U kunt pakketten installeren, upgraden en verwijderen met behulp van een programma met de naam **pip**. Standaard worden pakketten geïnstalleerd vanuit de Python Package Index, <[https://pypi.org](https://pypi.org/)\>. U kunt door de Python Package Index bladeren door ernaartoe te gaan in uw webbrowser.`pip`

`pip` heeft een aantal subopdrachten: "install", "uninstall", "freeze", etc. (Raadpleeg de [Installing Python Modules](https://docs.python.org/3/installing/index.html#installing-index) guide voor volledige documentatie voor .)`pip`

U kunt de nieuwste versie van een pakket installeren door de naam van een pakket op te geven:

```
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3

```

U kunt ook een specifieke versie van een pakket installeren door de pakketnaam gevolgd door en het versienummer op te geven:`==`

```
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0

```

Als u deze opdracht opnieuw uitvoert, ziet u dat de gevraagde versie al is geïnstalleerd en doet u niets. U kunt een ander versienummer opgeven om die versie te krijgen, of u kunt uitvoeren om het pakket te upgraden naar de nieuwste versie:`pip``pip install --upgrade`

```
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0

```

`pip uninstall` gevolgd door een of meer pakketnamen worden de pakketten uit de virtuele omgeving verwijderd.

`pip show` geeft informatie weer over een bepaald pakket:

```
(tutorial-env) $ pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:

```

`pip list` geeft alle pakketten weer die in de virtuele omgeving zijn geïnstalleerd:

```
(tutorial-env) $ pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)

```

`pip freeze` zal een vergelijkbare lijst van de geïnstalleerde pakketten produceren, maar de uitvoer gebruikt het formaat dat wordt verwacht. Een veel voorkomende conventie is om deze lijst in een bestand te plaatsen:`pip install``requirements.txt`

```
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0

```

Het kan vervolgens worden toegewezen aan versiebeheer en worden verzonden als onderdeel van een toepassing. Gebruikers kunnen vervolgens alle benodigde pakketten installeren met:`requirements.txt``install -r`

```
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

```

`pip` heeft veel meer opties. Raadpleeg de [handleiding Python Modules installeren](https://docs.python.org/3/installing/index.html#installing-index) voor volledige documentatie voor . Wanneer u een pakket hebt geschreven en het beschikbaar wilt maken op de Python Package Index, raadpleegt u de [handleiding Python Modules distribueren](https://docs.python.org/3/distributing/index.html#distributing-index).`pip`
