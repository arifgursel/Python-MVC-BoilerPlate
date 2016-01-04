"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Albums(Controller):
    def __init__(self, action):
        super(Albums, self).__init__(action)
        self.load_model('Album'); 
    #Read (*)
    def index(self, artist_id):
        #get all album and display    
        albums = self.models['Album'].index(artist_id)
        return self.load_view('postauth/albumManagement.html', albums=albums)
    #Read (1)
    def get_album(self, id):
        #get a single pres and display
        album = self.models['Album'].get_album(id);
        return self.load_view('postauth/editalbum.html', album=album[0]) 

    #Update
    def update_album(self, id, artist_id):
        #Get form data and update a album info
        album_info = {'artist_id': artist_id,
                     'writer': request.form['writer'],
                     'publisher': request.form['publisher'],
                     'headline': request.form['headline'],
                     'intro': request.form['intro'],
                     'content': request.form['content'],
                     'url': request.form['url'],
                     'id': id
                     };
        #Call model to update pres
        self.models['Album'].update_album(album_info)
        #Serve up the page to finalize process
        return redirect('/album')
    
    #Create
    def create_album(self, artist_id):
        #Get form data and assign to variables
        album_info = {'writer': request.form['writer'],
                     'publisher': request.form['publisher'],
                     'headline': request.form['headline'],
                     'intro': request.form['intro'],
                     'content': request.form['content'],
                     'url': request.form['url'],
                     'artist_id': artist_id
                     };
        #Call model to create pres 
        self.models['Album'].create_album(album_info);
        return redirect('/album')  
    
    #Delete
    def delete_album(self, id):
        #Call model to get pres
        self.models['Album'].delete_album(id)
        #Serve up the page to finalize process
        return redirect('/album')

    #Delete All Post
    def delete_all_albums(self, artist_id):
        #Call model to get pres
        self.models['Album'].delete_all_albums(artist_id)
        #Serve up the page to finalize process
        return redirect('/album')
    
    #pres management page
    def manageAlbum(self):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                album = self.models['Album'].index()
                return self.load_view('postauth/albumManagement.html', album=album)
        except KeyError:
                return redirect('/login')
    def newAlbum(self):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                return self.load_view('/postauth/newAlbum.html')
        except KeyError:
                return redirect('/login')
    
    

