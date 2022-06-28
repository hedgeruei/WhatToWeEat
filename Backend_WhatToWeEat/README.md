# 今天吃什麼 後端


## Pre-install
- Poetry
    - poetry config virtualenvs.in-project true

## Project Setup
```
poetry install
```

## Set FLASK_APP
for bash
```bash
export FLASK_APP=main
```

for powershell
```powershell
$env:FLASK_APP="main"
```

## Project Run
```
make backend-run
```
or 
```
poetry run flask run
```
or
```
flask run
```
