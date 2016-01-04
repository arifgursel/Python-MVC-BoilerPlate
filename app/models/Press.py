""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
class Press(Model):
    def __init__(self):
        super(Press, self).__init__()

    #=========CRUD Methods==========
    #Read (*)
    def index(self, artist_id):
        #get all Press currently registered in the DB
        query = "SELECT * FROM artist_press WHERE artist_id={} ORDER BY created_at DESC;".format(artist_id)
        return self.db.query_db(query)
    #Read (1)
    def get_press(self, id):
        #get a single blog by ID
        query = "SELECT * FROM artist_press WHERE id={};".format(id)
        return self.db.query_db(query)
    #Create   
    def create_press(self, press_info):
        #create a new blog
        query = "INSERT INTO artist_press (`artist_id`, `headline`, `intro`, `content`, `writer`, `publisher`, `url`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', NOW(), NOW())".format(press_info['artist_id'], press_info['headline'], press_info['intro'], press_info['content'], press_info['writer'], press_info['publisher'], press_info['url'])
        return self.db.query_db(query)
    #Update
    def update_press(self, press_info):
        #update a single blog by passing JSON of blog information
        query = "UPDATE artist_press SET `artist_id`='{}', `headline`='{}', `intro`='{}', `content`='{}', `writer`='{}', `publisher`='{}', `url`='{}', `updated_at`= NOW() WHERE `id`='{}';".format(press_info['artist_id'], press_info['headline'], press_info['intro'], press_info['content'], press_info['writer'], press_info['publisher'], press_info['url'], press_info['id'])
        return self.db.query_db(query)
    #Delete
    def delete_press(self, id):
        #Delete a single blog by ID
        query = "DELETE FROM artist_press WHERE `id`= {};".format(id)
        return self.db.query_db(query)
    #Delete All
    def delete_all_press(self, artist_id):
        #Delete a single blog by ID
        query = "DELETE FROM artist_press WHERE `artist_id`= {};".format(artist_id)
        return self.db.query_db(query)
    