from google.appengine.ext import db
from django import newforms as forms

class User(db.Model):
    answer_on = db.DateTimeProperty(auto_now_add = 1)
    comment = db.TextProperty();

class Type(db.Model):
    id = db.IntegerProperty()
    min = db.StringProperty()
    max = db.StringProperty()

class Question(db.Model):
    question = db.StringProperty()
    id = db.IntegerProperty()
    type = db.ReferenceProperty(Type)
#    created_on = db.DateTimeProperty(auto_now_add = 1)
#    created_by = db.UserProperty()
    
    def __str__(self):
        return '%s' %self.question
    
    def get_absolute_url(self):
        return '/poll/%s/' % self.key()
    

class Answer():
    question = db.ReferenceProperty(Question)
    answer = db.IntegerProperty()
    user = db.ReferenceProperty(User)
    