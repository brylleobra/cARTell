(~\$ This Symbol means in command prompt followed by a command)

<b><h1>Python Setup</h1></b>

1. Install Python 3. Check if you have python installed in your local machine, make sure you have a correct python version

   (if you have no python installed get the installer here https://www.python.org/downloads/release/python-372/)

   <b>make sure to tick the checkbox "Add Python 3.7 to PATH" in installer </b>
   ![image](https://user-images.githubusercontent.com/30989726/55272839-07f24700-52fe-11e9-8cf1-90ef0a7cc81f.png)

   This is to ensure that python commands can run in your command prompt/terminal without having to navigate to the python directory
   
   ~\$python --version

   Expected output
   (~\$Python 3.7.2) #Python 3.7.2 is also acceptable

2. Install Pip for Python 3. After installation check the version

   ~\$pip3 --version

   Expected Output
   pip 9.0.1 from .../lib/python3.7/... (python 3.7)

3. Install pipenv, python pip virtual environment, This is to create a separate python dependencies environment so that any installation to your local machine will not mess up your system

   ~\$pip3 install pipenv

4. Create a pipenv

   ~\$pipenv shell

5. Clone repo

   ~\$git clone <repo clone link>

6. Install requirements

   ~\$pipenv install -r requirements-dev.txt
