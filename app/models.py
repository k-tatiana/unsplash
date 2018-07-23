from app import db

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String, index=True, unique=True)
    image_desc = db.Column(db.String(255)),
    favorites = db.Column(db.Boolean, default=False)

    def add_image(self, image_url):
        if self.favorites == False:
            self.favorites = True

    def remove_image(self, image_url):
        if self.favorites == True:
            self.favorites = False

    def select_favorites(self):
        images = Images.query.filter_by(favorites=True)