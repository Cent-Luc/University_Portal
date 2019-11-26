from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

class CoursesAdminListView(ListView):
    model = models.Course
    template_name = 'courses_admin_list.html'
    
class CoursesAdminDetailView(DetailView):
    model = models.Course
    template_name = 'courses_admin_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,
                        self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(
                                  initial={'course':self.object})
        return context

class CoursesAdminUpdateView(UpdateView):
    model = models.Course
    fields = ['title', 'summary',]
    template_name = 'courses_admin_edit.html'

class CoursesAdminDeleteView(DeleteView):
    model = models.Course
    template_name = 'courses_admin_delete.html'
    success_url = reverse_lazy('courses_admin_list')

class CoursesAdminCreateView(CreateView):
    model = models.Course
    template_name = 'courses_admin_new.html'
    fields =  ['title', 'code', 'summary',]
