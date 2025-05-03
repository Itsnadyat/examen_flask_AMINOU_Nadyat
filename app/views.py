from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Task
from datetime import datetime

main = Blueprint('main', __name__)

# Page d'accueil avec toutes les tâches
@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Ajout d'une nouvelle tâche
@main.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        status = request.form['status']
        priority = request.form['priority']
        due_date = request.form['due_date'] if request.form['due_date'] else None
        due_date = datetime.strptime(due_date, '%Y-%m-%d') if due_date else None

        new_task = Task(title=title, description=description, status=status,
                        priority=priority, due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        flash('Tâche ajoutée avec succès !', 'success')
        return redirect(url_for('main.index'))

    return render_template('task_form.html')

# Modification d'une tâche
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form.get('description', '')
        task.status = request.form['status']
        task.priority = request.form['priority']
        task.due_date = request.form['due_date'] if request.form['due_date'] else None
        task.due_date = datetime.strptime(task.due_date, '%Y-%m-%d') if task.due_date else None
        db.session.commit()
        flash('Tâche mise à jour avec succès !', 'success')
        return redirect(url_for('main.index'))

    return render_template('task_form.html', task=task)

# Suppression d'une tâche
@main.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash('Tâche supprimée avec succès !', 'danger')
    return redirect(url_for('main.index'))
