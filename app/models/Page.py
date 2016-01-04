""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Rbr(Model):
    def __init__(self):
        super(Rbr, self).__init__()

     #=========CRUD Methods==========
    #Read (*)
    def index(self):
        #get all currently registered in the DB
        #query = "SELECT * FROM rbr;";
        #return self.db.query_db(query);
        pass
    
    #Read (1)
    def get_rbr(self, id):
        #get a single item by ID
        query = "SELECT * FROM rbr WHERE id={};".format(id);
        return self.db.query_db(query);
    
    #Create   
    def create_rbr(self, rbr_info):
        #create an item
        query = "INSERT INTO rbr (`x`, `x`, `x`, `x`, `created_at`, `updated_at`) VALUES ({}, {}, {}, {}, NOW(), NOW());".format(rbr_info.x, rbr_info.x, rbr_info.x, rbr_info.x);
        return self.db.query_db(query);
    
    #Update
    def update_rbr(self, rbr_info):
        #update a single item by passing JSON information of item
        query = "UPDATE rbr SET `x`={}, `x`={}, `x`={}, `updated_at`=NOW() WHERE `id`={};".format(rbr_info.x, rbr_info.x, rbr_info.x, rbr_info.x);
        return self.db.query_db(query);
    
    #Destroy
    def destroy_rbr(self, id):
        #Delete an item by ID
        query = "DELETE FROM rbr WHERE `id`={};".format(id);
        return self.db.query_db(query);

    #==========Additional Methods
    #Validate correctness of data for create/update methods
    def validate_rbr(self, data): #Flash processing for validation
        errors = []
        # some basic validations on data
        if not data:
            errors.append('No data recieved!')
        # check if there are any errors, if there are any return the array
        if errors:
            return {"status": False, "errors": errors}
        # otherwise return True
        else:
            return {"status": True, "data": data}
                

