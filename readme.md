## Authors
- [Kacper Kilianek](https://github.com/Kkilianek)
- [Adam Piszczek](https://github.com/AdamPiszczek)
- [Mateusz Cegielski](https://github.com/MateuszCegielski)
- [Ivan Ryzhankow](https://github.com/ToCatharsis)

## Abstract
A web application that allows the patient's medications to be stored backwards, allowing doctors to view the medicines taken by a given patient. It would be vital in treating heart diseases, where patients take many different medications. An additional advantage of the application is its security, which properly encrypts the patient's data and remedies, storing information about them on an external server (in the cloud).

## Setup
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

## How to Run
<ins>Before the first run, ensure that you have on and active PostgreSQL database.</ins>
- Linux / macOS version
```sh
> python3 manage.py runserver
```
- Windows  version
```sh
> python manage.py runserver
```
