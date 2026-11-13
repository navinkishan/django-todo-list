
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.db.models import Q, Case, When, IntegerField, F


def home(request):

    # Add new task
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        priority = request.POST.get('priority', 'Medium')
        due_date = request.POST.get('due_date') or None

        if title.strip():
            Task.objects.create(
                title=title.strip(),
                description=description,
                priority=priority,
                due_date=due_date
            )

        return redirect('home')

    # Get search and filter values
    search_query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', 'all')
    sort_by = request.GET.get('sort', 'newest')

    # Get all tasks
    tasks = Task.objects.all()

    # Search tasks by title
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query)
        )

    # Filter tasks by status
    if status_filter == 'pending':
        tasks = tasks.filter(completed=False)

    elif status_filter == 'completed':
        tasks = tasks.filter(completed=True)

    # Sort tasks
    # Sort tasks
    if sort_by == 'priority':

        tasks = tasks.order_by(
            Case(
                When(priority='High', then=0),
                When(priority='Medium', then=1),
                When(priority='Low', then=2),
                output_field=IntegerField()
            ),
            '-created_at'
        )

    elif sort_by == 'due_date':

        tasks = tasks.order_by(
            F('due_date').asc(nulls_last=True),
            '-created_at'
        )

    else:
        tasks = tasks.order_by('-created_at')
        
    # Dashboard counts (all tasks)
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    pending_tasks = Task.objects.filter(completed=False).count()

    return render(request, 'tasks/home.html', {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'search_query': search_query,
        'status_filter': status_filter,
        'sort_by': sort_by,
    })


def complete_task(request, task_id):

    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = True
        task.save()

    return redirect('home')


def delete_task(request, task_id):

    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()

    return redirect('home')


# FOR EDIT TASK IN HOME PAGE

def edit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority', 'Medium')
        due_date = request.POST.get('due_date') or None

        if title and title.strip():
            task.title = title.strip()
            task.description = description
            task.priority = priority
            task.due_date = due_date
            task.save()

            return redirect('home')

    return render(request, 'tasks/edit.html', {
        'task': task
    })
