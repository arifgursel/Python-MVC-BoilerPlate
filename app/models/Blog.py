""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
class Blog(Model):
    def __init__(self):
        super(Blog, self).__init__()

    #=========CRUD Methods==========
    #Read (*)
    def index(self):
        #get all blogs currently registered in the DB
        query = "SELECT * FROM blogs ORDER BY created_at DESC;";
        return self.db.query_db(query);
    #Read (1)
    def get_blog(self, id):
        #get a single blog by ID
        query = "SELECT * FROM blogs WHERE id={};".format(id);
        return self.db.query_db(query);
    #Create   
    def create_blog(self, blog_info):
        #create a new blog
        query = "INSERT INTO blogs (`user_id`, `headline`, `intro`, `content`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(blog_info['user_id'], blog_info['headline'], blog_info['intro'], blog_info['content']);
        return self.db.query_db(query);
    #Update
    def update_blog(self, blog_info):
        #update a single blog by passing JSON of blog information
        query = "UPDATE blogs SET `user_id`='{}', `headline`='{}', `intro`='{}', `content`='{}', `updated_at`=NOW() WHERE `id`='{}';".format(blog_info['user_id'], blog_info['headline'], blog_info['intro'], blog_info['content'], blog_info['id']);
        return self.db.query_db(query);
    #Delete
    def delete_blog(self, id):
        #Delete a single blog by ID
        query = "DELETE FROM blogs WHERE `id`={};".format(id);
        return self.db.query_db(query);
    #-------Custom Methods -----------
    def get_latest(self, numberOfPost):
        #get a single blog by ID
        query = "SELECT headline, intro, id FROM blogs ORDER BY id DESC LIMIT {}".format(numberOfPost);
        return self.db.query_db(query);
    