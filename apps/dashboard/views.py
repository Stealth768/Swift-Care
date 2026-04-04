from django.shortcuts import render

def doctor_panel(request):
    doctors = [
        {
            'name': 'Dr. Arjun Singh',
            'specialty': 'Cardiologist',
            'rating': '4.9',
            'reviews': 124,
            'image': 'https://www.shutterstock.com/image-vector/medical-doctor-profile-icon-male-260nw-1019204209.jpg',
            'status': 'Available'
        },
        {
            'name': 'Dr. Priya Sharma',
            'specialty': 'Emergency Medicine',
            'rating': '4.8',
            'reviews': 89,
            'image': 'https://png.pngtree.com/png-clipart/20231024/original/pngtree-illustration-of-a-female-doctor-for-profile-picture-png-image_13409385.png',
            'status': 'In Surgery'
        },
        {
            'name': 'Dr. Kabir Verma',
            'specialty': 'Neurologist',
            'rating': '5.0',
            'reviews': 210,
            'image': 'https://c8.alamy.com/comp/2FJR92X/flat-male-doctor-avatar-in-medical-face-protection-mask-and-stethoscope-healthcare-vector-illustration-people-cartoon-avatar-profile-character-icon-2FJR92X.jpg',
            'status': 'Available'
        }
    ]
    return render(request, 'dashboard.html', {'doctors': doctors})