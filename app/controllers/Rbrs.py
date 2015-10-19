"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Rbrs(Controller):
    def __init__(self, action):
        super(Rbrs, self).__init__(action)
        self.load_model('Rbr')
        
    #Read (*)
    def index(self):    
        rbrs = self.models['Rbr'].index()
        return self.load_view('postauth/postauth.html', rbrs=rbrs)
    
    #Read (1)
    def get_rbr(self, id):
        rbr = self.models['Rbr'].get_rbr(id)
        print 'Got user info: ', rbr
        return self.load_view('postauth/rbr.html', rbr=rbr)

    #Update
    def update_rbr(self, id):
        #Get form data and assign to variables
        rbr = get_rbr(id)
        rbr_info = { }
        #Call model to process data by passign appropriate variables
        self.models['Rbr'].update_rbr(rbr_info)
        #return True to indicate completion
        return redirect('/rbr')
    #Create
    def create_rbr(self):
        #Get form data and assign to variables
        rbr_info = {xxx: request.form['xxx'],
                         xxx: request.form['xxx']
                    }
        #Call model to create user 
        self.models['Rbr'].create_rbr(rbr_info)
        return redirect('/rbr')
    
    #Delete
    def delete_rbr(self, id):
        self.models['Rbr'].delete_rbr(id)
        #return True to indicate completion
        return redirect('/rbr')

    
    
    