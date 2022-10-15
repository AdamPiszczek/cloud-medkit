## Authors :pushpin:
- [Kacper Kilianek](https://github.com/Kkilianek)
- [Adam Piszczek](https://github.com/AdamPiszczek)
- [Mateusz Cegielski](https://github.com/MateuszCegielski)
- [Ivan Ryzhankow](https://github.com/ToCatharsis)

## About the event :calendar:
E-Health Hackathon - a two-day programming marathon organized as part of the Warsaw Health Innovation Hub consortium by Roche Polska, Janssen Polska in cooperation with the Federation of Polish Entrepreneurs. The aim was to develop an innovative IT solution for urgent changes - cardiology, with particular emphasis on heart failure. Teams of 3-5 people consisting of students or representatives of start-ups could apply to participate in the e-Health Hackathon. The three best projects will receive cash prizes: PLN 20,000, PLN 15,000, and PLN 10,000. The winning team was also allowed to present the developed solution to the Council of the Warsaw Health Innovation Hub and the WHIH Public Interest Group, which includes representatives of public administration.

## Abstract :books:
Our solution was a web application that allows the patient's medications to be stored backwards, allowing doctors to view the medicines taken by a given patient. It would be vital in treating heart diseases, where patients take many different medications. An additional advantage of the application is its security, which properly encrypts the patient's data and remedies, storing information about them on an external server (in the cloud). For more information, please see our presentation, which is available [under the given link](https://view.genial.ly/634272534b861e0011e57517/presentation-medkit)

## Setup :wrench:
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

## How to Run :running:
<ins>Before the first run, ensure that you have on and active PostgreSQL database.</ins>
- Linux / macOS version
```sh
> python3 manage.py runserver
```
- Windows  version
```sh
> python manage.py runserver
```
