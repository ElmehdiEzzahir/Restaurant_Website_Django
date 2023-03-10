from django.forms import ModelForm
from products.models import products


class item_creation(ModelForm):
	class Meta:
		model = products
		fields = '__all__'