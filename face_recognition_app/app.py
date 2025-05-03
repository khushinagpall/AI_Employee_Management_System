from django.apps import AppConfig


class FaceRecognitionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'face_recognition_app'

@app.route('/admin/view-students')
def view_students():
    return render_template('view_students.html')
