"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Pages(Controller):
    def __init__(self, action):
        super(Pages, self).__init__(action)
        self.load_model('Artist');
        self.load_model('Blog');
        self.load_model('User');
        self.load_model('Press');

        
    #serve static pages
    def index(self):
        numberOfPost = 3
        news = self.models['Blog'].get_latest(numberOfPost)
        return self.load_view('index.html', news=news)
    def about(self):
        return self.load_view('about.html')
    def contact(self):
        staffMembers = self.models['User'].index()
        return self.load_view('contact.html', staffMembers=staffMembers)
    def roster(self):
        roster = self.models['Artist'].index()
        return self.load_view('roster.html', roster=roster)
    def services(self):
        return self.load_view('services.html')
    def artist(self, id):
        artist = self.models['Artist'].get_artist_full_profile(id);
        pressList = self.models['Press'].index(id)
        albums = [{'name': 'jksdnckjsnklsa', 'label': 'John Doe'},
                     {'name': 'jksdnckjsnklsa', 'label': 'John Doe'},
                     {'name': 'jksdnckjsnklsa', 'label': 'John Doe'}]
        return self.load_view('artist.html', artist=artist[0], pressList=pressList, albums=albums)
    def blog(self):
        blogs = self.models['Blog'].index();
        return self.load_view('blog.html', blogs=blogs)
    def blogPost(self, id):
        blog = self.models['Blog'].get_blog(id);
        print "Passing: ", blog
        return self.load_view('blogPost.html', blog=blog[0])
    def login(self):
        return self.load_view('login.html')
    #======Post Auth Methods=========#
    def dashboard(self):
        try:
            if session['loggedIn'] == True and session['type'] >= 1:
                return self.load_view('/postauth/dashboard.html')
        except KeyError:
                return redirect('/login')
    def artists(self):
        try:
            if session['loggedIn'] == True and session['type'] >= 1:
                return self.load_view('/postauth/artists.html')
        except KeyError:
                return redirect('/login')
    
    

    

    

