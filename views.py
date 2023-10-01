# habits/views.py
from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitRecord
from .forms import HabitForm
import json
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.shortcuts import redirect
import json
from django.utils import timezone 

@login_required
def track_habit(request):
    if request.method == 'POST':
        # Handle tracking habit logic here
        # For example, mark a habit as completed for the current date
        habit_id = request.POST.get('habit_id')
        habit_record, created = HabitRecord.objects.get_or_create(
            habit_id=habit_id,
            date=date.today()  # You may need to import date from datetime
        )
        habit_record.completed = True
        habit_record.save()
        
        return redirect('dashboard')  # Redirect back to the dashboard after tracking

    # Handle GET requests or any other cases here
    return redirect('dashboard')  # Redirect back to the dashboard for other cases



@login_required
# def dashboard_view(request):
#     user = request.user
#     habits = Habit.objects.filter(user=user)
#     return render(request, 'dashboard.html', {'user': user, 'habits': habits})
 

def dashboard_view(request):
    user = request.user
    habits = Habit.objects.filter(user=user)

    # Fetch habit tracking data
    habit_data = []
    for habit in habits:
        habit_records = HabitRecord.objects.filter(habit=habit, date__lte=timezone.now().date())
        completed_count = habit_records.filter(completed=True).count()
        habit_data.append({
            'habit_name': habit.name,
            'completed_count': completed_count,
            'goal': habit.goal
        })
    
    # Convert the habit_data list to JSON
    habit_data_json = json.dumps(habit_data)

    return render(request, 'dashboard.html', {'user': user, 'habits': habits, 'habit_data_json': habit_data_json})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or any other desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or any other desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the logi

@login_required
def habit_create_view(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('dashboard')
    else:
        form = HabitForm()
    return render(request, 'habit_form.html', {'form': form})

@login_required
def habit_edit_view(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit_form.html', {'form': form, 'habit': habit})

@login_required
def habit_delete_view(request, habit_id):
    # Get the habit object or return a 404 response if it doesn't exist
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)

    if request.method == 'POST':
        # Handle habit deletion here
        habit.delete()
        return redirect('dashboard')  # Redirect to the dashboard after deletion

    # Render a confirmation page for deleting the habit
    return render(request, 'habit_delete.html', {'habit': habit})




@login_required
def habit_tracking_view(request):
    user = request.user
    habits = Habit.objects.filter(user=user)
    habit_data = []
    
    for habit in habits:
        habit_records = HabitRecord.objects.filter(habit=habit, date__lte=timezone.now().date())
        completed_count = habit_records.filter(completed=True).count()
        habit_data.append({
            'habit_name': habit.name,
            'completed_count': completed_count,
            'goal': habit.goal
        })

    habit_data_json = json.dumps(habit_data)

    return render(request, 'habit_tracking.html', {'habit_data_json': habit_data_json})


# habits/views.py

@login_required
def goal_setting_view(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    
    if request.method == 'POST':
        # Process the form data to set goals for the habit
        pass
    else:
        # Display the form for setting goals
        pass
    
    return render(request, 'goal_setting.html', {'habit': habit})
