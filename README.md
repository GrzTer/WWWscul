# WWWscul – Django Coursework Projects

This repository collects several **small Django projects completed for university coursework**.  
Each top-level folder is an independent mini-application that can be run and studied on its own.

| Folder | Working title | Purpose |
|--------|---------------|---------|
| `WWW_I/` | **Conference Room Manager** | Book conference rooms and schedule meetings. |
| `ZadanieSprawdzajace/` | **GoodDoctor** | Track patients and their medical appointments. |
| *(others)* | Lab exercises | Smaller, self-contained demos created during the same course. |

---

## 1&nbsp;&nbsp;Conference Room Manager (`WWW_I/`)

### Key Features
* **Room catalogue** – store room name, floor and number  
* **Availability view** – see which rooms are free or occupied  
* **Meeting scheduler** – create meetings with title, date, start time (09:00 default) and duration  

### Data Model

| Model | Fields |
|-------|--------------------------------|
| `Room` | `name`, `floor`, `room_num` |
| `Meeting` | `title`, `date`, `start_time`, `duration`, `room (FK)` |

URLs:

```
/              → list of meetings
room/           → list of rooms
new/            → add a meeting
```

---

## 2&nbsp;&nbsp;GoodDoctor (`ZadanieSprawdzajace/`)

### Key Features
* **Patient registry** – add patients with first name, last name, city, street and age  
* **Visit log** – record appointment date and recommendations linked to a patient  
* **Screens**  
  * `/pacjenci/` – list all patients  
  * `/details/<id>/` – patient card with visit history  
  * `/new` – add a visit  

### Data Model

| Model | Fields |
|-------|--------------------------------|
| `Pacjent` | `nazwisko`, `imie`, `miasto`, `ulica`, `wiek` |
| `Wizyta` | `date`, `zalecenia`, `pacjent (FK)` |

---

## Repository Layout
```
WWWscul/
├── DjangoProject/
├── Ogloshenia/
├── Pedagodzy/
├── Ryby/
├── WWW_I/                    # Conference-room project
│   ├── website/
│   ├── templates/
│   ├── static/
│   └── manage.py
├── ZadanieSprawdzajace/      # “GoodDoctor” medical project
│   ├── GoodDoctor/
│   ├── templates/
│   ├── static/
│   └── manage.py
├── farby/
├── ogloszenie/
├── tst/
├── .gitattributes
└── README.md
```

---

## Getting Started (any project)

```bash
# choose a project folder, e.g.:
cd WWW_I          # or ZadanieSprawdzajace

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```

---

Development Notes

Standard M-V-T architecture.

Function-based views keep the code concise; feel free to refactor to class-based views if needed.

Forms are generated with modelform_factory, demonstrating quick CRUD scaffolding.

Each sub-project ships with its own manage.py so they can be run independently.



---

Contributing

1. Fork the repository.


2. Create a feature branch.


3. Commit your changes.


4. Push the branch to your fork.


5. Open a pull request.




---

License

No explicit LICENSE file is present; assume all rights reserved unless the author adds a license.
If you plan to reuse code, please contact the repository owner.



