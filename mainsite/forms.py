from django.forms import ModelForm
from models import Message

class MessageForm(ModelForm):

	# def clean(self):
	# 	cleaned_data = super(MessageForm, self).clean()
	# 	spam = cleaned_data.get("spam_catcher")
	# 	import pdb; pdb.set_trace()
	# 	if spam:
	# 		raise forms.ValidationError("Screw you, spammer.")
	# 	else:
	# 		return self.cleaned_data

	class Meta:
		model = Message
		fields = ['message', 'name']