
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import  SQLAlchemy




app = Flask(__name__)

FLASK_DEBUG = True



# creating a configuration variable to set configurations
# app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://udacity:udacity@localhost:5432/example'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://udacity1:123@localhost:5432/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# linking to SQLALCHEMY
# represent an instance of our db
db = SQLAlchemy(app)



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
db.create_all()



@app.route("/")
def index():
    # return "Hello Flask Application"
    return render_template("index.html")



@app.route("/insert_artist", methods = ['POST'])
def insert():
    # checking if method is post
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        state = request.form['state']
        phone = request.form['phone']
        genres = request.form['genres']
        image_link = request.form['img_link']
        facebook_link = request.form['fb_link']

        my_artist =  Artist(name, city, state, phone, genres, image_link, facebook_link)
        db.session.add(my_artist)
        db.session.commit()

        return redirect(url_for('Index'))

    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)


