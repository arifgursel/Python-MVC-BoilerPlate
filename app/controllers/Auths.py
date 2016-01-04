"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Auths(Controller):
    def __init__(self, action):
        super(Auths, self).__init__(action)
        self.load_model('Auth');
        self.load_model('User');

    def index(self):
        return self.load_view('index.html')

    def reset(self):
        session.clear()
        return redirect('/')
            
    def process_log(self):
        login_info = {'email': request.form['email'],
                      'password': request.form['password']}
        login_status = self.models['Auth'].process_log(login_info)
        if login_status['status'] == True:
            session['loggedIn'] = True 
            session['id'] = login_status['user']['id'] 
            session['first_name'] = login_status['user']['first_name']
            session['last_name'] = login_status['user']['last_name']
            session['type'] = login_status['user']['type']
            if session['type'] > 1:
                return redirect('/dashboard')
            else:
                return redirect('/blog')
        else:
            for error in login_status['errors']:
                flash(error)
            return redirect('/login')


