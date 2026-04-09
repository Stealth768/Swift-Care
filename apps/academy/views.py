from django.shortcuts import render, get_object_or_404

def tutorial_list(request):
    tutorials = [
        {'id': 1, 'title': 'Emergency First Aid', 'description': 'Quick response guide for road accidents.'},
        {'id': 2, 'title': 'Trident System Manual', 'description': 'How to use the diagnostic tools.'},
        {'id': 3, 'title': 'Hospital Workflow', 'description': 'Managing patient queues effectively.'},
    ]
    return render(request, 'academy.html', {'tutorials': tutorials})

def tutorial_detail(request, tutorial_id=1):
    tutorials = {
        1: 'Emergency First Aid & Critical Care',
        2: 'Advanced Diagnostic Systems',
        3: 'Hospital Operations Management',
    }
    
    course_name = tutorials.get(tutorial_id, 'Medical Training Course')
    
    return render(request, 'academy_detail.html', {'course_name': course_name})

def tutorial_first_aid(request):
    return render(request, 'tutorial_first_aid.html')

def tutorial_diagnostic(request):
    return render(request, 'tutorial_diagnostic.html')

def tutorial_operations(request):
    return render(request, 'tutorial_operations.html')