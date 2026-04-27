import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parent
_MODULE_CACHE = {}


def load_module(filename, alias):
    key = (filename, alias)
    if key in _MODULE_CACHE:
        return _MODULE_CACHE[key]

    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    _MODULE_CACHE[key] = module
    return module


def run_script(script_name, user_input=""):
    process = subprocess.run(
        [sys.executable, str(ROOT / script_name)],
        input=user_input,
        capture_output=True,
        text=True,
        timeout=8,
    )
    return process.returncode, process.stdout, process.stderr


# -----------------------------
# Question 1 + 3: Song
# -----------------------------


def test_song_class_exists():
    song_module = load_module("song.py", "song_mod")
    assert hasattr(song_module, "Song")


def test_song_init_assigns_attributes():
    song_module = load_module("song.py", "song_mod")
    song = song_module.Song("N95", "Kendrick Lamar", 3.25)
    assert song.name == "N95"
    assert song.artist == "Kendrick Lamar"
    assert song.length == 3.25


@pytest.mark.parametrize(
    "minutes, expected_seconds",
    [
        (0, 0.0),
        (0.5, 30.0),
        (1.0, 60.0),
        (1.25, 75.0),
        (2.5, 150.0),
        (3.7, 222.0),
        (4.0, 240.0),
        (10.0, 600.0),
        (12.75, 765.0),
        (99.9, 5994.0),
    ],
)
def test_song_get_length_in_seconds(minutes, expected_seconds):
    song_module = load_module("song.py", "song_mod")
    song = song_module.Song("Any", "Artist", minutes)
    assert song.get_length_in_seconds() == pytest.approx(expected_seconds)


@pytest.mark.parametrize(
    "name, artist, length, expected",
    [
        ("tv off", "Kendrick Lamar", 3.7, "'tv off' by Kendrick Lamar (3.7)"),
        ("Alright", "Kendrick Lamar", 3.5, "'Alright' by Kendrick Lamar (3.5)"),
        ("Halo", "Beyonce", 4.2, "'Halo' by Beyonce (4.2)"),
        ("One", "U2", 4.36, "'One' by U2 (4.36)"),
        ("A", "B", 0.0, "'A' by B (0.0)"),
        ("Space Oddity", "David Bowie", 5.12, "'Space Oddity' by David Bowie (5.12)"),
    ],
)
def test_song_str_format(name, artist, length, expected):
    song_module = load_module("song.py", "song_mod")
    song = song_module.Song(name, artist, length)
    assert str(song) == expected


# -----------------------------
# Question 2: Movie
# -----------------------------


def test_movie_class_exists():
    movie_module = load_module("movie.py", "movie_mod")
    assert hasattr(movie_module, "Movie")


@pytest.mark.parametrize(
    "title, director, year",
    [
        ("Inception", "Christopher Nolan", "2010"),
        ("Interstellar", "Christopher Nolan", "2014"),
        ("Parasite", "Bong Joon-ho", "2019"),
        ("The Matrix", "Wachowski", "1999"),
        ("Amelie", "Jean-Pierre Jeunet", "2001"),
        ("Spirited Away", "Hayao Miyazaki", "2001"),
    ],
)
def test_movie_str_format(title, director, year):
    movie_module = load_module("movie.py", "movie_mod")
    movie = movie_module.Movie(title, director, year)
    assert str(movie) == f"Movie: {title} (Directed by {director}, {year})"


def test_movie_main_program_prints_formatted_output():
    code, stdout, stderr = run_script(
        "movie.py",
        "Whiplash\nDamien Chazelle\n2014\n",
    )
    assert code == 0
    assert stderr == ""
    assert "Movie: Whiplash (Directed by Damien Chazelle, 2014)" in stdout


# -----------------------------
# Question 3: practice.py
# -----------------------------


def test_print_songs_function_exists():
    practice_module = load_module("practice.py", "practice_mod")
    assert hasattr(practice_module, "print_songs")


def test_print_songs_empty_list(capsys):
    practice_module = load_module("practice.py", "practice_mod")
    practice_module.print_songs([])
    captured = capsys.readouterr()
    assert captured.out == ""


@pytest.mark.parametrize(
    "songs_data, expected_lines",
    [
        (
            [("tv off", "Kendrick Lamar", 3.7)],
            ["'tv off' by Kendrick Lamar (3.7)"],
        ),
        (
            [
                ("tv off", "Kendrick Lamar", 3.7),
                ("Alright", "Kendrick Lamar", 3.5),
            ],
            [
                "'tv off' by Kendrick Lamar (3.7)",
                "'Alright' by Kendrick Lamar (3.5)",
            ],
        ),
        (
            [
                ("Numb", "Linkin Park", 3.06),
                ("Fix You", "Coldplay", 4.55),
                ("Yellow", "Coldplay", 4.26),
            ],
            [
                "'Numb' by Linkin Park (3.06)",
                "'Fix You' by Coldplay (4.55)",
                "'Yellow' by Coldplay (4.26)",
            ],
        ),
        (
            [
                ("A", "B", 0.0),
                ("C", "D", 1.0),
                ("E", "F", 2.0),
                ("G", "H", 3.0),
            ],
            [
                "'A' by B (0.0)",
                "'C' by D (1.0)",
                "'E' by F (2.0)",
                "'G' by H (3.0)",
            ],
        ),
    ],
)
def test_print_songs_outputs_each_song_line(capsys, songs_data, expected_lines):
    song_module = load_module("song.py", "song_mod")
    practice_module = load_module("practice.py", "practice_mod")

    songs = [song_module.Song(name, artist, length) for name, artist, length in songs_data]
    practice_module.print_songs(songs)

    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == expected_lines


# -----------------------------
# Question 4: Car system
# -----------------------------


def test_car_class_exists():
    car_module = load_module("car.py", "car_mod")
    assert hasattr(car_module, "Car")


def test_car_init_default_mileage():
    car_module = load_module("car.py", "car_mod")
    car = car_module.Car("CAR001", "Toyota", 2020, "Red")
    assert car.mileage == pytest.approx(0.0)


def test_car_init_custom_mileage():
    car_module = load_module("car.py", "car_mod")
    car = car_module.Car("CAR001", "Toyota", 2020, "Red", 15000)
    assert car.mileage == pytest.approx(15000.0)


def test_car_change_color():
    car_module = load_module("car.py", "car_mod")
    car = car_module.Car("CAR001", "Toyota", 2020, "Red", 1000)
    car.change_color("Blue")
    assert car.color == "Blue"


@pytest.mark.parametrize(
    "initial, drive_by, expected",
    [
        (0.0, 10, 10.0),
        (15000.0, 200, 15200.0),
        (120.5, 0, 120.5),
        (42.0, 8.5, 50.5),
        (999.9, 0.1, 1000.0),
    ],
)
def test_car_drive_updates_mileage(initial, drive_by, expected):
    car_module = load_module("car.py", "car_mod")
    car = car_module.Car("CAR002", "Honda", 2018, "Black", initial)
    car.drive(drive_by)
    assert car.mileage == pytest.approx(expected)


@pytest.mark.parametrize(
    "car_id, brand, year, color, mileage, expected",
    [
        (
            "CAR001",
            "Toyota",
            2020,
            "Red",
            15000.0,
            "CAR001 - 2020 Red Toyota with 15000.0 miles",
        ),
        (
            "CAR100",
            "Ford",
            2010,
            "Blue",
            0.0,
            "CAR100 - 2010 Blue Ford with 0.0 miles",
        ),
        (
            "X1",
            "BMW",
            2024,
            "White",
            500.5,
            "X1 - 2024 White BMW with 500.5 miles",
        ),
        (
            "A-9",
            "Tesla",
            2023,
            "Silver",
            12345.67,
            "A-9 - 2023 Silver Tesla with 12345.67 miles",
        ),
    ],
)
def test_car_str_format(car_id, brand, year, color, mileage, expected):
    car_module = load_module("car.py", "car_mod")
    car = car_module.Car(car_id, brand, year, color, mileage)
    assert str(car) == expected


def test_create_car_from_input(monkeypatch):
    car_utils_module = load_module("car_utils.py", "car_utils_mod")

    values = iter(["CAR777", "Mazda", "2022", "Gray", "1200.5"])
    monkeypatch.setattr("builtins.input", lambda _="": next(values))

    car = car_utils_module.create_car_from_input()
    assert car.car_id == "CAR777"
    assert car.brand == "Mazda"
    assert car.year == 2022
    assert car.color == "Gray"
    assert car.mileage == pytest.approx(1200.5)


def test_display_cars_prints_all(capsys):
    car_module = load_module("car.py", "car_mod")
    car_utils_module = load_module("car_utils.py", "car_utils_mod")

    cars = {
        "CAR1": car_module.Car("CAR1", "Toyota", 2020, "Red", 100.0),
        "CAR2": car_module.Car("CAR2", "Honda", 2019, "Blue", 200.0),
    }

    car_utils_module.display_cars(cars)
    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()

    assert "CAR1 - 2020 Red Toyota with 100.0 miles" in output_lines
    assert "CAR2 - 2019 Blue Honda with 200.0 miles" in output_lines


def test_overall_add_and_exit_flow():
    user_input = "1\nCAR001\nToyota\n2020\nRed\n15000\n5\n"
    code, stdout, stderr = run_script("overall.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "CAR001 - 2020 Red Toyota with 15000.0 miles" in stdout
    assert "Car added." in stdout
    assert "Goodbye!" in stdout


def test_overall_view_flow_after_adding():
    user_input = "1\nCAR001\nToyota\n2020\nRed\n15000\n2\n5\n"
    code, stdout, stderr = run_script("overall.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "CAR001 - 2020 Red Toyota with 15000.0 miles" in stdout


def test_overall_drive_updates_mileage():
    user_input = "1\nCAR001\nToyota\n2020\nRed\n15000\n3\nCAR001\n200\n5\n"
    code, stdout, stderr = run_script("overall.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Mileage updated." in stdout
    assert "CAR001 - 2020 Red Toyota with 15200.0 miles" in stdout


def test_overall_paint_updates_color():
    user_input = "1\nCAR001\nToyota\n2020\nRed\n15000\n4\nCAR001\nBlue\n5\n"
    code, stdout, stderr = run_script("overall.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Color updated." in stdout
    assert "CAR001 - 2020 Blue Toyota with 15000.0 miles" in stdout


def test_overall_invalid_option_message():
    user_input = "9\n5\n"
    code, stdout, stderr = run_script("overall.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Invalid option. Please try again." in stdout


# -----------------------------
# Question 5: Banking system
# -----------------------------


def test_bank_account_class_exists():
    bank_module = load_module("bank_account.py", "bank_mod")
    assert hasattr(bank_module, "BankAccount")


def test_bank_account_init_default_balance():
    bank_module = load_module("bank_account.py", "bank_mod")
    account = bank_module.BankAccount(1234)
    assert account.account_number == 1234
    assert account.balance == pytest.approx(0.0)


def test_bank_account_init_custom_balance():
    bank_module = load_module("bank_account.py", "bank_mod")
    account = bank_module.BankAccount(1234, 250.75)
    assert account.balance == pytest.approx(250.75)


@pytest.mark.parametrize(
    "start, amount, expected",
    [
        (0.0, 0.0, 0.0),
        (0.0, 10.0, 10.0),
        (100.0, 50.0, 150.0),
        (50.25, 49.75, 100.0),
        (999.99, 0.01, 1000.0),
    ],
)
def test_bank_account_deposit(start, amount, expected):
    bank_module = load_module("bank_account.py", "bank_mod")
    account = bank_module.BankAccount(1234, start)
    account.deposit(amount)
    assert account.balance == pytest.approx(expected)


@pytest.mark.parametrize(
    "start, withdraw_amount, expected_code, expected_balance",
    [
        (100.0, 20.0, 0, 80.0),
        (100.0, 100.0, 0, 0.0),
        (100.0, 120.0, -1, 100.0),
        (0.0, 0.0, 0, 0.0),
        (10.5, 10.6, -1, 10.5),
        (10.5, 10.5, 0, 0.0),
    ],
)
def test_bank_account_withdraw(start, withdraw_amount, expected_code, expected_balance):
    bank_module = load_module("bank_account.py", "bank_mod")
    account = bank_module.BankAccount(1234, start)
    code = account.withdraw(withdraw_amount)
    assert code == expected_code
    assert account.balance == pytest.approx(expected_balance)


@pytest.mark.parametrize(
    "account_number, balance, expected_mask",
    [
        (1234, 100.0, "34"),
        (1001, 0.0, "01"),
        (9876, 5.5, "76"),
        (42, 12.345, "42"),
    ],
)
def test_bank_account_str_format(account_number, balance, expected_mask):
    bank_module = load_module("bank_account.py", "bank_mod")
    account = bank_module.BankAccount(account_number, balance)
    expected = f"Account Number: **{expected_mask}\nCurrent Balance: {balance:.2f}"
    assert str(account) == expected


def test_person_class_exists():
    person_module = load_module("person.py", "person_mod")
    assert hasattr(person_module, "Person")


def test_person_init_sets_empty_accounts():
    person_module = load_module("person.py", "person_mod")
    person = person_module.Person("Daniel")
    assert person.name == "Daniel"
    assert person.accounts == []


def test_person_add_account_appends_item():
    person_module = load_module("person.py", "person_mod")
    bank_module = load_module("bank_account.py", "bank_mod")

    person = person_module.Person("Alice")
    account = bank_module.BankAccount(1234, 50.0)
    person.add_account(account)

    assert len(person.accounts) == 1
    assert person.accounts[0] is account


def test_person_str_format():
    person_module = load_module("person.py", "person_mod")
    bank_module = load_module("bank_account.py", "bank_mod")

    person = person_module.Person("Maria")
    person.add_account(bank_module.BankAccount(1111, 10.0))
    person.add_account(bank_module.BankAccount(2222, 20.0))

    assert str(person) == "Name = Maria, Number of accounts = 2"


def test_utils_person_data_single_account(monkeypatch):
    utils_module = load_module("utils.py", "bank_utils_mod")

    values = iter(["Daniel", "1234", "100.0", "yes"])
    monkeypatch.setattr("builtins.input", lambda _="": next(values))

    person = utils_module.person_data()

    assert person.name == "Daniel"
    assert len(person.accounts) == 1
    assert person.accounts[0].account_number == 1234
    assert person.accounts[0].balance == pytest.approx(100.0)


def test_utils_person_data_multiple_accounts(monkeypatch):
    utils_module = load_module("utils.py", "bank_utils_mod")

    values = iter(["Alice", "1111", "40.0", "no", "2222", "60.5", "yes"])
    monkeypatch.setattr("builtins.input", lambda _="": next(values))

    person = utils_module.person_data()

    assert person.name == "Alice"
    assert len(person.accounts) == 2
    assert person.accounts[0].account_number == 1111
    assert person.accounts[1].account_number == 2222
    assert person.accounts[0].balance == pytest.approx(40.0)
    assert person.accounts[1].balance == pytest.approx(60.5)


def test_balance_summary_one_person(capsys):
    person_module = load_module("person.py", "person_mod")
    bank_module = load_module("bank_account.py", "bank_mod")
    utils_module = load_module("utils.py", "bank_utils_mod")

    person = person_module.Person("Daniel")
    person.add_account(bank_module.BankAccount(1234, 90.0))

    utils_module.balance_summary([person])
    captured = capsys.readouterr()

    assert captured.out.strip() == "Daniel : 90.00"


def test_balance_summary_multiple_people(capsys):
    person_module = load_module("person.py", "person_mod")
    bank_module = load_module("bank_account.py", "bank_mod")
    utils_module = load_module("utils.py", "bank_utils_mod")

    daniel = person_module.Person("Daniel")
    daniel.add_account(bank_module.BankAccount(1111, 50.0))
    daniel.add_account(bank_module.BankAccount(2222, 40.0))

    alice = person_module.Person("Alice")
    alice.add_account(bank_module.BankAccount(3333, 150.25))

    utils_module.balance_summary([daniel, alice])
    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert "Daniel : 90.00" in lines
    assert "Alice : 150.25" in lines


def test_main_shows_no_data_message_when_empty():
    code, stdout, stderr = run_script("main.py", "3\n4\n")

    assert code == 0
    assert stderr == ""
    assert "No data to show." in stdout
    assert "Goodbye!" in stdout


def test_main_add_person_then_show_balances():
    user_input = "1\nDaniel\n1234\n100.0\nyes\n3\n4\n"
    code, stdout, stderr = run_script("main.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Daniel : 100.00" in stdout
    assert "Goodbye!" in stdout


def test_main_add_account_to_existing_person():
    user_input = "1\nAna\n1111\n100\nyes\n2\nAna\n2222\n50\n3\n4\n"
    code, stdout, stderr = run_script("main.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Ana : 150.00" in stdout


def test_main_add_account_person_not_found():
    user_input = "2\nGhost\n4\n"
    code, stdout, stderr = run_script("main.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Person not found." in stdout


def test_main_invalid_option_message():
    user_input = "9\n4\n"
    code, stdout, stderr = run_script("main.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Invalid option. Please choose 1-4." in stdout


# -----------------------------
# Question 6: aircraft_altitude.py
# -----------------------------


def test_aircraft_altitude_example_flow():
    user_input = "Boeing 747\nA 5000\nD 2000\nX\n"
    code, stdout, stderr = run_script("aircraft_altitude.py", user_input)

    assert code == 0
    assert stderr == ""
    assert "Final altitude: 3000 feet" in stdout


@pytest.mark.parametrize(
    "commands, expected_altitude",
    [
        ("Cessna\nX\n", 0),
        ("Cessna\nA 100\nA 150\nX\n", 250),
        ("Cessna\nD 50\nX\n", -50),
        ("Cessna\nA 200\nD 20\nA 30\nD 10\nX\n", 200),
    ],
)
def test_aircraft_altitude_various_sequences(commands, expected_altitude):
    code, stdout, stderr = run_script("aircraft_altitude.py", commands)

    assert code == 0
    assert stderr == ""
    assert f"Final altitude: {expected_altitude} feet" in stdout


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
