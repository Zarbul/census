from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from census.models import People, Language, Department


class PeopleListView(ListView):
    model = People
    context_object_name = 'peoples'


class PeopleCreateView(CreateView):
    model = People
    template_name = 'census/people_add.html'
    success_url = reverse_lazy('list')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        names = People.objects.all()
        context['names'] = names
        return context


class PeopleUpdateView(UpdateView):
    template_name = 'census/people_add.html'
    model = People
    fields = '__all__'
    success_url = reverse_lazy('list')


class PeopleDeleteView(DeleteView):
    template_name = 'census/people_delete.html'
    model = People
    success_url = reverse_lazy('list')


class LanguageCreateView(CreateView):
    template_name = 'census/language_add.html'
    model = Language
    success_url = reverse_lazy('list')
    fields = ['name', ]


class DepartmentCreateView(CreateView):
    template_name = 'census/department_add.html'
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('list')
