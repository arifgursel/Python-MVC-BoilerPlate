"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User');
        
    #Read (*)
    def index(self):
        #get all users and display    
        users = self.models['User'].index()
        return self.load_view('postauth/userManagement.html', users=users)
    #Read (1)
    def get_user(self, id):
        #get a single user and display
        user = self.models['User'].get_user(id);
        print 'Getting and displaying: ', user
        return self.load_view('postauth/user.html', user=user[0]) 
    #Update
    def update_user(self, id):
        #Get form data and update a users info
        user_info = {'first_name': request.form['first_name'],
                     'last_name': request.form['last_name'],
                     'email': request.form['email'],
                     'mobile': request.form['mobile'],
                     'twitter': request.form['twitter'],
                     'id': id
                     };
        print 'Updating user info with: ', user_info
        #Call model to get user
        self.models['User'].update_user(user_info)
        #Serve up the page to finalize process
        return redirect('/users')

    #Create
    def create_user(self):
        #Get form data and assign to variables
        user_info = {'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'email': request.form['email'],
                    'password1': request.form['password1'],
                    'password2': request.form['password2']
                    };
        #Call model to create user 
        self.models['User'].process_reg(user_info);
        return redirect('/users')
    
    #Delete
    def delete_user(self, id):
        #Call model to get user
        self.models['User'].delete_user(id)
        #Serve up the page to finalize process
        return redirect('/users')

    #-----------User Methods ------------#
    def newStaff(self):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                return self.load_view('/postauth/newStaff.html')
        except KeyError:
                return redirect('/login')
                
    def process_reg(self):
        user_info = {'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'email': request.form['email'],
                    'password1': request.form['password1'],
                    'password2': request.form['password2']
                    };
        print 'Heres what we got from the form:', user_info;
        #New User registration handled by the User model
        reg_status = self.models['User'].process_reg(user_info);
        if reg_status['status'] == True:
            session['id'] = reg_status['user']['id'];
            session['first_name'] = reg_status['user']['first_name'];
            session['last_name'] = reg_status['user']['last_name'];
            return redirect('/dashboard');
        else:
            for error in reg_status['errors']:
                flash(error);
            return redirect('/login');

    def make_admin(self, id):
        print "ID: ", id
        self.models['User'].make_admin(id)
        #Serve up the page to finalize process
        return redirect('/users')


    

