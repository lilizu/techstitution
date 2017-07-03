from flask import Blueprint, render_template, request, redirect, url_for, Response
from app import mongo
from bson import ObjectId
import json


mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        name = ["DEA", "DEA1"]


        reports = mongo.db.reports.find()
        return render_template('mod_main/index.html', reports=reports);

@mod_main.route('/add_audit_form', methods=['GET', 'POST'])
def add_audit_form():
    form = AddAuditForm()
    if request.method == 'GET':
        audits = mongo.db.audits.find()  #mongo.db.audits.find()
        return render_template('mod_main/add_audit_form.html', audits=audits, form=form)

    elif request.method == 'POST':
        print request.form
        mongo.db.reports.insert({
            "audit_title": request.form['audit_title'],
            "audit_ref_num": request.form['audit_ref_num'],
            "audit_date": request.form['audit_date']
            #"name": request.form['name'],
            #"last_name": request.form['last_name']
            #audit_title eshte emri i inputit audit_title te request_form duhet me kan audit_title
        })
        return redirect(url_for('main.audit_list'))


@mod_main.route('/remove/audit', methods=['POST'])
def remove_audit():
    if request.method == 'POST':
        audit_id = request.form['id']
        mongo.db.reports.remove({"_id":ObjectId(report_id)})
        return Response(json.dumps({"removed": True}), mimetype='application/json')

@mod_main.route('/remove/<string:report_id>', methods=['GET'])
def remove(report_id):
    if request.method == 'GET':
        mongo.db.reports.remove({"_id":ObjectId(report_id)})
        return Response(json.dumps({"removed": True}), mimetype='application/json')

@mod_main.route('/add-people', methods=['GET', 'POST'])
def add_people():
    #TODO: Implement POST REQUEST
    # if fail:
        # build logic
    # if success:
        # build logic
    return "JSON RESULT"