from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
    startDate = DateField('Start date', validators=[DataRequired()])
    endDate = DateField("End date (if ongoing, select today's date and update later)", validators=[DataRequired()])
    pain = SelectField('Pain level', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], coerce=int)
    nv = SelectField('Nausea &/or vomiting', choices=['Neither', 'Felt nauseous and/or was sick'])
    phonophoto = SelectField('Aversion to light &/or sounds', choices=['Neither', 'Unable to tolerate bright lights/loud sounds'])
    adls = SelectField('Effect on normal activities', choices=['Able to continue', 'Not able to continue'])
    period = SelectField('Relation to menstrual cycle', choices=['Not within -2 to +3 days of start of menstruation', 'Within -2 to +3 days of start of menstruation'])
    acutetx1 = SelectField('Select any acute treatment taken',
                           choices=['None', 'Aspirin 300mg', 'Aspirin 600mg', 'Aspirin 900mg', 'Ibuprofen 400mg', 'Ibuprofen 600mg', 'Paracetamol 500mg', 'Paracetamol 1000mg',
                                    'Diclofenac 25mg', 'Naproxen 250mg', 'Metoclopromide 10mg', 'Domperidone 10mg', 'Prochlorperazine 10mg', 'Sumatriptan 50mg tablet',
                                    'Sumatriptan 100mg tablet', 'Sumatriptan 10mg nasal spray', 'Sumatriptan 20mg nasal spray', 'Almotriptan 12.5mg', 'Eletriptan 40mg',
                                    'Frovatriptan 2.5mg', 'Naratriptan 2.5mg', 'Rizatriptan 10mg', 'Zolmitriptan 5mg', 'Other'])
    acutetx2 = SelectField('Select any acute treatment taken',
                           choices=['None', 'Aspirin 300mg', 'Aspirin 600mg', 'Aspirin 900mg', 'Ibuprofen 400mg', 'Ibuprofen 600mg', 'Paracetamol 500mg', 'Paracetamol 1000mg',
                                    'Diclofenac 25mg', 'Naproxen 250mg', 'Metoclopromide 10mg', 'Domperidone 10mg', 'Prochlorperazine 10mg', 'Sumatriptan 50mg tablet',
                                    'Sumatriptan 100mg tablet', 'Sumatriptan 10mg nasal spray', 'Sumatriptan 20mg nasal spray', 'Almotriptan 12.5mg', 'Eletriptan 40mg',
                                    'Frovatriptan 2.5mg', 'Naratriptan 2.5mg', 'Rizatriptan 10mg', 'Zolmitriptan 5mg', 'Other'])
    acutetx3 = SelectField('Select any acute treatment taken',
                           choices=['None', 'Aspirin 300mg', 'Aspirin 600mg', 'Aspirin 900mg', 'Ibuprofen 400mg', 'Ibuprofen 600mg', 'Paracetamol 500mg', 'Paracetamol 1000mg',
                                    'Diclofenac 25mg', 'Naproxen 250mg', 'Metoclopromide 10mg', 'Domperidone 10mg', 'Prochlorperazine 10mg', 'Sumatriptan 50mg tablet',
                                    'Sumatriptan 100mg tablet', 'Sumatriptan 10mg nasal spray', 'Sumatriptan 20mg nasal spray', 'Almotriptan 12.5mg', 'Eletriptan 40mg',
                                    'Frovatriptan 2.5mg', 'Naratriptan 2.5mg', 'Rizatriptan 10mg', 'Zolmitriptan 5mg', 'Other'])
    acutetxSuccess = SelectField('Was pain improved 2 hours after taking treatment?', choices=['None taken', 'No', 'Slightly', 'Greatly', 'Completely resolved headache'])
    prophylactic = SelectField('Are you currently taking a preventative?', choices=['No', 'Amitriptyline', 'Candesartan', 'Propanolol', 'Topiramate', 'Erenumab (Aimovig)', 'Fremanezumab (Ajovy)', 'Galcanezumab (Emgality)'])
    prophylacticDose = StringField('Enter total daily dose of preventative medication currently taken')
    triggers = SelectField('Any potential triggers for this attack?', choices=['None', 'Irregular sleep', 'Altered meal times', 'Dietary changes', 'Increased exercise', 'Decreased exercise', 'Stress'])
    notes = TextAreaField('Any further notes?')
    submit = SubmitField('Save Headache Event')
