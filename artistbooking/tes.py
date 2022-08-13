

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # Todo implement any missing fields, as a database migration using Flask-Migrate

    def __init__(self, name, city, state, address, phone, image_link, facebook_link):
        self.name = name
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        image_link = image_link
        facebook_link = facebook_link


    def __repr__(self):
        return f'<Venue ID: {self.id}, name: {self.name}>'
    

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # Todo: implement any missing fields, as a database migration using Flask-Migrate
    def __repr__(self):
        return f'<Artist ID: {self.id}, name: {self.name}>'
    

    def __init__(self, name, city, state, phone, genres, image_link, facebook_link):
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.genres = genres
        self.image_link = image_link
        self.facebook_link = facebook_link
    

# Todo Implement Show and Artist models, and complete all model relationships and properties, as a database migration.






# artist = Artist(name='Guns N Petals', city='San Francisco', state="CA", 
# phone="326-123-5000", genres="Rock n Roll", 
# image="https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80", facebook_link="https://www.facebook.com/GunsNPetals")

# db.session.add(artist)
# db.session.commit()#  __tablename__ = 'my_custom_table_name'.


# create tables for models
# db.create_all()



