from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'pacil-inventory',
        'student_name': 'William Joel Matthew Quinn Rompis',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
