from django import forms
from ads.models import Ad, Comment 
from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.humanize import naturalsize
from django.core import validators
from django.core.exceptions import ValidationError


class CreateForm(forms.ModelForm):
	max_upload_limit = 2 * 1024 * 1024
	max_upload_limit_text = naturalsize(max_upload_limit)

	#call this 'picture' so it gets copied from the form to the in-memory
	#model. It will not be the "bytes", it will be the 'InMemoryUploadedFile'
	#because we need to pull out things like 'content_type'
	picture = forms.FileField(required=False, label='File to upload <= '+max_upload_limit_text)
	upload_field_name = 'picture'


	class Meta:
		model = Ad
		fields = ['title', 'price', 'text', 'picture']


	#Validate the size of the picture
	def clean(self):
		cleaned_data = super().clean()
		pic = cleaned_data.get('picture')
		if pic is None:
			return 

		if len(pic) > self.max_upload_limit:
			self.add_error('picture', "File must be less than "+self.max_upload_limit_text+"bytes")


	#Convert uploaded File object to a picture
	def save(self, commit=True):
		instance = super(CreateForm, self).save(commit=False)

		#We only need to adjus picture if it is a freshly uploaded file
		f = instance.picture	#Making a copy
		if isinstance(f, InMemoryUploadedFile):		#Extract data from the form to the model
			bytearr = f.read()
			instance.content_type = f.content_type
			instance.picture = bytearr		#Overwrite with the actual image data

		if commit:
			instance.save()

		return instance

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)

    # class Meta:
    # 	model = Comment
    # 	fields = ['text']




