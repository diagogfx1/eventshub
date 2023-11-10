from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from crispy_forms.layout import Layout, Submit, Row, Column


# # Create your forms here.

#Search form

class EventSearchForm(forms.Form):
    query = forms.CharField(label='', max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super(EventSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('query', css_class='col-md-8 mb-9 '),
                Column(Submit('submit', 'Search', css_class='btn btn-danger col-md-8 text-center text-center')),
            )
        )