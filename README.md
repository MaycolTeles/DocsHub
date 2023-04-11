# C214 Project

This repository contains the code for C214 - Engenharia de Software project.

# TODO: REMOVE
# O que é o projeto, Funcionalidades, Ferramentas e Tecnologias Utilizadas (explicar sobre cada uma delas e o motivo da escolha) e Equipe.

<h4 align="left"> 
	Authors :pencil2:
</h4>

<p align="left">
 <a href="https://github.com/maycolteles">Maycol Teles Costa Dionisio Pereira</a> 
</p>
<p align="left">
 <a href="https://github.com/RaphaelRFreitas">Raphael Rangel Freitas</a> 
</p>

*********************

## Summary :clipboard:

* [Requirements](#requirements)
* [Setup and Installation](#setup-installation)
* [How to Use](#how-to-use)
* [Technical Information](#technical-information)
* [Final Considerations](#final-considerations)

*********************
##  Requirements :pencil: <a name="requirements"></a>

* [Python 3.10+](https://www.python.org/)
* Pip 23.0+ (comes with Python 3)

*********************
##  Setup and Installation :white_check_mark: <a name="setup-installation"></a>

### Cloning the repo :file_folder:
First off, in order to get a copy of the project to run/test it, clone the repository into a folder on your machine:

```
git clone git@github.com:MaycolTeles/projeto_c214.git
```

### Creating and Activating the Virtual Environment :open_file_folder:
It is recommended to install the dependencies inside a [virtualenv](https://docs.python.org/3/tutorial/venv.html). So, inside the folder where you cloned the repository, create a new virtualenv:

```
python3 -m virtualenv venv
```
    
Then, activate the virtualenv (for Linux/MacOS):

```
source venv/bin/activate
```

or (for Windows):

```
venv\Scripts\activate
```

if you're having some problems with the `virtualenv` or wants to learn more, check [this docs](docs/virtualenv.md).

### Installing Dependencies :wrench:
To install all the necessary project dependencies, run the following command in the terminal (but first make sure you're running it from whithin the virtualenv):

```
pip install -r requirements.txt
```

### Executing the Project :arrow_forward:
To run the application, you can use the Makefile to run it by running:

```
make run
```

or you can use the Python interpreter directly by running:

```
python app/run.py
```

*********************

## How To Use :man_technologist: <a name="how-to-use"></a>

# TODO
*********************

##  Technical Information :pencil: <a name="technical-information"></a>

The application is writting in Python, using concepts of:
* Clean Architecture
* Clean Code
* SOLID
* TDD

Some of the technologies are listed below:
* Flask
* Django
* SQLite
* MySQL
* MongoDB

To check the technical information in details you can check [this docs](docs/technical_information.md).

*********************
## Final Considerations :pushpin: <a name="final-considerations"></a>

To create the "Aula" entity, a builder could be used. Also, the project's architecture and design could be improved as well.