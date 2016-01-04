"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Blogs(Controller):
    def __init__(self, action):
        super(Blogs, self).__init__(action)
        self.load_model('Blog'); 
    #Read (*)
    def index(self):
        #get all blogs and display    
        blogs = self.models['Blog'].index()
        return self.load_view('postauth/blogManagement.html', blogs=blogs)
    #Read (1)
    def get_blog(self, id):
        #get a single Blog and display
        blog = self.models['Blog'].get_blog(id);
        return self.load_view('postauth/editBlog.html', blog=blog[0]) 
    #Front Page News Feed
    def get_latest(self):
        numberOfPost = 3
        #get a single Blog and display
        news = self.models['Blog'].get_latest(numberOfPost);
        return self.load_view('index.html', news=news)

    #------Post Auth Blog Management --------#
    
    #Update
    def update_blog(self, id):
        #Get form data and update a blogs info
        blog_info = {'user_id': session['id'],
                     'headline': request.form['headline'],
                     'intro': request.form['intro'],
                     'content': request.form['content'],
                     'id': id
                     };
        #Call model to update Blog
        self.models['Blog'].update_blog(blog_info)
        #Serve up the page to finalize process
        return redirect('/blogs')
    
    #Create
    def create_blog(self):
        #Get form data and assign to variables
        blog_info = {'headline': request.form['headline'],
                     'intro': request.form['intro'],
                     'content': request.form['content'],
                     'user_id': session['id']
                     };
        #Call model to create Blog 
        self.models['Blog'].create_blog(blog_info);
        return redirect('/blogs')  
    
    #Delete
    def delete_blog(self, id):
        #Call model to get Blog
        self.models['Blog'].delete_blog(id)
        #Serve up the page to finalize process
        return redirect('/blogs')
    
    #Blog management page
    def manageBlogs(self):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                blogs = self.models['Blog'].index()
                return self.load_view('postauth/blogManagement.html', blogs=blogs)
        except KeyError:
                return redirect('/login')
    def newBlog(self):
        try:
            if session['loggedIn'] == True and session['type'] == 1:
                return self.load_view('/postauth/newBlog.html')
        except KeyError:
                return redirect('/login')
    
    

