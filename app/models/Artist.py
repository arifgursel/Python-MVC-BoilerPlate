""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
class Artist(Model):
    def __init__(self):
        super(Artist, self).__init__()

    #=========Artist CRUD Methods==========
    #Read (*)
    def index(self):
        #get all artists currently registered in the DB
        query = "SELECT * FROM artists WHERE active = 1 ORDER BY name ASC;";
        return self.db.query_db(query);
    #Read (*)
    def get_roster(self):
        #get all artists currently registered in the DB
        query = "SELECT * FROM artists ORDER BY name ASC;";
        return self.db.query_db(query);
    #Read (1)
    def get_artist(self, id):
        #get a single artist by ID
        query = "SELECT * FROM artists WHERE id={};".format(id);
        return self.db.query_db(query);
    def get_artist_full_profile(self, id):
        #get a single artist by ID
        query = "SELECT artists.id, name, instrument, bio, active, has_profile, has_digital, artist_profiles.composer, artist_profiles.arranger, artist_profiles.clinic, artist_profiles.residency, artist_digitals.website, artist_digitals.calendar, artist_digitals.facebook, artist_digitals.twitter, artist_digitals.instagram, artists.created_at, artists.updated_at FROM artists, artist_profiles, artist_digitals WHERE artists.id = artist_profiles.artist_id AND artist_profiles.artist_id = artist_digitals.artist_id AND artists.id = {};".format(id);
        return self.db.query_db(query);#Read (1)
    def get_artist_roster_info(self, id):
        #get a single artist by ID
        query = "SELECT artists.id, name, instrument, bio, active, has_profile, has_digital, artist_profiles.composer, artist_profiles.arranger, artist_profiles.clinic, artist_profiles.residency, artist_digitals.website, artist_digitals.calendar, artist_digitals.facebook, artist_digitals.twitter, artist_digitals.instagram, artists.created_at, artists.updated_at FROM artists, artist_profiles, artist_digitals WHERE artists.id = artist_profiles.artist_id AND artist_profiles.artist_id = artist_digitals.artist_id AND artists.id = {};".format(id);
        return self.db.query_db(query);
    #Create   
    def create_artist(self, artist_info):
        #create a new artist
        query = "INSERT INTO artists (`name`, `bio`, `instrument`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(artist_info['name'], artist_info['bio'], artist_info['instrument']);
        return self.db.query_db(query);
    #Update
    def update_artist(self, artist_info):
        #update a single artist by passing JSON of artist information
        query = "UPDATE artists SET `name`='{}', `bio`='{}', `instrument`='{}', `updated_at`=NOW() WHERE `id`='{}';".format(artist_info['name'], artist_info['bio'], artist_info['instrument'], artist_info['id']);
        return self.db.query_db(query);
    #Delete
    def delete_artist(self, id):
        #Delete a single artist by ID
        query = "DELETE FROM artists WHERE `id`={};".format(id);
        return self.db.query_db(query);
    
    #=========Artist Profile Toggle Methods==========
    def toggleProfileOn(self, artist_id):
        #set artist profile value as set
        query = "UPDATE artists SET `has_profile` = 1, `updated_at` = NOW() WHERE `id`={};".format(artist_id);
        return self.db.query_db(query);
    def toggleProfileOff(self, artist_id):
        #set artist profile to not set
        query = "UPDATE artists SET `has_profile` = 0, `updated_at` = NOW() WHERE `id`={};".format(artist_id);
        return self.db.query_db(query);
    def toggleDigitalOn(self, artist_id):
        #set artist digital profile to set
        query = "UPDATE artists SET `has_digital` = 1, `updated_at` = NOW() WHERE `id`={};".format(artist_id);
        return self.db.query_db(query);
    def toggleDigitalOff(self, artist_id):
        #set artist digital profile to not set
        query = "UPDATE artists SET `has_digital` = 0, `updated_at` = NOW() WHERE `id`={};".format(artist_id);
        return self.db.query_db(query);
    def deactivate(self, artist_id):
        #deactivate artist profile before deleting
        query = "UPDATE artists SET `active` = 0, `updated_at` = NOW() WHERE `id`={};".format(artist_id);
        return self.db.query_db(query);
    def activate(self, artist_id):
        #set artist profile to active to remove from delete list
        query = "UPDATE artists SET `active` = 1, `updated_at` = NOW() WHERE `id`={};".format(artist_id);
        return self.db.query_db(query);

    #=========Artist Profile Methods==========
    #Read
    def get_profile(self, id):
        #get a single artist by ID
        query = "SELECT * FROM artist_profiles WHERE artist_id={};".format(id);
        return self.db.query_db(query);
    #Create   
    def create_profile(self, artist_profile_info):
        #create a new artist
        query = "INSERT INTO artist_profiles (`artist_id`, `composer`, `arranger`, `clinic`, `residency`, `created_at`, `updated_at`) VALUES ('{}', '{}','{}', '{}','{}', NOW(), NOW())".format(artist_profile_info['artist_id'], artist_profile_info['composer'], artist_profile_info['arranger'], artist_profile_info['clinic'], artist_profile_info['residency']);
        return self.db.query_db(query);
    #Update
    def update_profile(self, artist_profile_info):
        #update a single artist by passing JSON of artist information
        query = "UPDATE artist_profiles SET `composer`='{}', `arranger`='{}', `clinic`='{}', `residency`='{}', `updated_at`=NOW() WHERE `artist_id`='{}';".format(artist_profile_info['composer'], artist_profile_info['arranger'], artist_profile_info['clinic'], artist_profile_info['residency'], artist_profile_info['artist_id']);
        return self.db.query_db(query);
    #Delete
    def delete_profile(self, id):
        #Delete a single artist by ID
        query = "DELETE FROM artist_profiles WHERE `artist_id`={};".format(id);
        return self.db.query_db(query);
    
    #=========Artist Digital Profile Methods==========
    #Read
    def get_digital(self, artist_id):
        #get a single artist by ID
        query = "SELECT * FROM artist_digitals WHERE artist_id={};".format(artist_id);
        return self.db.query_db(query);
    #Create   
    def create_digital(self, artist_digital_info):
        #create a new artist
        query = "INSERT INTO artist_digitals (`artist_id`, `website`, `calendar`, `facebook`, `twitter`, `instagram`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', '{}', '{}','{}', NOW(), NOW())".format(artist_digital_info['artist_id'], artist_digital_info['website'], artist_digital_info['calendar'], artist_digital_info['facebook'], artist_digital_info['twitter'], artist_digital_info['instagram']);
        return self.db.query_db(query);
    #Update
    def update_digital(self, artist_digital_info):
        #update a single artist by passing JSON of artist information
        query = "UPDATE artist_digitals SET `website`='{}', `calendar`= '{}', `facebook`= '{}', `twitter`= '{}', `instagram`= '{}', `updated_at`=NOW() WHERE `artist_id`= '{}';".format(artist_digital_info['website'], artist_digital_info['calendar'], artist_digital_info['facebook'], artist_digital_info['twitter'], artist_digital_info['instagram'], artist_digital_info['artist_id']);
        return self.db.query_db(query);
    #Delete
    def delete_digital(self, artist_id):
        #Delete a single artist by ID
        query = "DELETE FROM artist_digitals WHERE `artist_id`={};".format(artist_id);
        return self.db.query_db(query);



