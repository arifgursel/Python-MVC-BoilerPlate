"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
#Login / Reg Routes - Pre Authorization
routes['default_controller'] = 'Auths'
routes['/logout'] = 'Auths#reset'
routes['POST']['/processreg'] = 'Users#process_reg'
routes['POST']['/processlog'] = 'Auths#process_log'
#Default Project Route - Post Authorization
routes['GET']['/rbr'] = 'Rbrs#index'
#User CRUD Routes
routes['POST']['/users'] = 'Users#create_user'                  #CREATE:    Create a new user with data passed from a form
routes['GET']['/users'] = 'Users#index'                         #READ:      Get all users in the DB now
routes['GET']['/users/<int:id>'] = 'Users#get_user'             #READ:      Get a single user by ID
routes['POST']['/users/<int:id>/edit'] = 'Users#update_user'    #UPDATE:    Get a single user by ID
routes['POST']['/users/<int:id>/delete'] = 'Users#delete_user'  #DELETE:    Delete a single user by ID
#Other Project Routes (Built from Wireframes)
"""
    You use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note: that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes:
    User CRUD Routes
    ================
    routes['POST']['/users'] = 'Users#create'              #CREATE:    Create a new user with data passed from a form
    routes['GET']['/users'] = 'Users#get_all'              #READ:      Get all users in the DB now
    routes['GET']['/users/<int:id>'] = 'Users#get_user'    #READ:      Get a single user by ID
    routes['PUT']['/users/<int:id>'] = 'users#update'      #UPDATE:    Get a single user by ID
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'  #DELETE:    Delete a single user by ID
"""
