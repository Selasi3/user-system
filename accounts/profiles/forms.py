from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import FileUpload

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class FileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ('file_name','file',)