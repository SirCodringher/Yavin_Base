import random
import time

library_list = []
current_date = time.strftime("%d.%m.%Y", time.localtime())

class Movies:

    def __init__(self, title, year, type):
        self.title = title
        self.year = year
        self.type = type
        self.no_plays = 0
        library_list.append(self)

    def play(self, step=1):
        self.no_plays += step

    def __str__(self):
        return f"{self.title} {self.year}"

    def __repr__(self):
        return f"{self.title} {self.year}"


movie1 = Movies(title="Alien", year="1979", type="horror, sci-fi")
movie2 = Movies(title="Boondock Saints", year="1999", type="action, thriller")
movie3 = Movies(title="Star Wars: Episode II - Attack of the Clones", year="2002", type="action, adventure, sci-fi")
movie4 = Movies(title="The Fifth Element", year="1997", type="sci-fi, action, adventure")
movie5 = Movies(title="The Lord of the Rings: The Return of the King", year="2003", type="fantasy, adventure, drama")
movie6 = Movies(title="Life of Brian", year="1979", type="comedy")
movie7 = Movies(title="The Terminator", year="1984", type="Sci-Fi")
movie8 = Movies(title="Dune", year="2021", type="sci-fi, action")
movie9 = Movies(title="National Lampoon's Christmas Vacation", year="1989", type="comedy, family")
movie10 = Movies(title="Casino", year="1995", type="crime, drama")

class Series(Movies):

    def __init__(self, no_episode, no_season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.no_episode = no_episode
        self.no_season = no_season

    def play(self, step=1):
        self.no_plays += step

    def __str__(self):
        return f"{self.title} S{self.no_season}E{self.no_episode}"

    def __repr__(self):
        return f"{self.title} S{self.no_season}E{self.no_episode}"

series1 = Series(title="The Pacific", year="2010", type="drama", no_episode=1, no_season=1)
series2 = Series(title="Clone Wars", year="2008 - 2020 ", type="sci-fi", no_episode=1, no_season=1)
series3 = Series(title="The Big Bang Theory", year="2007 - 2019 ", type="comedy", no_episode=1, no_season=1)
series4 = Series(title="Game of Thrones", year="2011 - 2019", type="comedy", no_episode=1, no_season=1)
series5 = Series(title="The Sopranos", year="1999 - 2007 ", type="drama", no_episode=1, no_season=1)
series6 = Series(title="The Ranch", year="2016-2020", type="comedy", no_episode=1, no_season=1)
series7 = Series(title="Jackass", year="2000 - 2007", type="comedy", no_episode=1, no_season=1)
series8 = Series(title="Breaking Bad", year="2008 - 2013", type="thriller", no_episode=1, no_season=1)
series9 = Series(title="McGyver", year="1985 - 1992", type="thriller", no_episode=1, no_season=1)
series10 = Series(title="House M.D.", year="2004 - 2007", type="drama", no_episode=1, no_season=1)

def movies_list():
    movies = []
    for position in library_list:
        if type(position) == Movies:
            movies.append(position)
    return sorted(movies, key=lambda x: x.title, reverse=False)

def series_list():
    series = []
    for position in library_list:
        if type(position) == Series:
            series.append(position)
    return sorted(series, key=lambda x: x.title, reverse=False)

def search(title):
    for position in library_list:
        if title == position.title:
            return position

def generate_views():
    random_view = random.choice(library_list)
    random_no = random.randrange(1, 101)
    for position in library_list:
        if position == random_view: 
            position.play(step=random_no)

def generate_views_10():
    for view in range(10):
        generate_views()

def top_titles(content_type, number):
    movies_by_no_plays = []
    series_by_no_plays = []
    library_list_by_no_plays = sorted(library_list, key=lambda x: x.no_plays, reverse=True)
    if content_type == "Movies":
        for position in library_list_by_no_plays:
            if type(position) == Movies:
                movies_by_no_plays.append(position)
        print(movies_by_no_plays[:number])
    elif content_type == "Series":
        for position in library_list_by_no_plays:
            if type(position) == Series:
                series_by_no_plays.append(position)
        print(series_by_no_plays[:number])
    elif content_type == "All content":
        print(library_list_by_no_plays[:number])

    else:
        print("No content")


print('--------Biblioteka filmów--------')
for position in library_list:
    print(position)
generate_views_10()
print(f"----Najpopularniejsze filmy i seriale dnia {current_date}----")
top_titles("All content", 3)