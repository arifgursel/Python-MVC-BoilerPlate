# Python-MVC-BoilerPlate

Instructions
Install Pip
First make sure you have pip installed. If you don't have it installed there are great instructions here:  https://pip.pypa.io/en/latest/installing.html

Install virtualenv
sudo pip install virtualenv
Clone from Git
Now we'll clone the project from GitHub

git clone -b stable https://github.com/Ketul-Patel/Pylot.git
Run the Setup
cd into the project and source the setup file

cd Pylot
. setup
If the setup command threw an error run from the Pylot directory:

./setup
And then:

source venv/bin/activate
After your set up command has run, your terminal prompt should look like something this. Specifically the (venv):
Start the Server
Now you can start your development server like so:

python manage.py runserver
