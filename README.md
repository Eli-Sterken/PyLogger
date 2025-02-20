# PyLogger
A simple keylogger written in Python.

# How To Use

Input your webhook in the ```webhook``` varible in main.py

```zsh
python -m venv env
```
```zsh
./env/Scripts/Activate.ps1
 ```

Change "Activate.ps1" to the env activation script for your system. Hore info [here](https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/).

```zsh
pip install -r requirements.txt
```
```zsh
pyinstaller --onefile --icon icon.png main.py
```

Then use the exe created in ```/dist```

# Enjoy!
