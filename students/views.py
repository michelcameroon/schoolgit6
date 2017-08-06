#from django.http import Http404

from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse


#from django.template import loader

from .models import Student



def index(request):

    latest_student_list = Student.objects.order_by('-pub_date')[:5]
    context = {'latest_student_list': latest_student_list}
    return render(request, 'students/index.html', context)

#    template = loader.get_template('students/index.html')
#    context = {
#        'latest_student_list': latest_student_list,
#    }
#    return HttpResponse(template.render(context, request))

#    output = ', '.join([q.student_firstName for q in latest_student_list])
#    return HttpResponse(output)


#    return HttpResponse("Hello, world. You're at the students index.")


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


#def detail(request, student_id):
#
#    try:
#        student = Student.objects.get(pk=student_id)
#    except Student.DoesNotExist:
#        raise Http404("Student does not exist")
#    return render(request, 'students/detail.html', {'student': question})


#    return HttpResponse("You're looking at student %s." % student_id)




def results(request, student_id):
    response = "You're looking at the results of student %s."
    return HttpResponse(response % student_id)
