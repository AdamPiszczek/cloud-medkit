## Authors
- Kacper Kilianek
- Adam Piszczek
- Mateusz Cegielski
- Ivan Ryzhankow

## Setup 🛠️
- Linux / macOS version
```sh
> pip install ./requirements.txt
> python3 manage.py makemigrations
> python3 manage.py migrate
> python3 manage.py collectstatic
> python3 manage.py runserver
```
- Windows version
```sh
> pip install -r ./requirements.txt
> python manage.py makemigrations
> python manage.py migrate
> python manage.py collectstatic
> python manage.py runserver
```
<ins>Before the first run, ensure that you have on and active PostgreSQL database.</ins>

## How to Run
- Linux / macOS version
```sh
> python3 manage.py runserver
```
- Windows  version
```sh
> python manage.py runserver
```