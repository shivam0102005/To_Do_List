from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task,User

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    # tasks = Task.query.all()
    return redirect(url_for('tasks.view_tasks'))
    # return render_template("tasks.html", tasks=tasks)

@task_bp.route('/tasks')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    # Get current user
    current_user = User.query.filter_by(username=session['user']).first()
    
    # Only show tasks for this user
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

@task_bp.route("/add", methods=["POST"])
def add_task():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    title = request.form.get("title")
    if title:
        # Get current user
        current_user = User.query.filter_by(username=session['user']).first()
        
        new_task = Task(title=title, status="Pending", user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully", "success")

    return redirect(url_for("tasks.view_tasks"))

@task_bp.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_status(task_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    # Get current user
    current_user = User.query.filter_by(username=session['user']).first()
    
    # Only allow modifying tasks that belong to this user
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if task:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
        flash("Task status updated!", "info")

    return redirect(url_for("tasks.view_tasks"))

@task_bp.route('/delete/<int:task_id>', methods=["POST"])
def delete_task(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    # Get current user
    current_user = User.query.filter_by(username=session['user']).first()
    
    # Only allow deleting tasks that belong to this user
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!", "info")

    return redirect(url_for('tasks.view_tasks'))

@task_bp.route("/clear", methods=["POST"])
def clear_tasks():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    # Get current user
    current_user = User.query.filter_by(username=session['user']).first()
    
    # Only clear tasks for this user
    Task.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash("All tasks cleared!", "info")
    return redirect(url_for("tasks.view_tasks"))