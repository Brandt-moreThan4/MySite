from django import forms
#from .models import Comment

class EmailPostForm(forms.Form):
    """Sharing a post by email form. The email will come from brandtgreen97@gmail.com"""

    #Use the widget attribute to change how the html renders.
    # I would rather figure out how to include my homemade forms. The extra flexibility would be refreshing.


    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


#class CommentForm(forms.ModelForm):
#    """Comment submission form"""
#    class Meta:
#        model = Comment
#        fields = ('name', 'email', 'body')

