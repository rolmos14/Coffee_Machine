class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return '"' + self.title + '" by ' + self.artist + ' (' + self.year + ') hangs in the ' + self.museum + '.'


name, painter, date = [input() for _ in range(3)]
paint = Painting(name, painter, date)
print(paint)
