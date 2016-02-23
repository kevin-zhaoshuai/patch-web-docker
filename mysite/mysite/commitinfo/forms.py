from django import forms

class CommitForm(forms.Form):
	date = forms.ChoiceField(
        choices=(
            ("2012", "2012"),
            ("2015", "2015"),
        ),
        label='Commit Period',
    )
