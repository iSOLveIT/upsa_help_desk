from flask import request

from . import app, mongo
from .support import send_ticket_agents, send_ticket_details
from .algolia import search_bar

from random import sample
from datetime import datetime as dt
import re


# Route for search input
@app.route('/')
def index():
    search_term: str = request.args.get('search_term')
    if search_term is not None:
        search_term = search_term.lower()
        # limit of 512 characters per query by Algolia
        res = re.search(r"^[\w\d ]{5,200}?$", search_term)
        if res is not None:
            answers = search_bar(query=search_term)
            if answers is None:
                # return render_template('index.html', results="None")
                return {"results": None}
            # return render_template('index.html', results=answers)
            return {"results": answers}
    # return render_template('index.html', results='None')
    return {"results": None}


# Route for fetching the selected result
@app.route('/search_result/<string:question_id>')
def select_result(question_id):
    records_col = mongo.get_collection('records')
    result = records_col.find_one(
        {'_questionID': int(question_id)},
        {'_title': 1, '_answer': 1, '_category': 1, '_id': 0}
    )
    return {"results": result}


# Route for support
@app.route('/support', methods=['POST'])
def support():
    # ticket_collection = mongo.get_collection('tickets')
    question = request.form.get('question')
    category = request.form.get('category')
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    created = dt.now()
    ticket_id = "".join(sample("abcdefgh123456789", 5))
    mail_sender = "UPSA Help Desk Contact"

    # ticket_collection.insert_one({
    #     "_ticketID": ticket_id, "_question": question, "_answer": "",
    #     "_email": email, "_category": category, "_name": name, "status": False,
    #     "_created": created
    # })
    send_ticket_details(
        question=question, user_email=email, user_name=name, category=category,
        ticket_id=ticket_id, created_on=created, _sender=mail_sender
    )
    send_ticket_agents(
        question=question, category=category, user_email=email,
        ticket_id=ticket_id, created_on=created, _sender=mail_sender
    )
    return {"results": 'success'}
