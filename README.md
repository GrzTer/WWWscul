# 🌐 Repozytorium Projektów Django WWWscul

> To repozytorium zawiera dwie aplikacje webowe Django: System Zarządzania Salami Konferencyjnymi (WWW_I) oraz System Rezerwacji Wizyt Medycznych (ZadanieSprawdzajace).

---

## 📑 Przegląd Projektów

### 1. 🏢 Zarządzanie Salami Konferencyjnymi (WWW_I)

Aplikacja Django do zarządzania salami konferencyjnymi i planowania spotkań w organizacji.

#### ✨ Funkcje
- **Zarządzanie Salami**
  - 📋 Śledzenie informacji o salach (nazwa, piętro, numer sali)
  - 🔍 Podgląd dostępności sal
- **Zarządzanie Spotkaniami**
  - 📅 Planowanie spotkań z tytułem, datą i czasem trwania
  - 🔄 Przypisywanie spotkań do konkretnych sal
  - ⏱️ Śledzenie czasów i długości spotkań

#### 💾 Modele
- **`Sala`**
  - 📝 Nazwa
  - 🏗️ Piętro
  - 🔢 Numer sali
- **`Spotkanie`**
  - 📌 Tytuł
  - 📅 Data
  - ⏰ Czas rozpoczęcia (domyślnie: 9:00)
  - ⌛ Czas trwania (w godzinach)
  - 🔗 Sala (klucz obcy)

### 2. 👨‍⚕️ GoodDoctor (ZadanieSprawdzajace)

System zarządzania wizytami medycznymi do śledzenia pacjentów i ich wizyt.

#### ✨ Funkcje
- **Zarządzanie Pacjentami**
  - 👥 Przechowywanie i zarządzanie informacjami o pacjentach
  - 📊 Podgląd szczegółów i historii pacjentów
- **Zarządzanie Wizytami**
  - 📋 Planowanie i śledzenie wizyt medycznych
  - 📝 Zapisywanie zaleceń z wizyt
  - 📊 Przegląd statystyk wizyt

#### 💾 Modele
- **`Pacjent`**
  - 👤 Imię
  - 👤 Nazwisko
  - 🏙️ Miasto
  - 🏠 Ulica
  - 📅 Wiek
- **`Wizyta`**
  - 📅 Data
  - 📝 Zalecenia
  - 👤 Pacjent (klucz obcy)

## 🗂️ Struktura Repozytorium

```bash
WWWscul/
├── WWW_I/                  # 🏢 Projekt Zarządzania Salami
│   ├── website/            # 💻 Główna aplikacja
│   ├── templates/          # 🎨 Szablony HTML
│   ├── static/             # 📁 Pliki statyczne
│   └── manage.py           # ⚙️ Skrypt zarządzania
│
└── ZadanieSprawdzajace/    # 👨‍⚕️ Projekt Medyczny
    ├── GoodDoctor/         # 💊 Główna aplikacja
    ├── templates/          # 🎨 Szablony HTML
    ├── static/             # 📁 Pliki statyczne
    └── manage.py           # ⚙️ Skrypt zarządzania
```

## ⚙️ Instalacja i Konfiguracja

### 📋 Wymagania wstępne
- 🐍 Python 3.x
- 📦 pip (menedżer pakietów Python)
- 🔒 Wirtualne środowisko (zalecane)

### 🚀 Konfiguracja dowolnego projektu

1️⃣ Przejdź do katalogu projektu (WWW_I lub ZadanieSprawdzajace)

2️⃣ Utwórz i aktywuj wirtualne środowisko:
```bash
python -m venv venv
source venv/bin/activate  # Na Windows: venv\Scripts\activate
```

3️⃣ Zainstaluj zależności:
```bash
pip install django
```

4️⃣ Zastosuj migracje bazy danych:
```bash
python manage.py migrate
```

5️⃣ Utwórz superużytkownika (opcjonalnie):
```bash
python manage.py createsuperuser
```

6️⃣ Uruchom serwer deweloperski:
```bash
python manage.py runserver
```

## 📱 Użytkowanie

### 🏢 WWW_I (Zarządzanie Salami)
1. 🔑 Uzyskaj dostęp do panelu administracyjnego
2. 🏗️ Zarządzaj salami przez interfejs
3. 📅 Planuj i organizuj spotkania

### 👨‍⚕️ GoodDoctor
1. 👥 Zarządzaj pacjentami i wizytami
2. 📋 Przeglądaj dane pacjentów
3. 📊 Monitoruj statystyki wizyt

## 💻 Rozwój

Oba projekty stosują architekturę MVT Django:
- **📦 Model**: Struktura danych
- **🔄 Widok**: Logika biznesowa
- **🎨 Szablon**: Warstwa prezentacji

## 🤝 Wkład w Projekt

1. 🔄 Sforkuj repozytorium
2. 🌿 Utwórz gałąź funkcji
3. ✅ Zatwierdź zmiany
4. 📤 Wypchnij do gałęzi
5. 📩 Utwórz Pull Request

## 📄 Licencja

Te projekty są open-source i dostępne na licencji MIT.

---

<div align="center">
<i>Stworzone z ❤️ przy użyciu Django</i>
</div>