import sqlite3
from pathlib import Path

class DB_Film:
    def __init__(self):
        self.connection = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('DROP TABLE IF EXISTS films')
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS films (
        top INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        rating INTEGER,
        genre TEXT,
        image TEXT
        )
        """)

    def populate_tables(self):
        self.cursor.execute('''
        iNSERT INTO films (name, description, rating, genre, image) VALUES
        ("Kingsman", "«Kingsman» — организация супершпионов, действующая на благо человечества вдали от любопытных глаз.", 7.7, "Боевик", "https://s6.vcdn.biz/static/f/782641401/image.jpg/pt/r375x0x4"),
        ("Titanic", "В первом и последнем плавании шикарного «Титаника» встречаются двое. Пассажир нижней палубы Джек выиграл билет в карты, а богатая наследница Роза отправляется в Америку, чтобы выйти замуж по расчёту.", 8.4, "Романтика/Приключения", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.kino-teatr.ru%2Fmovie%2Fposters%2Fbig%2F2%2F19522.jpg&tbnid=B4XJBBm0364JmM&vet=12ahUKEwjr4fqzr6uEAxWeQ1UIHcYnCC8QMygEegQIARBQ..i&imgrefurl=https%3A%2F%2Fwww.kino-teatr.ru%2Fkino%2Fmovie%2Fhollywood%2F19522%2Fannot%2F&docid=0bKn-PR__j59CM&w=300&h=434&q=титаник%20жанр&client=safari&ved=2ahUKEwjr4fqzr6uEAxWeQ1UIHcYnCC8QMygEegQIARBQ"),
        ("King Kong", "В 1930-м году съемочная группа под предводительством режиссера-неудачника Карла Дэнхэма отправляется на загадочный Остров Черепа неподалеку от Суматры, чтобы изучать легенды о гигантской горилле по кличке Конг.", 7.6, "Боевик/Ужасы","https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BMjYxYmRlZWYtMzAwNC00MDA1LWJjNTItOTBjMzlhNGMzYzk3XkEyXkFqcGdeQXVyMTQxNzMzNDI%40._V1_.jpg&tbnid=GGxXoBAjNWRriM&vet=12ahUKEwiRnNHnsauEAxW9FRAIHSNcDigQMygAegQIARBH..i&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0360717%2F&docid=TpLz7eSbBmhejM&w=2689&h=3981&q=king%20kong&client=safari&ved=2ahUKEwiRnNHnsauEAxW9FRAIHSNcDigQMygAegQIARBH"),
        ("Avatar", "Джейк Салли — бывший морской пехотинец, прикованный к инвалидному креслу. Несмотря на немощное тело, Джейк в душе по-прежнему остается воином. Он получает задание совершить путешествие в несколько световых лет к базе землян на планете Пандора, где корпорации добывают редкий минерал, имеющий огромное значение для выхода Земли из энергетического кризиса.", 8, "Научная фантастика/Боевик", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BZDA0OGQxNTItMDZkMC00N2UyLTg3MzMtYTJmNjg3Nzk5MzRiXkEyXkFqcGdeQXVyMjUzOTY1NTc%40._V1_FMjpg_UX1000_.jpg&tbnid=oq9Edn2Gx8VdmM&vet=12ahUKEwjru_TdsquEAxUuFhAIHX_wCjgQMygBegQIARBz..i&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0499549%2F&docid=Zn19HiGjooaZRM&w=1000&h=1477&q=avatar&client=safari&ved=2ahUKEwjru_TdsquEAxUuFhAIHX_wCjgQMygBegQIARBz")
        ''')
        self.connection.commit()

    def get_films(self):
        self.cursor.execute('SELECT * FROM films')
        return self.cursor.fetchall()

if __name__ == '__main__':
    db = DB_Film()
    db.create_tables()
    db.populate_tables()

