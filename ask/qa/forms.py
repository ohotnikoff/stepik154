from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, question, **kwargs):
        self._question = question
        super(AnswerForm, self).__init__(*kwargs)

    def save(self):
        self.cleaned_data['question'] = self._question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

