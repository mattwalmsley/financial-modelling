# Notes on Python Set-Up

Create virtual environment with venv module

    python3 -m venv .venv

- [Using the command line](https://docs.python.org/3/using/cmdline)
- [venv](https://docs.python.org/3/library/venv.html)

</br>

Activate virtual environment:

    source .venv/bin/activate

</br>

Install required packages for venv from file:

    pip3 install -r requirements.txt

</br>

Add the following to workspace settings for VS Code - [settings.json](../../.vscode/settings.json):

    "python.defaultInterpreterPath": "${workspaceFolder}/quant-library/python/.venv"

</br>

To make/update the file with required packages for venv:

    pip3 freeze > requirements.txt
