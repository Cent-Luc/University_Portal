from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

class CoursesAdminListView(ListView):
    model = models.Course
    template_name = 'courses_admin_list.html'
    
class CoursesAdminDetailView(DetailView):
    model = models.Course
    template_name = 'courses/course/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,
                        self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(
                                  initial={'course':self.object})
        return context

class CoursesAdminUpdateView(UpdateView):
    pass

class CoursesAdminDeleteView(DeleteView):
    pass

