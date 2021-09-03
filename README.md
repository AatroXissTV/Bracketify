# Bracketify

This is a **training project** part of "Application Developper Python" OC formation. 

The software has to handle chess tournaments with swiss pairing.

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

## Updates

This is a beta version of Bracketify and things are not working as expected.
Files are structured with MVC but critical features are missing such as views and controllers. 
Models are not completed yet and work has to be done on every model to ensure everything is working as intended. 

Updates on the models are expected to be done by the end of the week (Aug 5, 2021). 

First version of Views have been implementend. 
They are not connected with anything.

You can consult the project management board if you want accurate tracking of progress! 

### To Do list
- [x] Create player model
- [x] Create tournament model
- [x] Create participant model
- [x] Create match model
- [x] Create round model
- [ ] Create Main Menu view
- [ ] Create tournament view
- [ ] Create player view

## Author

This software was made by Antoine "AatroXiss" Beaudesson with :heart: and :coffee:

## Support

Contributions, issues and features requests are welcome ! 
Feel free to give a ⭐️ if you liked this project. 