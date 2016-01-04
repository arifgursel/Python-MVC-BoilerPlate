""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
class User(Model):
    def __init__(self):
        super(User, self).__init__()

    #=========CRUD Methods==========
    #Read (*)
    def index(self):
        #get all users currently registered in the DB
        query = "SELECT * FROM users WHERE type < 4 ORDER BY type DESC;"
        return self.db.query_db(query);
    #Read (1)
    def get_user(self, id):
        #get a single user by ID
        query = "SELECT * FROM users WHERE id={};".format(id);
        return self.db.query_db(query);
    #Create   
    def create_user(self, user_info):
        #get a single user by ID
        query = "INSERT INTO users (`first_name`, `last_name`, `email`, `pw_hash`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(user_info['first_name'], user_info['last_name'], user_info['email'], user_info['pw_hash']);
        return self.db.query_db(query);
    #Update
    def update_user(self, user_info):
        #update a single user by passing JSON of user information
        query = "UPDATE users SET `first_name`='{}', `last_name`='{}', `email`='{}', `mobile`='{}', `twitter`='{}', `updated_at`=NOW() WHERE `id`='{}';".format(user_info['first_name'], user_info['last_name'], user_info['email'], user_info['mobile'], user_info['twitter'], user_info['id']);
        return self.db.query_db(query);
    #Delete
    def delete_user(self, id):
        #Delete a single user by ID
        query = "DELETE FROM users WHERE `id`={};".format(id);
        return self.db.query_db(query);
        
    #==========Special Methods For User Manipulation
    def get_latest_user(self):
        #get the last user added to DB
        query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
        return self.db.query_db(query);

    #Method to process new user registration, uses (C)rud call
    def process_reg(self, user_info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # some basic validations
        if not user_info['first_name']:
            errors.append('First name cannot be blank')
        elif len(user_info['first_name']) < 2:
            errors.append('First name must be at least 2 characters long')
        if not user_info['last_name']:
            errors.append('Last name cannot be blank')
        elif len(user_info['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        if not user_info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append('Enter valid email address')
        if not user_info['password1']:
            errors.append('Password cannot be blank')
        elif len(user_info['password1']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif user_info['password1'] != user_info['password2']:
            errors.append('Passwords must match!')
        # check if there are any errors, if there are any return the array
        # otherwise return True
        if errors:
            return {"status": False, "errors": errors}
        else:
            #Bcrypt the password
            password = user_info['password1']
            user_info['pw_hash'] = self.bcrypt.generate_password_hash(password)
            
            # code to insert reg info into DB goes here
            temp = self.create_user(user_info)
            print 'Creating User returns: ', temp
            # retrieve the last inserted user from above so you can return and save session info
            user = self.get_latest_user()
            return {"status": True, "user": user[0]} #always returns a list so we retrieve the first and hopefully only element
    #Make Admin
    def make_admin(self, id):
        print "ID: ", id
        query = "UPDATE users SET `type`= 1, `updated_at`= NOW() WHERE `id`={};".format(id);
        print "Query: ", query
        return self.db.query_db(query);
    
