from dotenv import load_dotenv
from flask_mail import Mail, Message
from flask import request, jsonify
from os import environ, path, getcwd
from services.all_func import *
load_dotenv(path.join(getcwd(), '.env')) #loading .env file

MAIL_USERNAME = environ.get('MAIL_USERNAME') # getting the mail usernmame from .env
MAIL_PASSWORD = environ.get('MAIL_PASSWORD') # getting the mail password from .env
mail = Mail() # creating an instance of mail

# deactivation mail function
def activation_mail(*args):


    image_url = 'https://processitglobal.com/wp-content/themes/pitg-child/assets-pitg/images/logo.png'
    # print(args[0], args[1], args[2], args[3])
    if args[0] == 'pending':
        cn_approver = (args[3])
        sendtoEmail = getemailbycn(cn_approver)
        approver_mail=[]
        approver_mail.append(sendtoEmail)
        print(approver_mail)

        # print(sendtoEmail+"    "+args[3])
        # Create the email message with HTML formatting
        message_body = f"<p><img src='{image_url}' alt='Company Logo' width='100' height='75'></p>"
        message_body += f"<p>Hello {str(args[3])},</p>"
        message_body += f"<p>You received a request by {str(args[2])} for activtion of employee {str(args[1])}.</p>"
        message_body += f"<p>Please review the request in portal and take action accordingly.</p>"
        message_body += f"<h3><strong>Regards,</strong></h3>"
        message_body += f"<h3><strong>ProcessIT IDAM Team</strong></h3>"
                
        message = Message(subject="Pending request",
                        sender=MAIL_USERNAME,
                        recipients=approver_mail,
                        html=message_body)
        
        
        # Send the email
        try:
            mail.send(message)
            return jsonify({"message": "Email sent successfully"}), 200
        except Exception as e:
            print(e)
            return jsonify({"message": f"Email could not be sent: {str(e)}"}), 500
        
    
    else:
        if args[0] == 'approved' or 'rejected':
            print('inside rejected')
            cn_receiver = (args[1])
            print(cn_receiver)
            sendtoEmail = getemailbycn(cn_receiver)
            receiver_mail=[]
            receiver_mail.append(sendtoEmail)
            print(receiver_mail)
            
            # Create the email message with HTML formatting
            message_body = f"<p><img src='{image_url}' alt='Company Logo' width='100' height='75'></p>"
            message_body += f"<p>Hello {str(args[1])},</p>"
            message_body += f"<p>Your request has been reviewed and {str(args[0])} by {str(args[3])} for activation of employee {str(args[2])}.</p>"
            message_body += f"<h3><strong>Regards,</strong></h3>"
            message_body += f"<h3><strong>ProcessIT IDAM Team</strong></h3>"
                    
            message = Message(subject="Completion of request for activation of employee",
                            sender=MAIL_USERNAME,
                            recipients=receiver_mail,
                            html=message_body)
            
            # Send the email
            try:
                mail.send(message)
                return jsonify({"message": "Email sent successfully"}), 200
            except Exception as e:
                return jsonify({"message": f"Email could not be sent: {str(e)}"}), 500    
            

# deactivation mail function
def deactivation_mail(*args):


    image_url = 'https://processitglobal.com/wp-content/themes/pitg-child/assets-pitg/images/logo.png'
    # print(args[0], args[1], args[2], args[3])
    if args[0] == 'pending':
        cn_approver = (args[3])
        sendtoEmail = getemailbycn(cn_approver)
        approver_mail=[]
        approver_mail.append(sendtoEmail)
        print(approver_mail)

        # print(sendtoEmail+"    "+args[3])
        # Create the email message with HTML formatting
        message_body = f"<p><img src='{image_url}' alt='Company Logo' width='100' height='75'></p>"
        message_body += f"<p>Hello {str(args[3])},</p>"
        message_body += f"<p>You received a request by {str(args[2])} for deactivtion of employee {str(args[1])}.</p>"
        message_body += f"<p>Please review the request in portal and take action accordingly.</p>"
        message_body += f"<h3><strong>Regards,</strong></h3>"
        message_body += f"<h3><strong>ProcessIT IDAM Team</strong></h3>"
                
        message = Message(subject="Pending request",
                        sender=MAIL_USERNAME,
                        recipients=approver_mail,
                        html=message_body)
        
        
        # Send the email
        try:
            mail.send(message)
            return jsonify({"message": "Email sent successfully"}), 200
        except Exception as e:
            print(e)
            return jsonify({"message": f"Email could not be sent: {str(e)}"}), 500
        
    
    else:
        if args[0] == 'approved' or 'rejected':
            print('inside rejected')
            cn_receiver = (args[1])
            print(cn_receiver)
            sendtoEmail = getemailbycn(cn_receiver)
            receiver_mail=[]
            receiver_mail.append(sendtoEmail)
            print(receiver_mail)
            
            # Create the email message with HTML formatting
            message_body = f"<p><img src='{image_url}' alt='Company Logo' width='100' height='75'></p>"
            message_body += f"<p>Hello {str(args[1])},</p>"
            message_body += f"<p>Your request has been reviewed and {str(args[0])} by {str(args[3])} for deactivation of employee {str(args[2])}.</p>"
            message_body += f"<h3><strong>Regards,</strong></h3>"
            message_body += f"<h3><strong>ProcessIT IDAM Team</strong></h3>"
                    
            message = Message(subject="Completion of request for deactivation of employee",
                            sender=MAIL_USERNAME,
                            recipients=receiver_mail,
                            html=message_body)
            
            # Send the email
            try:
                mail.send(message)
                return jsonify({"message": "Email sent successfully"}), 200
            except Exception as e:
                return jsonify({"message": f"Email could not be sent: {str(e)}"}), 500    
            
    
    # else:
    #     if args[0] == 'rejected':
    #         # Create the email message with HTML formatting
    #         message_body = f"<p><img src='{image_url}' alt='Company Logo' width='100' height='75'></p>"
    #         message_body += f"<p>Hello {args[1]},</p>"
    #         message_body += f"<p>Login ID {args[2]},</p>"
    #         message_body += f"<h3><strong>Account deactivation rejected.</strong></h3>"
                    
    #         message = Message(subject="Rejected request",
    #                         sender=MAIL_USERNAME,
    #                         recipients=[args[3]],
    #                         html=message_body)
            
    #         # Send the email
    #         try:
    #             mail.send(message)
    #             return jsonify({"message": "Email sent successfully"}), 200
    #         except Exception as e:
    #             return jsonify({"message": f"Email could not be sent: {str(e)}"}), 500      
        


# access to resource mail function

def atr_mail(*args):

    image_url = 'https://processitglobal.com/wp-content/themes/pitg-child/assets-pitg/images/logo.png'
    
    if args[0] == 'pending':
        cn_approver = (args[2])
        sendtoEmail = getemailbycn(cn_approver)
        approver_mail=[]
        approver_mail.append(sendtoEmail)
        print(approver_mail)
        # Create the email message with HTML formatting
        message_body = f"<p><img src='{image_url}' alt='Company Logo' width='100' height='75'></p>"
        message_body += f"<p>Hello {str(args[2])},</p>"
        message_body += f"<p>You received a request by {str(args[1])} for access to resource.</p>"
        message_body += f"<p>Reason: {str(args[3])}</p>"
        message_body += f"<p>Please review the request in portal and take action accordingly.</p>"
        message_body += f"<h3><strong>Regards,</strong></h3>"
        message_body += f"<h3><strong>ProcessIT IDAM Team</strong></h3>"
                
        message = Message(subject="Pending request",
                        sender=MAIL_USERNAME,
                        recipients=approver_mail,
                        html=message_body)
        
        # Send the email
        try:
            mail.send(message)
            return jsonify({"message": "Email sent successfully"}), 200
        except Exception as e:
            return jsonify({"message": f"Email could not be sent: {str(e)}"}), 500
        
    
    else:
        if args[0] == 'approved' or 'rejected':
            # Create the email message with HTML formatting
            print('inside rejected')
            cn_receiver = (args[1])
            sendtoEmail = getemailbycn(cn_receiver)
            receiver_mail=[]
            receiver_mail.append(sendtoEmail)
            print(receiver_mail)
            
            # Create the email message with HTML formatting
            message_body = f"<p><img src='{image_url}' alt='Company Logo' width='100' height='75'></p>"
            message_body += f"<p>Hello {str(args[1])},</p>"
            message_body += f"<p>Your request has been reviewed and {str(args[0])} by {str(args[3])} for access to resource of employee {str(args[2])}.</p>"
            message_body += f"<h3><strong>Regards,</strong></h3>"
            message_body += f"<h3><strong>ProcessIT IDAM Team</strong></h3>"
                    
            message = Message(subject="Completion of request for access to resource",
                            sender=MAIL_USERNAME,
                            recipients=receiver_mail,
                            html=message_body)
            
            # Send the email
            try:
                mail.send(message)
                return jsonify({"message": "Email sent successfully"}), 200
            except Exception as e:
                return jsonify({"message": f"Email could not be sent: {str(e)}"}), 500    
            