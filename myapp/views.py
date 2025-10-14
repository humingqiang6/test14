from django.shortcuts import render

def my_view(request):
    # Example context data to pass to the template
    context = {
        'title': 'My Django Page',
        'message': 'Hello from the view!',
    }
    # Render the template 'my_template.html' with the context
    return render(request, 'my_template.html', context)
