from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Task


class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ('title', 'description')
		labels = {
			'title': _('Judul'),
			'description': _('Deskripsi'),
		}

		error_messages = {
			'title': {
				'required': _("Judul harus diisi."),		
			},
			'description': {
				'required': _("Deskripsi harus diisi."),
			},
		}
