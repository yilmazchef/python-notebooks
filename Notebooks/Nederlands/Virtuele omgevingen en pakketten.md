---
created: 13-09-222022
tags: []
source: https://github.com/yilmazchef/repo
author: Yilmaz Mustafa
---

# 12. Virtuele omgevingen en pakketten — Python 3.10.7 documentatie

> ## Excerpt

> Python applications will often use packages and modules that don’t
come as part of the standard library.  Applications will sometimes
need a specific version of a library, because the application may
require that a particular bug has been fixed or the application may be
written using an obsolete version of the library’s interface.

---

## 12\. Virtual Environments and Packages[¶](https://docs.python.org/3/tutorial/venv.html#virtual-environments-and-packages "Permalink to this headline")

## 12.1. Introduction[¶](https://docs.python.org/3/tutorial/venv.html#introduction "Permalink to this headline")

Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

The solution for this problem is to create a [virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment), a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A’s environment.

## 12.2. Creating Virtual Environments[¶](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments "Permalink to this headline")

The module used to create and manage virtual environments is called [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments."). [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") will usually install the most recent version of Python that you have available. If you have multiple versions of Python on your system, you can select a specific Python version by running or whichever version you want.`python3`

To create a virtual environment, decide upon a directory where you want to place it, and run the [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") module as a script with the directory path:

```
python3 -m venv tutorial-env

```

This will create the directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.`tutorial-env`

A common directory location for a virtual environment is . This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with environment variable definition files that some tooling supports.`.venv``.env`

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

```
tutorial-env\Scripts\activate.bat

```

On Unix or MacOS, run:

```
source tutorial-env/bin/activate

```

(This script is written for the bash shell. If you use the **csh** or **fish** shells, there are alternate and scripts you should use instead.)`activate.csh``activate.fish`

Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running will get you that particular version and installation of Python. For example:`python`

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
