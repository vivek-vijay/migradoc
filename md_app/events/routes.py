from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from md_app import db
from md_app.models import HeadacheEvent
from md_app.events.forms import EventForm
from flask_login import current_user, login_required


events = Blueprint('events', __name__)


@events.route("/event/new", methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    if form.validate_on_submit():
        event = HeadacheEvent(
                    startDate=form.startDate.data,
                    endDate=form.endDate.data,
                    pain=form.pain.data,
                    nv=form.nv.data,
                    phonophoto=form.phonophoto.data,
                    adls=form.adls.data,
                    period=form.period.data,
                    acutetx1=form.acutetx1.data,
                    acutetx2=form.acutetx2.data,
                    acutetx3=form.acutetx3.data,
                    acutetxSuccess=form.acutetxSuccess.data,
                    prophylactic=form.prophylactic.data,
                    prophylacticDose=form.prophylacticDose.data,
                    triggers=form.triggers.data,
                    notes=form.notes.data,
                    migraineur=current_user
                    )
        db.session.add(event)
        db.session.commit()
        flash('Event has been saved', 'success')
        return redirect(url_for('events.headache_diary'))
    return render_template('create_event.html', title='New Event', form=form, legend='Add Headache event')


@events.route("/headachediary", methods=['GET', 'POST'])
@login_required
def headache_diary():
    page = request.args.get('page', 1, type=int)
    events = HeadacheEvent.query.filter_by(user_id=current_user.id).order_by(HeadacheEvent.startDate.desc()).paginate(page=page, per_page=10)
    return render_template('headachediary.html', events=events)


@events.route("/event/<int:event_id>")
@login_required
def event(event_id):
    event = HeadacheEvent.query.get_or_404(event_id)
    if event.migraineur != current_user:
        abort(403)
    return render_template('event.html', title=event.startDate.strftime('%d/%m/%Y'), event=event)


@events.route("/event/<int:event_id>/update", methods=['GET', 'POST'])
@login_required
def update_event(event_id):
    event = HeadacheEvent.query.get_or_404(event_id)
    if event.migraineur != current_user:
        abort(403)
    form = EventForm()
    if form.validate_on_submit():
        event.startDate = form.startDate.data
        event.endDate = form.endDate.data
        event.pain = form.pain.data
        event.nv = form.nv.data
        event.phonophoto = form.phonophoto.data
        event.adls = form.adls.data
        event.period = form.period.data
        event.acutetx1 = form.acutetx1.data
        event.acutetx2 = form.acutetx2.data
        event.acutetx3 = form.acutetx3.data
        event.acutetxSuccess = form.acutetxSuccess.data
        event.prophylactic = form.prophylactic.data
        event.prophylacticDose = form.prophylacticDose.data
        event.triggers = form.triggers.data
        event.notes = form.notes.data
        db.session.commit()
        flash('Event has been updated', 'success')
        return redirect(url_for('events.event', event_id=event.id))
    elif request.method == 'GET':
        form.startDate.data = event.startDate
        form.endDate.data = event.endDate
        form.pain.data = event.pain
        form.nv.data = event.nv
        form.phonophoto.data = event.phonophoto
        form.adls.data = event.adls
        form.period.data = event.period
        form.acutetx1.data = event.acutetx1
        form.acutetx2.data = event.acutetx2
        form.acutetx3.data = event.acutetx3
        form.acutetxSuccess.data = event.acutetxSuccess
        form.prophylactic.data = event.prophylactic
        form.prophylacticDose.data = event.prophylacticDose
        form.triggers.data = event.triggers
        form.notes.data = event.notes
    return render_template('create_event.html', title='Update Event', form=form, legend='Update headache event')


@events.route("/event/<int:event_id>/delete", methods=['POST'])
@login_required
def delete_event(event_id):
    event = HeadacheEvent.query.get_or_404(event_id)
    if event.migraineur != current_user:
        abort(403)
    db.session.delete(event)
    db.session.commit()
    flash('Event has been deleted', 'success')
    return redirect(url_for('events.headache_diary'))


@events.route("/headachediary/summary", methods=['GET', 'POST'])
@login_required
def diary_summary():
    events = HeadacheEvent.query.filter_by(user_id=current_user.id).all()
    return render_template('diarysummary.html', events=events)
