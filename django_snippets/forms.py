from .models import MODELS_YOU_NEED

# all basic forms inherit from ModelForm
from django.forms import ModelForm

class NameForm(ModelForm):
    # set parameters
    class Meta:
        # model you want to create form for
        model = MODEL_NAME
        # set list of fields for form from model vars
        fields = ['field1', 'field2', 'etc']
        # set all fields from model vars
        fields = "__all__"
        # exclude fields you don't want
        exclude = ["FIELD_TO_EXCLUDE"]
        # change labels
        labels = {"old": "new"}
    # if you need to give some selectors for html/css

    def __init__(self, *args, **kwargs):
            super(FORM_NAME, self).__init__(*args, **kwargs)

            for _, field in self.fields.items():
                # set {"selector": "value"}
                field.widget.attrs.update(
                    {"class": "input", "placeholder": f"--{field.label}--"}
                )

