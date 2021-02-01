from app import db
from sqlalchemy.exc import IntegrityError

class Film(db.Model):

    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    film_name = db.Column(db.String(128), nullable=False)
    img_url = db.Column(db.Text, nullable=False)
    release_year = db.Column(db.Integer)
    summary = db.Column(db.String(128))
    director = db.Column(db.String(128))
    genre = db.Column(db.String(128))
    rating = db.Column(db.String(128))
    film_runtime = db.Column(db.Integer)
    meta_score = db.Column(db.Integer)

    def __init__(self, film_name, img_url, release_year, summary, director, genre, rating, film_runtime, meta_score):

        self.film_name = film_name
        self.img_url = img_url
        self.release_year = release_year
        self.summary = summary
        self.director = director
        self.genre = genre
        self.rating = rating
        self.film_runtime = film_runtime
        self.meta_score = meta_score

    def save(self):
        print(self, "hello in model add")
        db.session.add(self)
        try:
            db.session.commit()
            return True, self.id
        except IntegrityError:
            return False, None

    def delete(film_id):
        print(film_id, "hello in model delete")
        film_to_delete = Film.query.filter_by(id=film_id).first()
        db.session.delete(film_to_delete)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

            
    def update(film_id, self):
        film_to_update = Film.query.filter_by(id=film_id).first()
        # print(film_to_update.film_name, "heeeeeeeeeeeeeeeeere")
        if not film_to_update:
          return
        else:
          film_to_update.film_name = self.film_name
          film_to_update.img_url = self.img_url
          film_to_update.release_year = self.release_year
          film_to_update.summary = self.summary
          film_to_update.director = self.director
          film_to_update.genre = self.genre
          film_to_update.rating = self.rating
          film_to_update.film_runtime = self.film_runtime
          film_to_update.meta_score = self.meta_score
          try:
              db.session.commit()
              return True, self.id
          except IntegrityError:
              print("i am an error")
              return False, None
              db.session.commit()

    
    @staticmethod
    def get_all_films():
      return Film.query.all()
    
    @staticmethod
    def get_one_film(id):
      return BlogpostModel.query.get(id)

    def __repr__(self):
      return '<id {}>'.format(self.id)


    @property
    def films_serializer(film):
      return {
        'id': film.id,
        'film_name': film.film_name,
        'img_url': film.img_url,
        'release_year': film.release_year,
        'summary': film.summary,
        'director': film.director,
        'genre': film.genre,
        'rating': film.rating,
        'film_runtime': film.film_runtime,
        'meta_score': film.film_runtime
        }
