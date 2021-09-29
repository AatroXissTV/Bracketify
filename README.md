# Bracketify (OC_P4)

Bracketify is a **training project** part of "Python application developer" training of OpenClassrooms. 
It's an interactive CLI application made in Python. It's developed with an MVC pattern and uses TinyDB to persist Rounds, matches, players & tournaments. 

The front-end is made with a package called PyInquirer. 
It has been made on Windows so it might not work with MacOS and Linux. 

Make sure to install all packages in 'requirements.txt'.

The software currently handles management of chess tournament with Swiss Pairing algorithm.

## Download & Create a virtual env

For this software you will need Python 3 (made on Python 3.9.6)

Open a terminal and navigate into the folder you want Bracketify to be downloaded. 
Then run the following commands: 

* From repository download files and clone the folder.
    ```
    $ git clone https://github.com/AatroXissTV/Bracketify.git Bracketify
    $ cd Bracketify
    ```
* Create a Python environment named "env".
    ```
    $ python -m venv env
    ```
* Activate the environment.
    ```
    $ source/env/bin/activate #MacOS & linux
    $ source/env/Scripts/activate # Windows
    ```
* Install packages from **requirements.txt**.
    ```
    $ pip install -r requirements.txt
    ```
* Once you have created the environment and the requirements.txt you can execute the script that way :
    ```
    $ python main.py
    ```

## Generate Flake8 Report

You can generate a flake8 report. It's located inside the 'flake-report' folder. 
flake8 has an option for max-line set to 79.

* Generate Flake8 report:
    ```
    $ flake8 --format=html --htmldir=flake-report
    ```

## Updates

Hi everyone, 
I finally finished this long OpenClassrooms project that gave me a lot of trouble and made me lose my two weeks advance. 

Everything works according to the specifications except for the matches which are not stored as tuples but directly with a list of key values in the database. 

## Author

This software was made by Antoine "AatroXiss" Beaudesson with :heart: and :coffee:

## Support

Contributions, issues and features requests are welcome ! 
Feel free to give a ⭐️ if you liked this project. 