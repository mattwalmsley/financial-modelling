# Notes on Python Set-Up

Creat virtual enviornment with venv module

    python3 -m venv .venv

- [Using the command line](https://docs.python.org/3/using/cmdline)
- [venv](https://docs.python.org/3/library/venv.html)

<br>
Activate virtual environment:

    source .venv/bin/activate

<br>
Make a file with required packagages for venv:

    pip3 freeze > requirements.txt

<br>
Install required packagages for venv from file:

    pip3 install -r requirements.txt