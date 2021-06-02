# Open food fact project

### Version 1.0.0

This is the first release of this project.
More upgrades might come in a near future stay tuned !

## Installation

pip install mysql-connector-python
pip install requests

The solution is to install corresponding Python 3 module:

sudo apt-get install python3-mysql.connector

It fixes import mysql.connector error.


## Usage
This program is made to find healthier alternatives to a base product.
The only criteria for the search is the nutri-score. ( To see what is a nutriscore: [Nutriscore](https://fr.wikipedia.org/wiki/Nutri-score) )

After a search, if you like the result you can save it for further usage.

# How to use:

Launch main.py

Press Enter to exit the welcome menu.

You will be given a list of choice from different categories.
Select one, then another list of product to choose from will be given.
Select one, then the program will search inside its database for a proper substitute.
Once found you will be displayed with all the informations regarding this product,
(Name, nutriscore, shops where you can find it and a link to this product sheet)
Then you will be given the choice to save the result or make another search.

When inside the main menu you can also see your saved products, update the database for more up to date infos regarding the products, or exit the program.


### Copyright and contributions

contributors : Pierre F Le Gulluche

Open Source program.Use it at will.