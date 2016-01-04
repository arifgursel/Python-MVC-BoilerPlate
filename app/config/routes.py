"""
    Routes Configuration File
"""
from system.core.router import routes

#=============
#Default Route
#=============
routes['default_controller'] = 'Pages'

#=============
#Access Routes
#=============
routes['GET']['/login'] = 'Pages#login'
routes['GET']['/logout'] = 'Auths#reset'
routes['POST']['/processreg'] = 'Users#process_reg'
routes['POST']['/processlog'] = 'Auths#process_log'

#=============
#Public Routes
#=============
routes['GET']['/home'] = 'Pages#index'
routes['GET']['/about'] = 'Pages#about'
routes['GET']['/contact'] = 'Pages#contact'
routes['GET']['/roster'] = 'Pages#roster'
routes['GET']['/roster/artist/<int:id>'] = 'Pages#artist'
routes['GET']['/services'] = 'Pages#services'
routes['GET']['/blog'] = 'Pages#blog'
routes['GET']['/blog/<int:id>'] = 'Pages#blogPost'

#=============
#Private Routes
#=============
routes['GET']['/dashboard'] = 'Pages#dashboard'

#=============
#Misc Routes
#=============
routes['POST']['/sendemail'] = 'Contacts#index'


#=============
#Staff Routes
#=============
#------------------------------------
#Serve Views
#------------------------------------
routes['GET']['/users/new'] = 'Users#newStaff'

#------------------------------------
#CRUD Routes
#------------------------------------
routes['POST']['/users'] = 'Users#create_user'                  #CREATE:    Create a new user with data passed from a form
routes['GET']['/users'] = 'Users#index'                         #READ:      Get all users in the DB now
routes['GET']['/users/<int:id>'] = 'Users#get_user'             #READ:      Get a single user by ID
routes['POST']['/users/<int:id>/edit'] = 'Users#update_user'    #UPDATE:    Get a single user by ID
routes['POST']['/users/<int:id>/delete'] = 'Users#delete_user'  #DELETE:    Delete a single user by ID

#vvvv *** Not Secure ***
routes['GET']['/users/<int:id>/admin'] = 'Users#make_admin'     #UPDATE:    Make staff member an admin
#^^^^ *** Not Secure ***

#=============
#Artist Routes
#=============

#------------------------------------
#Serve Form Views
#------------------------------------
routes['GET']['/artists/new'] = 'Artists#newArtist'
routes['GET']['/artists/profile/detailed/<int:artist_id>'] = 'Artists#newDetailProfile'
routes['GET']['/artists/profile/detailed/<int:artist_id>/edit'] = 'Artists#get_detailed_profile'
routes['GET']['/artists/profile/digital/<int:artist_id>'] = 'Artists#newDigitalProfile'
routes['GET']['/artists/profile/digital/<int:artist_id>/edit'] = 'Artists#get_digital_profile'
routes['GET']['/artists/profile/full/<int:artist_id>'] = 'Artists#get_artist_full_profile'             #READ:      Get a single artist by artist_id

#------------------------------------
#Artist Basic Profile CRUD Routes
#------------------------------------
routes['GET']['/artists'] = 'Artists#get_roster'                           #READ:      Get all artists in the DB now
routes['POST']['/artists'] = 'Artists#create_artist'                  #CREATE:    Create a new artist with data passed from a form
routes['GET']['/artists/<int:id>'] = 'Artists#get_artist'             #READ:      Get a basic artist profile by ID
routes['POST']['/artists/<int:id>/edit'] = 'Artists#update_artist'    #UPDATE:    Update a basic artist profile by ID
routes['POST']['/artists/<int:id>/delete'] = 'Artists#delete_artist'  #DELETE:    Delete a artist and all associated profiles by ID
routes['POST']['/artists/<int:id>/deactivate'] = 'Artists#deactivate_artist'  #DELETE:    Delete a artist and all associated profiles by ID
routes['POST']['/artists/<int:id>/activate'] = 'Artists#activate_artist'  #DELETE:    Delete a artist and all associated profiles by ID
#------------------------------------
#Artist Detailed Profile CRUD Routes
#------------------------------------
routes['POST']['/artists/profile/detailed/<int:artist_id>'] = 'Artists#create_detailed_profile'         #CREATE:    Create a new artist profile with data passed from a form
routes['POST']['/artists/profile/detailed/<int:artist_id>/edit'] = 'Artists#update_detailed_profile'    #UPDATE:    Get a single artist profile by artist_id
routes['POST']['/artists/profile/detailed/<int:artist_id>/delete'] = 'Artists#delete_detailed_profile'  #DELETE:    Delete a single artist profile by artist_id

#------------------------------------
#Artist Digital Profile CRUD Routes
#------------------------------------
routes['POST']['/artists/profile/digital/<int:artist_id>'] = 'Artists#create_digital_profile'                  #CREATE:    Create a new digital profile with data passed from a form
routes['POST']['/artists/profile/digital/<int:artist_id>/edit'] = 'Artists#update_digital_profile'    #UPDATE:    Get a single digital profile by artist_id
routes['POST']['/artists/profile/digital/<int:artist_id>/delete'] = 'Artists#delete_digital_profile'  #DELETE:    Delete a single digital profile by artist_id

#=============
#Blog Routes
#=============
#------------------------------------
#CRUD Routes
#------------------------------------
routes['GET']['/blogs'] = 'Blogs#manageBlogs'                         #READ:      Get all blog post
routes['GET']['/blogs/<int:id>'] = 'Blogs#get_blog'             #READ:      Get a single blog by ID
routes['POST']['/blogs'] = 'Blogs#create_blog'                  #CREATE:    Create a new blog with data passed from a form
routes['POST']['/blogs/<int:id>/edit'] = 'Blogs#update_blog'    #UPDATE:    Update blog post by ID
routes['POST']['/blogs/<int:id>/delete'] = 'Blogs#delete_blog'  #DELETE:    Delete a single blog by ID
routes['GET']['/newBlog'] = 'Blogs#newBlog'

#=============
#Press Routes
#=============
#------------------------------------
#CRUD Routes
#------------------------------------
routes['GET']['/press/new/<int:artist_id>'] = 'PressList#newPress'
routes['GET']['/press/<int:artist_id>'] = 'PressList#index'                      #READ:      Get a single pres by artist_id
routes['GET']['/press/<int:artist_id>/<int:id>'] = 'PressList#get_press'                      #READ:      Get a single pres by artist_id
routes['POST']['/press/<int:artist_id>'] = 'PressList#create_press'                  #CREATE:    Create a new pres with data passed from a form
routes['POST']['/press/<int:artist_id>/<int:id>/edit'] = 'PressList#update_press'    #UPDATE:    Get a single pres by artist_id
routes['POST']['/press/<int:artist_id>/<int:id>/delete'] = 'PressList#delete_press'  #DELETE:    Delete a single blog by artist_id
routes['POST']['/press/<int:artist_id>/delete'] = 'PressList#delete_all_press'  #DELETE:    Delete a single blog by artist_id


#=============
#Album Routes
#=============
