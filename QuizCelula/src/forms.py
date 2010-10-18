from django import newforms as forms
import models
from google.appengine.ext.db import djangoforms

class TypeForm(djangoforms.ModelForm):
    class Meta:
        model = models.Type
        
class QuestionForm(forms.Form):
    choice = forms.CharField(max_length = 100)
    
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        
    def save(self):
#        question = models.Question(poll = self.poll, choice = self.clean_data['choice'])
#        question.put()
        
        