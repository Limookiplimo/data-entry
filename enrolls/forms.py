from django.forms import ModelForm
from enrolls.models import Employee
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div

class EmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'employee-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2 col-form-label'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div('title', css_class='form-group'),
            Div('first_name', css_class='form-group'),
            Div('last_name', css_class='form-group'),
            Div('age', css_class='form-group'),
            Div('email', css_class='form-group'),
            Div('phone', css_class='form-group'),
            Div('department', css_class='form-group'),
            Div('doe', css_class='form-group'),
            Div(
                Submit('submit', 'Enroll', css_class='btn btn-primary'),
                css_class='form-group',
            )
        )

    class Meta:
        model = Employee
        fields = ('title', 'first_name', 'last_name', 'age', 'email', 'phone', 'department', 'doe')
