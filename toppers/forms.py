from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Themes
class ThemesForm(ModelForm):
    class Meta:
        model = Themes
        fields = '__all__'
        widgets = {
            'right_content_fg': TextInput(attrs={'type': 'color'}),
            'right_content_bg': TextInput(attrs={'type': 'color'}),
            'center_content_bg':TextInput(attrs={'type': 'color'}),
            'title_text_color': TextInput(attrs={'type': 'color'}),
            'category_text_color': TextInput(attrs={'type': 'color'}),
            'amount_bg_color':TextInput(attrs={'type':'color'}),
            'amount_fg_color': TextInput(attrs={'type': 'color'}),
            'branch_fg_color': TextInput(attrs={'type': 'color'}),
            'branch_bg_color': TextInput(attrs={'type': 'color'}),

            'bm_name_color': TextInput(attrs={'type': 'color'}),
            'bm_box_shadow': TextInput(attrs={'type': 'color'}),

        }
