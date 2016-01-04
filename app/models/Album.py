""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
class Album(Model):
    def __init__(self):
        super(Album, self).__init__()

    #=========CRUD Methods==========
    #Read (*)
    def index(self):
        #get all Press currently registered in the DB
        query = "SELECT * FROM artist_albums ORDER BY created_at DESC;"
        return self.db.query_db(query)
    #Read (1)
    def get_album(self, id):
        #get a single blog by ID
        query = "SELECT * FROM artist_albums WHERE id={};".format(id)
        return self.db.query_db(query)
    #Create   
    def create_album(self, album_info):
        #create a new blog
        query = "INSERT INTO artist_albums (`artist_id`, `headline`, `intro`, `content`, `author`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', '{}', '{}', NOW(), NOW())".format(album_info['artist_id'], album_info['headline'], album_info['intro'], album_info['content'], album_info['author'])
        return self.db.query_db(query)
    #Update
    def update_album(self, album_info):
        #update a single blog by passing JSON of blog information
        query = "UPDATE artist_albums SET `artist_id`='{}', `headline`='{}', `intro`='{}', `content`='{}', `author`='{}', `updated_at`=NOW() WHERE `id`='{}';".format(album_info['artist_id'], album_info['headline'], album_info['intro'], album_info['content'], album_info['author'], album_info['id'])
        return self.db.query_db(query)
    #Delete
    def delete_album(self, id):
        #Delete a single blog by ID
        query = "DELETE FROM artist_albums WHERE `id`= {};".format(id)
        return self.db.query_db(query)
    #Delete All
    def delete_all_albums(self, artist_id):
        #Delete a single blog by ID
        query = "DELETE FROM artist_albums WHERE `artist_id`= {};".format(artist_id)
        return self.db.query_db(query)
    