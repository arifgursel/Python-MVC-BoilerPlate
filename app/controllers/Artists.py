"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Artists(Controller):
    def __init__(self, action):
        super(Artists, self).__init__(action)
        self.load_model('Artist');
        self.load_model('Press');
        self.load_model('Album');

    ##-----Artist Basic Profile CRUD ------## 
    #Check Auth and Serve View
    def newArtist(self):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                return self.load_view('/postauth/newArtist.html')
        except KeyError:
                return redirect('/login')
    #Create
    def create_artist(self):
        #Get form data and assign to variables
        artist_info = {'name': request.form['name'],
                     'bio': request.form['bio'],
                     'instrument': request.form['instrument']
                     };
        #Call model to create Artist 
        self.models['Artist'].create_artist(artist_info);
        return redirect('/artists')  
    #Read (*)
    def get_roster(self):
        #get all Artists and display    
        artists = self.models['Artist'].get_roster()
        return self.load_view('postauth/artistManagement.html', artists=artists)
    #Read (1)
    def get_artist(self, id):
        #get a single Artist and display
        artist = self.models['Artist'].get_artist(id);
        return self.load_view('postauth/artistBasicProfile.html', artist=artist[0]) 
    #Update
    def update_artist(self, id):
        #Get form data and update a Artists info
        artist_info = {'name': request.form['name'],
                     'bio': request.form['bio'],
                     'instrument': request.form['instrument'],
                     'id': id
                     };
        print 'Updating artist info with: ', artist_info
        #Call model to get Artist
        self.models['Artist'].update_artist(artist_info)
        #Serve up the page to finalize process
        return redirect('/artists/profile/full/{}'.format(id))
    #Deactivate
    def deactivate_artist(self, id):
        #Call model to delete Artist
        self.models['Artist'].deactivate(id)
        return redirect('/artists')
    #Deactivate
    def activate_artist(self, id):
        #Call model to delete Artist
        self.models['Artist'].activate(id)
        return redirect('/artists')
    #Delete
    def delete_artist(self, id):
        #Call model to delete Artist Press
        self.models['Press'].delete_all_press(id)
        #Call model to delete Artist
        self.models['Artist'].delete_profile(id)
        #Call model to delete Artist
        self.models['Artist'].delete_digital(id)
        #Call model to delete Artist
        self.models['Artist'].delete_artist(id)
    
        #Serve up the page to finalize process
        return redirect('/artists')
    ##-----Artist Detailed Profile CRUD ------##
    #Check Auth and Serve View
    def newDetailProfile(self, artist_id):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                return self.load_view('/postauth/newDetailProfile.html', artist_id=artist_id)
        except KeyError:
                return redirect('/login')
    #Create
    def create_detailed_profile(self, artist_id):
        #Get form data and assign to variables
        artist_profile_info = {'composer': request.form['composer'],
                         'arranger': request.form['arranger'],
                         'clinic': request.form['clinic'],
                         'residency': request.form['residency'],
                         'artist_id': artist_id
                         };
        #Call model to create Artist 
        value = self.models['Artist'].create_profile(artist_profile_info)
        print "Added profile and got: ", value
        self.models['Artist'].toggleProfileOn(artist_id)
        return redirect('/artists')  
    #Read
    def get_detailed_profile(self, artist_id):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                #get a single Artist and display
                artist = self.models['Artist'].get_profile(artist_id);
                return self.load_view('postauth/artistDetailProfile.html', artist=artist[0], artist_id=artist_id)
        except KeyError:
                return redirect('/login')
    #Update
    def update_detailed_profile(self, artist_id):
        #Get form data and update a Artists info
        artist_profile_info = {'composer': request.form['composer'],
                         'arranger': request.form['arranger'],
                         'clinic': request.form['clinic'],
                         'residency': request.form['residency'],
                         'artist_id': artist_id
                         };
        self.models['Artist'].update_profile(artist_profile_info)
        #Serve up the page to finalize process
        return redirect('/artists/profile/full/{}'.format(artist_id))
    #Delete
    def delete_detailed_profile(self, artist_id):
        #Call model delete profile method
        value = self.models['Artist'].delete_profile(artist_id)
        print "Deleted profile and got: ", value
        self.models['Artist'].toggleProfileOff(artist_id)
        #Serve up the page to finalize process
        return redirect('/artists')

    ##-----Artist Digital Profile CRUD ------##
    #Check Auth and Serve Views
    def newDigitalProfile(self, artist_id):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                return self.load_view('/postauth/newDigitalProfile.html', artist_id=artist_id)
        except KeyError:
                return redirect('/login')
    #Read
    def get_digital_profile(self, artist_id):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                #get a single Artist and display
                artist = self.models['Artist'].get_digital(artist_id);
                return self.load_view('postauth/artistDigitalProfile.html', artist=artist[0], artist_id=artist_id)
        except KeyError:
                return redirect('/login')
    #Update
    def update_digital_profile(self, artist_id):
        #Get form data and update a Artists info
        artist_digital_info = {'website': request.form['website'],
                         'calendar': request.form['calendar'],
                         'facebook': request.form['facebook'],
                         'twitter': request.form['twitter'],
                         'instagram': request.form['instagram'],
                         'artist_id': artist_id
                         };
        self.models['Artist'].update_digital(artist_digital_info)
        #Serve up the page to finalize process
        return redirect('/artists/profile/full/{}'.format(artist_id))
    #Create
    def create_digital_profile(self, artist_id):
        #Get form data and assign to variables
        artist_digital_info = {'website': request.form['website'],
                               'calendar': request.form['calendar'],
                               'facebook': request.form['facebook'],
                               'twitter': request.form['twitter'],
                               'instagram': request.form['instagram'],
                               'artist_id': artist_id
                                };
        print "artist_digital_info: ", artist_digital_info
        #Call model to create Artist 
        value = self.models['Artist'].create_digital(artist_digital_info)
        print "Added digital and got: ", value
        self.models['Artist'].toggleDigitalOn(artist_id)
        return redirect('/artists')  
    #Delete
    def delete_digital_profile(self, artist_id):
        #Call model delete profile method
        value = self.models['Artist'].delete_digital(artist_id)
        print "Deleted and got: ", value
        self.models['Artist'].toggleDigitalOff(artist_id)
        #Serve up the page to finalize process
        return redirect('/artists')
##-----Artist Full Profile CRUD ------##
    #Check Auth and Serve Views
    def get_artist_full_profile(self, artist_id):
        ###Full Profile [Baisc+Detail+Social]
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                #get full profile & display
                artistList = self.models['Artist'].get_artist_full_profile(artist_id);
                print 'Getting and displaying: ', artistList
                return self.load_view('/postauth/artistFullProfile.html', artist=artistList[0])
        except KeyError:
                return redirect('/login')