from django import forms
from django.shortcuts import redirect, render, HttpResponse
from .models import Cohort, Student
from django.forms import ModelForm

# Create your views here.


class CohortForm(forms.ModelForm):
    class Meta:
        model = Cohort
        fields = ('cohort_name', 'start_date', 'end_date')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('cohort', 'first_name', 'last_name')

# COHORT METHODS


def cohorts_list(request):
    cohorts = Cohort.objects.all()
    return render(request, 'cohorts/cohorts_list.html', {'cohorts': cohorts})


def cohort_detail(request, cohort_id):
    cohort_detail = Cohort.objects.get(id=cohort_id)
    return render(request, "cohorts/cohort_detail.html", {'cohort_detail': cohort_detail})


def cohort_delete(request, cohort_id):
    if request.method == 'POST':
        cohort = Cohort.objects.get(id=cohort_id)
        cohort.delete()
    return redirect('cohorts_list')


def cohort_new(request):
    if request.method == "POST":
        form = CohortForm(request.POST)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.save()
            return redirect('cohort_detail', cohort_id=cohort.id)
    else:
        form = CohortForm()
    return render(request, 'cohorts/forms.html', {'form': form, 'type_of_request': 'New'})
