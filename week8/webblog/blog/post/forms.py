from django import forms


from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','slug','author','image','body')

        widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.ImageField(),
        }

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widget = {
            'body': forms.TextInput(attrs={'class':'form-control'}),
        }