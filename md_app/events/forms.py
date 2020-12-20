from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    pain = SelectField('Pain level', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], coerce=int)
    nv = SelectField('Nausea &/or vomiting', choices=['Neither', 'Felt sick and/or vomited'])
    phonophoto = SelectField('Aversion to light &/or sounds', choices=['Neither', 'Aversion to light', 'Aversion to sound only', 'Aversion to light & sound'])
    adls = SelectField('Effect on normal activities', choices=['Able to continue', 'Not able to continue'])
    period = SelectField('Relation to menstrual cycle', choices=['Not within -2 to +3 days of start of menstruation', 'Within -2 to +3 days of start of menstruation'])
    acutetx = SelectField('Any acute treatment taken?', choices=['None', 'Paracetamol 500mg', 'Paracetamol 1g', 'Regular-dose NSAID e.g. ibuprofen 600mg', 'High-dose NSAID e.g. ibuprofen 900mg', 'Triptan', 'Metoclopromide/domperidone'])
    prophylactic = SelectField('Currently taking a preventative?', choices=['No', 'Amitriptyline', 'Propanolol', 'Topiramate', 'Candesartan'])
    # prophylacticDose =
    triggers = SelectField('Any potential triggers for this attack?', choices=['None', 'Irregular sleep', 'Altered meal times', 'Dietary changes', 'Increased exercise', 'Decreased exercise', 'Stress'])
    submit = SubmitField('Save Headache Event')
