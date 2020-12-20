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
        event = HeadacheEvent(date=form.date.data, pain=form.pain.data, nv=form.nv.data, phonophoto=form.phonophoto.data, adls=form.adls.data, period=form.period.data, acutetx=form.acutetx.data, prophylactic=form.prophylactic.data, triggers=form.triggers.data, migraineur=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Event has been saved', 'success')
        return redirect(url_for('events.headache_diary'))
    return render_template('create_event.html', title='New Event', form=form, legend='Add Headache event')


@events.route("/headachediary", methods=['GET', 'POST'])
@login_required
def headache_diary():
    page = request.args.get('page', 1, type=int)
    events = HeadacheEvent.query.filter_by(user_id=current_user.id).order_by(HeadacheEvent.date.desc()).paginate(page=page, per_page=4)
    return render_template('headachediary.html', events=events)


@events.route("/event/<int:event_id>")
@login_required
def event(event_id):
    event = HeadacheEvent.query.get_or_404(event_id)
    if event.migraineur != current_user:
        abort(403)
    return render_template('event.html', title=event.date.strftime('%d/%m/%Y'), event=event)


@events.route("/event/<int:event_id>/update", methods=['GET', 'POST'])
@login_required
def update_event(event_id):
    event = HeadacheEvent.query.get_or_404(event_id)
    if event.migraineur != current_user:
        abort(403)
    form = EventForm()
    if form.validate_on_submit():
        event.date = form.date.data
        event.pain = form.pain.data
        event.nv = form.nv.data
        event.phonophoto = form.phonophoto.data
        event.adls = form.adls.data
        event.period = form.period.data
        event.acutetx = form.acutetx.data
        event.prophylactic = form.prophylactic.data
        event.triggers = form.triggers.data
        db.session.commit()
        flash('Event has been updated', 'success')
        return redirect(url_for('events.event', event_id=event.id))
    elif request.method == 'GET':
        form.date.data = event.date
        form.pain.data = event.pain
        form.nv.data = event.nv
        form.phonophoto.data = event.phonophoto
        form.adls.data = event.adls
        form.period.data = event.period
        form.acutetx.data = event.acutetx
        form.prophylactic.data = event.prophylactic
        form.triggers.data = event.triggers
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
