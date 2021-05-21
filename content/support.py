from . import mail, mongo
from flask_mail import Message


# Send support ticket to Agents
def send_ticket_agents(*, question, category, user_email, ticket_id, created_on, _sender: str):
    agents_col = mongo.get_collection('agents')
    agents_data = agents_col.find({}, {'_agentEmail': 1})   # list of all agents from database
    if agents_data is not None:
        _recipients = [agent['_agentEmail'] for agent in agents_data]
        msg = Message("Support Ticket", sender=(_sender, "isolveitgroup@gmail.com"), recipients=_recipients)
        msg.body = f'''Hello Agent,
A support ticket with the following details has been filed,
    - Ticket ID: {ticket_id}
    - Question: {question}
    - Category: {category}
    - Email: {user_email}
    - Created: {created_on.strftime('%B %d, %Y, %H:%M ') + 'GMT'}
    
Answer the user by emailing {user_email}.
Thank you.

Regards,
{_sender.upper()}
    '''
        mail.send(msg)
        return 'OK'


# Send support ticket details to user
def send_ticket_details(*, user_email, question, category, ticket_id, user_name, created_on, _sender: str):
    msg = Message('Support Ticket Received', sender=(_sender, "isolveitgroup@gmail.com"), recipients=[user_email])
    msg.body = f'''Hello {user_name},
Below is the support ticket details,
    - Ticket ID: {ticket_id}
    - Question: {question}
    - Category: {category}
    - Created: {created_on.strftime('%B %d, %Y, %H:%M ') + 'GMT'}
Thank you.

Regards,
{_sender.upper()}
'''
    mail.send(msg)
    return 'OK'
