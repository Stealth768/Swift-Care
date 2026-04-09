from django.shortcuts import render

# Sample doctors data
DOCTORS_DATA = [
    {
        'id': 1,
        'name': 'Dr. Arjun Singh',
        'specialty': 'Cardiologist',
        'rating': '4.9',
        'reviews': 124,
        'image': 'https://www.shutterstock.com/image-vector/medical-doctor-profile-icon-male-260nw-1019204209.jpg',
        'status': 'Available',
        'reviews_list': [
            {
                'author': 'Rajesh Kumar',
                'date': '2 weeks ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Excellent doctor. Very professional and took time to explain my condition. Highly recommended!'
            },
            {
                'author': 'Priya Desai',
                'date': '1 month ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Dr. Singh is incredibly knowledgeable. The consultation was thorough and he addressed all my concerns.'
            },
            {
                'author': 'Amit Verma',
                'date': '6 weeks ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'One of the best cardiologists I\'ve consulted. Very patient and provides detailed explanations.'
            },
            {
                'author': 'Neha Patel',
                'date': '2 months ago',
                'rating_stars': [1, 2, 3, 4],
                'text': 'Great experience overall. Dr. Singh was professional and caring. Would definitely visit again.'
            },
        ]
    },
    {
        'id': 2,
        'name': 'Dr. Priya Sharma',
        'specialty': 'Emergency Medicine',
        'rating': '4.8',
        'reviews': 89,
        'image': 'https://png.pngtree.com/png-clipart/20231024/original/pngtree-illustration-of-a-female-doctor-for-profile-picture-png-image_13409385.png',
        'status': 'In Surgery',
        'reviews_list': [
            {
                'author': 'Vikram Singh',
                'date': '3 weeks ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Dr. Priya is amazing in emergencies. Calm, composed, and makes quick decisions. Saved my father\'s life!'
            },
            {
                'author': 'Sarah Khan',
                'date': '1 month ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Handling my emergency with utmost care and expertise. Very attentive and quick to respond.'
            },
            {
                'author': 'Ravi Patel',
                'date': '2 months ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Excellent emergency specialist. Very calm under pressure and provides reassurance to patients.'
            },
        ]
    },
    {
        'id': 3,
        'name': 'Dr. Kabir Verma',
        'specialty': 'Neurologist',
        'rating': '5.0',
        'reviews': 210,
        'image': 'https://c8.alamy.com/comp/2FJR92X/flat-male-doctor-avatar-in-medical-face-protection-mask-and-stethoscope-healthcare-vector-illustration-people-cartoon-avatar-profile-character-icon-2FJR92X.jpg',
        'status': 'Available',
        'reviews_list': [
            {
                'author': 'Deepak Gupta',
                'date': '1 week ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Best neurologist in the city. Perfect diagnosis, thorough examination, and excellent follow-up care.'
            },
            {
                'author': 'Maya Singh',
                'date': '3 weeks ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Dr. Verma is exceptional. Very supportive and explains complex neurological conditions in simple terms.'
            },
            {
                'author': 'Arjun Reddy',
                'date': '1 month ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Outstanding care and expertise. My chronic condition has improved significantly under his treatment.'
            },
            {
                'author': 'Pooja Kapoor',
                'date': '6 weeks ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Perfect 5-star experience. Highly qualified, caring, and always available for consultations.'
            },
            {
                'author': 'Suresh Sharma',
                'date': '2 months ago',
                'rating_stars': [1, 2, 3, 4, 5],
                'text': 'Exceptional neurologist with years of experience. Very satisfied with the treatment and results.'
            },
        ]
    }
]

def doctor_panel(request):
    doctors = DOCTORS_DATA
    return render(request, 'dashboard.html', {'doctors': doctors})

def doctor_profile(request):
    doctor_id = request.GET.get('id', 1)
    try:
        doctor = DOCTORS_DATA[int(doctor_id) - 1]
    except (ValueError, IndexError):
        doctor = DOCTORS_DATA[0]
    return render(request, 'doctor_profile.html', {'doctor': doctor})

def consultation_page(request):
    doctor_id = request.GET.get('doctor', 1)
    try:
        doctor = DOCTORS_DATA[int(doctor_id) - 1]
    except (ValueError, IndexError):
        doctor = DOCTORS_DATA[0]
    return render(request, 'consultation.html', {'doctor': doctor})

def sos_monitor(request):
    return render(request, 'sos_monitor.html')