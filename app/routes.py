# app/routes.py
from flask import Blueprint, request, render_template, jsonify
from app.models import Log, db, LogMongo
from datetime import datetime
from sqlalchemy import or_, and_

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/ingest', methods=['POST'])
def ingest_log():
    log_data = request.get_json()

    new_log_sql = Log(
        level=log_data['level'],
        message=log_data['message'],
        resourceId=log_data['resourceId'],
        timestamp=datetime.strptime(log_data['timestamp'], '%Y-%m-%dT%H:%M:%SZ'),
        traceId=log_data['traceId'],
        spanId=log_data['spanId'],
        commit=log_data['commit'],
        parentResourceId=log_data['metadata']['parentResourceId'] if 'metadata' in log_data else None
    )

    db.session.add(new_log_sql)
    db.session.commit()

    new_log_mongo = {
        "level": log_data['level'],
        "message": log_data['message'],
        "resourceId": log_data['resourceId'],
        "timestamp": datetime.strptime(log_data['timestamp'], '%Y-%m-%dT%H:%M:%SZ'),
        "traceId": log_data['traceId'],
        "spanId": log_data['spanId'],
        "commit": log_data['commit'],
        "parentResourceId": log_data['metadata']['parentResourceId'] if 'metadata' in log_data else None
    }

    LogMongo.insert_log(new_log_mongo)

    return jsonify({'status': 'success'}), 201

@bp.route('/search', methods=['GET', 'POST'])
def search_logs():
    if request.method == 'POST':
        # Form submission, process the search parameters
        search_params = {
            'level': request.form.get('level'),
            'message': request.form.get('message'),
            'resourceId': request.form.get('resourceId'),
            'timestamp': request.form.get('timestamp'),
            'traceId': request.form.get('traceId'),
            'spanId': request.form.get('spanId'),
            'commit': request.form.get('commit'),
            'parentResourceId': request.form.get('parentResourceId')
        }

        # Filter out None or empty values from search_params
        search_params = {k: v for k, v in search_params.items() if v is not None and v!=''}

        # Build the query dynamically based on the non-empty search parameters
        query_sql = Log.query.filter(and_(*(getattr(Log, k) == v for k, v in search_params.items())))
        logs_sql = query_sql.all()

        # Query MongoDB for logs only if there are non-empty search parameters
        logs_mongo = LogMongo.search_logs(search_params) if search_params else []
    else:
        # Initial GET request, no form submission
        logs_sql = Log.query.all()
        logs_mongo = []

    return render_template('index.html', logs_sql=logs_sql, logs_mongo=logs_mongo)
