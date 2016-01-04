"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class PressList(Controller):
    def __init__(self, action):
        super(PressList, self).__init__(action)
        self.load_model('Press'); 
    #Read (*)
    def index(self, artist_id):
        #get all press and display    
        pressList = self.models['Press'].index(artist_id)
        return self.load_view('postauth/pressManagement.html', pressList=pressList, artist_id=artist_id)
    #Read (1)
    def get_press(self, artist_id, id):
        #get a single pres and display
        press = self.models['Press'].get_press(id);
        return self.load_view('postauth/editPress.html', press=press[0], artist_id=artist_id, id=id) 

    #Update
    def update_press(self, artist_id, id):
        #Get form data and update a press info
        press_info = {'artist_id': artist_id,
                     'writer': request.form['writer'],
                     'publisher': request.form['publisher'],
                     'headline': request.form['headline'],
                     'intro': request.form['intro'],
                     'content': request.form['content'],
                     'url': request.form['url'],
                     'id': id
                     };
        #Call model to update pres
        self.models['Press'].update_press(press_info)
        #Serve up the page to finalize process
        return redirect('/press/{}'.format(artist_id))
    
    #Create
    def create_press(self, artist_id):
        #Get form data and assign to variables
        press_info = {'writer': request.form['writer'],
                     'publisher': request.form['publisher'],
                     'headline': request.form['headline'],
                     'intro': request.form['intro'],
                     'content': request.form['content'],
                     'url': request.form['url'],
                     'artist_id': artist_id
                     };
        #Call model to create pres 
        self.models['Press'].create_press(press_info);
        return redirect('/press/{}'.format(artist_id))
    
    #Delete
    def delete_press(self, artist_id, id):
        #Call model to get pres
        self.models['Press'].delete_press(id)
        #Serve up the page to finalize process
        return redirect('/press/{}'.format(artist_id))

    #Delete All Post
    def delete_all_press(self, artist_id):
        #Call model to get pres
        self.models['Press'].delete_all_press(artist_id)
        #Serve up the page to finalize process
        return redirect('/press/{}'.format(artist_id))
    
    #pres management page
    def managepress(self, artist_id):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                press = self.models['Press'].index()
                return self.load_view('postauth/pressManagement.html', press=press, artist_id=artist_id)
        except KeyError:
                return redirect('/login')
    def newPress(self, artist_id):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                return self.load_view('/postauth/newPress.html', artist_id=artist_id)
        except KeyError:
                return redirect('/login')
    
    

