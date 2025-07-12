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