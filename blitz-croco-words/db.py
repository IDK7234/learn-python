import sqlite3
from multiprocessing.connection import Connection


def add_data(con: sqlite3.Connection, name:str, dic: {str,str}) -> None:
    cur = con.cursor()
    cur.executemany(f"INSERT INTO {name} VALUES(?, ?)", dic)
    con.commit()



def main():
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    name = "movie_new"
    cur.execute(f"CREATE TABLE IF NOT EXISTS {name}(title, year)")

    data = {
        ("Monty Python Live at the Hollywood Bowl", 1982),
        ("Monty Python's The Meaning of Life", 1983),
        ("Monty Python's Life of Brian", 1979),
    }

    add_data(con, name, data)


if __name__ == '__main__':
    main()