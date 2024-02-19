import sqlite3
from pathlib import Path
from pprint import pprint

class DB_Film:
    def __init__(self):
        self.connection = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('DROP TABLE IF EXISTS genres')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre TEXT
        )
        ''')
        self.cursor.execute('DROP TABLE IF EXISTS films')
        self.cursor.execute("""
        CREATE TABLE films (
        top INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        rating INTEGER,
        image TEXT,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES genres (id)
        )
        """)

    def populate_tables(self):
        self.cursor.execute('''INSERT INTO genres (genre) VALUES
        ("Боевик"),
        ("Комедия"),
        ("Романтика"),
        ("Мистика"),
        ("Фантастика"),
        ("Приключения")
        ''')
        self.cursor.execute('''
        iNSERT INTO films (name, description, rating, genre_id, image) VALUES
        ("Kingsman", "«Kingsman» — организация супершпионов, действующая на благо человечества вдали от любопытных глаз.", 7.7, 1, "https://s6.vcdn.biz/static/f/782641401/image.jpg/pt/r375x0x4"),
        ("Titanic", "В первом и последнем плавании шикарного «Титаника» встречаются двое. Пассажир нижней палубы Джек выиграл билет в карты, а богатая наследница Роза отправляется в Америку, чтобы выйти замуж по расчёту.", 8.4, 3, "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.kino-teatr.ru%2Fmovie%2Fposters%2Fbig%2F2%2F19522.jpg&tbnid=B4XJBBm0364JmM&vet=12ahUKEwjr4fqzr6uEAxWeQ1UIHcYnCC8QMygEegQIARBQ..i&imgrefurl=https%3A%2F%2Fwww.kino-teatr.ru%2Fkino%2Fmovie%2Fhollywood%2F19522%2Fannot%2F&docid=0bKn-PR__j59CM&w=300&h=434&q=титаник%20жанр&client=safari&ved=2ahUKEwjr4fqzr6uEAxWeQ1UIHcYnCC8QMygEegQIARBQ"),
        ("King Kong", "В 1930-м году съемочная группа под предводительством режиссера-неудачника Карла Дэнхэма отправляется на загадочный Остров Черепа неподалеку от Суматры, чтобы изучать легенды о гигантской горилле по кличке Конг.", 7.6, 1,"https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BMjYxYmRlZWYtMzAwNC00MDA1LWJjNTItOTBjMzlhNGMzYzk3XkEyXkFqcGdeQXVyMTQxNzMzNDI%40._V1_.jpg&tbnid=GGxXoBAjNWRriM&vet=12ahUKEwiRnNHnsauEAxW9FRAIHSNcDigQMygAegQIARBH..i&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0360717%2F&docid=TpLz7eSbBmhejM&w=2689&h=3981&q=king%20kong&client=safari&ved=2ahUKEwiRnNHnsauEAxW9FRAIHSNcDigQMygAegQIARBH"),
        ("Avatar", "Джейк Салли — бывший морской пехотинец, прикованный к инвалидному креслу. Несмотря на немощное тело, Джейк в душе по-прежнему остается воином. Он получает задание совершить путешествие в несколько световых лет к базе землян на планете Пандора, где корпорации добывают редкий минерал, имеющий огромное значение для выхода Земли из энергетического кризиса.", 8, 5, "https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BZDA0OGQxNTItMDZkMC00N2UyLTg3MzMtYTJmNjg3Nzk5MzRiXkEyXkFqcGdeQXVyMjUzOTY1NTc%40._V1_FMjpg_UX1000_.jpg&tbnid=oq9Edn2Gx8VdmM&vet=12ahUKEwjru_TdsquEAxUuFhAIHX_wCjgQMygBegQIARBz..i&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0499549%2F&docid=Zn19HiGjooaZRM&w=1000&h=1477&q=avatar&client=safari&ved=2ahUKEwjru_TdsquEAxUuFhAIHX_wCjgQMygBegQIARBz"),
        ("Один Дома", "Американское семейство отправляется из Чикаго в Европу, но в спешке сборов бестолковые родители забывают дома… одного из своих детей. Юное создание, однако, не теряется и демонстрирует чудеса изобретательности. И когда в дом залезают грабители, им приходится не раз пожалеть о встрече с милым крошкой.", 8.3, 2, "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fru%2F0%2F03%2FHome_Alone_dvd_rus.jpg&tbnid=fYLuNMbjTKgY_M&vet=12ahUKEwifx_bNn7eEAxWyQ1UIHXZcDFEQMygAegQIARBJ..i&imgrefurl=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%259E%25D0%25B4%25D0%25B8%25D0%25BD_%25D0%25B4%25D0%25BE%25D0%25BC%25D0%25B0&docid=gu-15N4PJNrM3M&w=1642&h=2325&q=один%20дома&client=safari&ved=2ahUKEwifx_bNn7eEAxWyQ1UIHXZcDFEQMygAegQIARBJ"),
        ("Мгла", "Маленький городок накрывает сверхъестественный туман, отрезая людей от внешнего мира. Группе героев, оказавшихся в этот момент в супермаркете, приходится вступить в неравный бой с обитающими в тумане монстрами.", 7.6, 4, "https://www.google.com/imgres?imgurl=https%3A%2F%2Favatars.mds.yandex.net%2Fget-kinopoisk-image%2F1600647%2Fe365ec59-b8ba-4d2c-b068-0c472832a47e%2F600x900&tbnid=od-2pXht7YaDkM&vet=12ahUKEwj93tzDoLeEAxVoDhAIHTh4BaQQMygAegQIARBg..i&imgrefurl=https%3A%2F%2Fwww.kinopoisk.ru%2Ffilm%2F273302%2F&docid=vVzz0tbL18ZOgM&w=552&h=827&q=мгла&client=safari&ved=2ahUKEwj93tzDoLeEAxVoDhAIHTh4BaQQMygAegQIARBg"),
        ("Интерстеллар", "Наше время на Земле подошло к концу, команда исследователей берет на себя самую важную миссию в истории человечества; путешествуя за пределами нашей галактики, чтобы узнать есть ли у человечества будущее среди звезд.", 8.6, 5, "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fru%2Fc%2Fc3%2FInterstellar_2014.jpg&tbnid=xoGCyiYEzMuvhM&vet=12ahUKEwjCwtyCobeEAxVuIhAIHYEGC8EQMygAegQIARBB..i&imgrefurl=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%2598%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D1%2581%25D1%2582%25D0%25B5%25D0%25BB%25D0%25BB%25D0%25B0%25D1%2580&docid=WRNQlH1Uayce9M&w=405&h=564&q=интерстеллар&client=safari&ved=2ahUKEwjCwtyCobeEAxVuIhAIHYEGC8EQMygAegQIARBB"),
        ("Пираты Карибского Моря", "В новой истории о поисках истины, предательстве, вечной молодости и смертельной опасности капитану Джеку Воробью предстоит столкнуться с женщиной из своего прошлого Анжеликой. До самого конца не будет понятно, связывает ли их настоящая любовь, или же Анжелика искусно притворяется, чтобы вместе с Джеком добраться до таинственного источника вечной молодости.", 7.3, 6, "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fru%2F7%2F79%2FPotC_ost.jpg&tbnid=qDJrvL511B-o5M&vet=12ahUKEwjSpa3CobeEAxUOKhAIHcK4C8kQMygAegQIARBD..i&imgrefurl=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%259F%25D0%25B8%25D1%2580%25D0%25B0%25D1%2582%25D1%258B_%25D0%259A%25D0%25B0%25D1%2580%25D0%25B8%25D0%25B1%25D1%2581%25D0%25BA%25D0%25BE%25D0%25B3%25D0%25BE_%25D0%25BC%25D0%25BE%25D1%2580%25D1%258F%3A_%25D0%259D%25D0%25B0_%25D1%2581%25D1%2582%25D1%2580%25D0%25B0%25D0%25BD%25D0%25BD%25D1%258B%25D1%2585_%25D0%25B1%25D0%25B5%25D1%2580%25D0%25B5%25D0%25B3%25D0%25B0%25D1%2585&docid=vdRqb4dZOrxrXM&w=350&h=500&q=Пираты%20Карибского%20моря%3A%20На%20странных%20берегах&client=safari&ved=2ahUKEwjSpa3CobeEAxUOKhAIHcK4C8kQMygAegQIARBD")
        ''')
        self.connection.commit()

    def get_films(self):
        self.cursor.execute('SELECT * FROM films')
        return self.cursor.fetchall()

    def get_films_by_genre_name(self, genre_name):
        self.cursor.execute('''
        SELECT f.name, f.description, f.rating, f.image
        FROM films AS f
        JOIN genres AS g ON f.genre_id = g.id
        WHERE g.genre = :genre_name
        ''',
                            {'genre_name':genre_name}
        )
        return self.cursor.fetchall()

if __name__ == '__main__':
    db = DB_Film()
    db.create_tables()
    db.populate_tables()
    # pprint(db.get_films_by_genre_name('Приключения'))
