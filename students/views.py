from django.urls import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from courses.models import Course
from .models import Student

from .forms import StudentEnrollForm
from .forms import CourseEnrollForm


class StudentEnrollView(FormView):
    student = None
    form_class = StudentEnrollForm

    def form_valid(self, form):
        self.student = form.cleaned_data['student']
        self.student.students.add(self.request.user)
        return super(StudentEnrollView,
                     self).form_valid(form)

        def get_success_url(self):
            return reverse_lazy('student_enroll_detail',
                                args=[self.student.id])


class StudentEnrollCourseView(FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView,
                     self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail',
                            args=[self.course.id])


class StudentCourseListView(ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])

class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super(StudentCourseDetailView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView,
                        self).get_context_data(**kwargs)
        #get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            #get current module
            context['module'] = course.modules.get(
                    id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = course.modules.all()[0]
            return context

class StudentRegistrationView(CreateView):
    template_name = 'students/registration.html'
    model = Student
    fields = (
        'student_id', 'level_of_study', 'sponsor', 'year_joined',
        'semester_joined', 'national_id', 'date_of_birth',
        'nhif_membership_no', 'nhif_owner', 'nhif_is_card_valid',
        'nhif_valid_until'
    )

    def form_valid(self, form):
        """
        Overridden to always set the user field to the currently logged in user
        """
        user = self.request.user
        form.instance.user = user
        return super(StudentRegistrationView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    """
    This view is used to change the details
    of a particular student
    """
    model = Student
    fields = (
        'level_of_study', 'sponsor', 'year_joined',
        'semester_joined', 'national_id', 'date_of_birth',
        'nhif_membership_no', 'nhif_owner', 'nhif_is_card_valid',
        'nhif_valid_until'
    )
    template_name = 'students/update.html'

class StudentDetailView(ListView):
    """
    Here a student can check his/her registration
    details and edit them as required
    """
    model = Student
    template_name = "students/detail.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
