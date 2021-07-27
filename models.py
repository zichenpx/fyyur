#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)

moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
# TODO: connect to a local postgresql database
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Venue(db.Model):
  __tablename__ = 'venue'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120))
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  genres = db.Column(db.String(500))
  website_link = db.Column(db.String(500))
  seeking_talent = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.String) 
  shows = db.relationship('Show', backref='venue', lazy='joined', cascade='all, delete')
  # Note: The above configuration establishes a collection of Show objects on Venue called Venue.shows.

  def __repr__(self):
    return f'<Venue {self.id} {self.name}>'

class Artist(db.Model):
  __tablename__ = 'artist'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  website_link = db.Column(db.String(500))
  seeking_venue = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.String(500))
  shows = db.relationship('Show', backref='artist', lazy='joined', cascade='all, delete')
  
  def __repr__(self):
    return f'<Artist {self.id} {self.name}>'

class Show(db.Model):
  __tablename__ = 'show'

  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
  start_time = db.Column(db.DateTime)
  
  def __repr__(self):
    # return f'<Show {self.id}, Artist {self.artist_id}, Venue {self.venue_id}, Start time: {self.start_time}>'
    return 'Show(%s, %s, %s)' % (self.venue_id, self.artist_id, self.start_time)

# TODO Implem,ent Show and Artist models, and complete all model relationships and properties, as a database migration.
