from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional

class TaskForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    status = SelectField('Statut', choices=[('À faire', 'À faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')])
    priority = SelectField('Priorité', choices=[('Basse', 'Basse'), ('Moyenne', 'Moyenne'), ('Haute', 'Haute')])
    due_date = DateField('Date d\'échéance', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Enregistrer')
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Optional

class TaskForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    status = SelectField('Statut', choices=[('À faire', 'À faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')])
    priority = SelectField('Priorité', choices=[('Basse', 'Basse'), ('Moyenne', 'Moyenne'), ('Haute', 'Haute')])
    due_date = DateField('Date d\'échéance', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Enregistrer')
