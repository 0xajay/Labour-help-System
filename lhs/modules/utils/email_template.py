headerHtmlPart = '''
        <html>
        <head>
       <style>
           body{
           display:block;
           font-size: 17px;
           text-align: justify;
           font-family: Times, Serif;
           margin: 20px 20px 20px 20px;
           background-color: #E7EAFC;
           margin:auto;
           width: 40%;
           padding: 10px;
           }
           .body{
           background-color: #E7EAFC;
           padding:30px
           }
           .header{
               width:80%;
           }
           .e-font-small{
               font-size: 13px;
           }
           .e-margin-top{
               margin-top:20px;
           }
           .e-margin-top-small{
               margin-top:30px;
           }
           .content {
           display: flex;
           }
           table{
               line-height: 25px;
               margin-top:50px;
           }
           footer{
             margin-top: 2cm;
           }
       </style>
       </head>
       <body>
       <div class="body">
 '''
footerImages = '''
            <table>
               <tbody>
                   <tr>
                       <td> <img src="cid:image1" width="50%"> </td>
                       <td> <img src="cid:image2" width="50%"> </td>
                   </tr>
                   <tr>
                       <td> Build your online profile </td>
                       <td> Find Professionals </td>
                   </tr>
                   <tr>
                       <td> <ul><li>Add to your Resume</li><li>Show off your skills</li> <li>Negotiate Contracts</li> <li>Connect with Colleagues</li></ul></td>
                       <td> <ul><li>Send offers</li><li>Easy-booking </li> <li>Automate Payments </li><li>Manage your schedule</li></ul></td>
                   </tr>
               </tbody>
               </div>
               </div>
               </body>
               </html>'''


def welcomeRegisterTemplate(otp,firstname):
    content = "Hi <b>"+firstname+"<b/>,<p>Thanks for signing up with Resonance!  We are so excited you’ve made your first step in becoming a part of our thriving community!.<br/>To confirm your email address, please enter the 6-digit code below in the Resonance app: <br/><b>"+str(otp)+"</b><br/>If you ever have any questions about our platform, including building your profile, sending offers, negotiating contracts, using your schedule, or any other features don’t hesitate to message or contact us at <b>support@yourresonance.com<b/>"+"<br/>Thank you for using Resonance. Keep making art your reality!<br/><b>The Resonance Team</b>"
    return content

def ChangePasswordTemplate(otp,firstname):
    content = "Hi <b>"+firstname+",<br/>To confirm your email address, please enter the 6-digit code below in the Resonance app:<br/><b>"+str(otp)+"<b/><br/><br/>If you ever have any questions about our platform, including building your profile, sending offers, negotiating contracts, using your schedule, or any other features don’t hesitate to message or contact us at support@yourresonance.com.<br/>Thank you for using Resonance. Keep making art your reality!<br/><br/>The Resonance Team<br/><br/>Build your online profile<br/>Find Professionals<br/>Add to your Resume<br/>Show off your skills<br/>Negotiate Contracts<br/>Connect with Colleagues<br/>Send offers<br/>Easy-booking<br/>Automate Payments<br/>Manage your schedule"
    return content

def InvitationTemplate(firstname,lastname):
    content = "Hello <b>"+firstname+" "+lastname+"<b/> has added you as a colleague on Resonance!<br/>Download the app by clicking here and build your profile today<br/>If you ever have any questions about our platform, including building your profile, sending offers, negotiating contracts, using your schedule, or any other features, don’t hesitate to message or contact us at support@yourresonance.com<br/><br/>Thank you for using Resonance. Keep making art your reality!<br/><br/>The Resonance Team<br/><br/>Build your online profile<br/>Find Professionals<br/>Add to your Resume<br/>Show off your skills<br/>Negotiate Contracts<br/>Connect with Colleagues<br/>Send offers<br/>Easy-booking<br/>Automate Payments<br/>Manage your schedule"
    return content

def prelim_tic_content(firstName):
    content = "Hi "+firstName+",<br/><br/>You’ve just received a new job offer on Resonance! To view the offer, please open the app and go to the My Jobs tab. Under engagements, tap on “Offers you’ve received”.<br/>Make sure to respond to this offer soon, so that the person knows you’re available!<br/><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def prelim_toc_title():
    title = "Resonance - A professional has replied to your offer"
    return title

def prelim_toc_content(employerName,professionalName,professionalMessage):
    content = "Hi "+employerName+",<br/><br/>"+professionalName+" has said they are interested in your offer! <br/><i>"+professionalMessage+"</i><br/><br/>Open the Resonance App and head to the My Jobs tab to send out a full offer. You can add information about events, payment details, and riders you may be offering.<br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def contract_tic_content(employerName,professionalName):
    content = "Hi "+ professionalName +",<br/><br/>"+employerName+''' has sent you a new offer on Resonance! To view the offer, please open the app and go to the My Jobs tab. Under Engagements, tap on "Offers you’ve received”.<br/>You can choose to accept, negotiate terms, or decline the offer.<br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team'''

    return content

def contract_toc_title():
    title = "Resonance - Offer Negotiated"
    return title

def contract_toc_content(employerName,professionalName,professionalMessage):
    content = "Hi "+employerName+",<br/><br/>"+professionalName+" has negotiated terms on the offer you sent them.<br/><i>"+professionalMessage+"</i><br/><br/>To view details about their requested changes go to the Offers you’ve sent section under Engagements in the My Jobs tab.<br/>This is the only opportunity the professional has to negotiate terms to your original sent offer.<br/>You are free to accept or decline their requested terms. Alternatively, you can meet them in the middle and modify the terms to something agreeable to both parties.<br/>After you’ve sent the final offer, the professional will need to accept or decline the opportunity.<br/>If you have any questions regarding negotiating offers, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def contract_final_title():
    title = "Resonance - Final Offer"
    return title

def contract_final_content(employerName,professionalName):
    content = "Hi "+professionalName+",<br/><br/>"+employerName+" has sent you a final offer and modified details in the offer based on the terms you negotiated.<br/>To view the final offer terms go to the Offers you’ve received section under Engagements of the My Jobs tab.<br/>This is the final opportunity for you to accept or decline their offer. Make sure to go over all of the details before accepting.<br/>If you decide to accept, "+employerName+" will be prompted to confirm the offer and authorize payment for the dates outlined in the offer details.<br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>Your Resonance Team"
    return content

def contract_finalized_to_professional_title():
    title = "Resonance - You’re Hired!"
    return title

def contract_finalized_to_professional_content(employerName,professionalName):
    content = "Hi "+professionalName+",<br/><br/>"+employerName+" has confirmed and authorized payment for the job you’ve accepted.<br/>Go to the Accepted Engagements section of the My Jobs tab to view full details or to find "+employerName+"’s contact information.<br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def accepted_offer_title():
    title = "Resonance - Offer Accepted!"
    return title

def accepted_offer_content(employerName,professionalName,professionalMessage):
    content = "Hi "+employerName+",<br/><br/>"+professionalName+" has accepted your offer!<br/><br/><i>"+professionalMessage+"</i><br/>Make sure to complete the offer process by going to the Confirm section under Jobs you’ve sent in the My Jobs tab. You’ll be prompted to confirm and authorize this opportunity according to the details outlined in the offer.  Make sure to do this as quickly as possible so "+professionalName+" knows you’ve hired them.<br/>If you have any questions, please email us at info@yourresonance.com <br/><br/>Thanks for using Resonance! <br/><br/> The Resonance Team"

    return content

def prelim_tic_not_available_title():
    title = "Resonance - A professional has replied to your offer"
    return title

def prelim_tic_not_available_content(employerName,professionalName,professionalMessage):
    content = "Hi "+employerName+",<br/><br/>"+professionalName+" has said they are interested in your offer, but they won’t be available for the dates you specified.<br/><i>"+professionalMessage+"</i><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def reject_offer_title():
    title = "Resonance - Offer Declined"
    return title

def reject_offer_content(employerName,professionalName,professionalMessage):
    content = "Hi "+employerName+",<br/><br/>"+professionalName+" has declined the offer you sent them. <br/><br/><i>"+professionalMessage+"</i><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"

    return content

def rescind_offer_title():
    title = "Resonance - Offer Rescinded"
    return title

def rescind_offer_content(employerName,professionalName,professionalMessage):
    content = "Hi "+professionalName+",<br/><br/>"+employerName+" has decided to rescind the offer they sent to you.<br/><br/><i>"+professionalMessage+"</i><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def slot_new_booking_request(card_name,booker_name,date,time,location,booker_message):
    content = '''Session Details<br/>'''+card_name+'''<br/>'''+date+''',''' +time+''', <br/>Booked By: '''+booker_name+'''<br/>Location: '''+location+'''<br/><br/>Message from '''+booker_name+'''<br/><br/><i>'''+booker_message+'''</i><br/><br/>Next Steps: <br/><br/><ul><li>Go to <b>Pending Bookings</b> under <b>Bookings</b> in the <b>Engagements</b> tab to see full details about the session.</li>
                <li>Tap <b>Respond</b> to either <b>Accept</b> or <b>Decline</b> the booking request</li>
                <li>Once you’ve accepted the session, go to the <b>Confirmed Bookings</b> under <b>Bookings</b> to view your upcoming, completed, and cancelled bookings.</li>
                </ul><br/><br/>
                Make sure to respond to this request soon, so '''+booker_name+''' knows you want to work with them!<br/><br/>
                If you have any questions, please email us at info@yourresonance.com<br/><br/>
                Thanks for using Resonance!<br/><br/>
                The Resonance Team<br/><br/>
                '''
    return content

def slot_confirmed_session(card_name,owner_name,date,time,location,booking_id,owner_message):
    content = owner_name+" has accepted your booking request!<br/><br/>Session Details<br/>"+card_name+"<br/>"+date+", "+time+",<br/>Confirmed By: "+owner_name+"<br/>Location: "+location+"<br/>Booking ID: "+booking_id+"<br/><br/>Next Steps:<br/><br/><ul><li>Go to <b>Confirmed Bookings</b> under <b>Bookings</b> in the <b>Engagements</b> tab to see full details about the session.</li><li>Tap <b>View details</b> to see specific information about the booking including date, time, and location</li><li>From there you can <b>contact</b> the professional, cancel the session, or report a problem.</li></ul> <br/><br/>We hope you have a great time working with "+owner_name+"!!<br/><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def slot_declined_session(card_name,owner_name,date,time,location,booking_id,owner_message):
    content = "Session Details<br/><br/>"+card_name+"<br/>"+date+", "+time+",<br/>Declined By: "+owner_name+"<br/>Location:  "+location+"<br/>Booking ID: "+booking_id+"<br/><br/>"+owner_name+" has declined your booking request.<br/><br/>Message from "+owner_name+"<br/><br/><i>"+owner_message+"<br/><br/>Next Steps:<br/><br/><ul><li>Tap on <b>View cancelled & Declined Bookings</b> under <b>Bookings</b> in the <b>Engagements</b> tab to see full details about the declined session.</li></ul><br/><br/>We’re sorry this booking didn’t work out.Don’t hesitate to book again soon!<br/><br/>If you have any questions, please email us at info@yourresonance.com <br/><br/>Thanks for using Resonance.The Resonance Team"

    return content

def cancelled_session_to_booker(card_name,owner_name,date,time,location,booking_id,owner_message):
    content = "Session Details<br/>"+card_name+"<br/>"+date+","+time+",<br/>You Booked: "+owner_name+"<br/>Location: "+location+"<br/>Booking ID: "+booking_id+"<br/><br/>"+owner_name+" has cancelled your session<br/><br/>Message from "+owner_name+"<br/><br/><i>"+owner_message+"</i><br/><br/>Next Steps:<br/><br/><ul><li>Tap on View cancelled & Declined Bookings under Bookings in the Engagements tab to see full details about the cancelled session.</li></ul><br/><br/>We’re sorry this session was cancelled.  Don’t hesitate to book again soon!<br/><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def cancelled_session_to_owner(card_name,booker_name,date,time,location,booking_id,booker_message):
    content = booker_name+" has cancelled the session<br/><br/>Session Details<br/>"+card_name+"<br/>"+date+", "+time+",<br/>Booked by: "+booker_name+"<br/>Location: "+location+"<br/>Booking ID: "+booking_id+"<br/><br/>Message from "+booker_name+"<br/><br/><i>"+booker_message+"<i/><br/><br/>Next Steps:<br/><br/><ul><li>If "+booker_name+" cancelled the session within your cancellation policy window, you will receive the funds for the session in your connected bank account soon.</li><li>Tap on View cancelled & Declined Bookings under Bookings in the Engagements tab to see full details about the cancelled session.</li></ul><br/><br/>We’re sorry this session was cancelled.  Keep an eye out for any new booking requests coming your way!<br/><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def session_complete_payment(card_name,amount_sent,date,time,booker_name,location,receipt,total_amount):
    content = "Session Details<br/><br/>"+card_name+"<br/>"+amount_sent+"<br/>"+date+", "+time+",<br/>Booked By: "+booker_name+"<br/>Location: "+location+"<br/>Receipt : "+receipt+"<br/><br/>The funds in the amount of "+total_amount+" for your session with "+booker_name+" have been successfully disbursed to your connected account.<br/><br/>Next Steps:<br/><br/><ul><li>Go to the <b>Menu</b> tab and tap on the <b>Dashboard</b>.</li><li>Tap on <b>Earnings</b> to view your transaction history, track earnings, and payout funds to your connected bank account.</li></ul><br/><br/>Congrats on the awesome work! We can’t wait to see what new opportunities come your way!<br/><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content

def session_complete_payment_to_booker(card_name,owner_name,date,time,location,payment_datetime,total_amount,receipt,cancellation_hours):
    content = "Payment Details<br/>"+total_amount+"<br/>"+payment_datetime+"<br/><br/>TOTAL AMOUNT: "+total_amount+"<br/><br/>Receipt :"+receipt+"<br/><br/>Cancellation Policy: "+cancellation_hours+" hours<br/><br/><br/>Session Details<br/>"+card_name+"<br/>"+date+", "+time+",<br/>You Booked: "+owner_name+"<br/>Location: "+location+"<br/><br/>To view your receipt on Resonance<br/><br/><ul><li>Go to <b>Completed Bookings</b> under <b>Bookings</b> in the Engagements tab.</li><li>Open <b>View Details</b> for the session and tap <b>BOOKING ID</b> to see your payment receipt..</li></ul><br/><br/>Thanks for booking on Resonance! See you next time!<br/><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content


def problem_collecting_payment_to_owner(card_name,booker_name,date,time,location,receipt,sendable_amount):
    content = sendable_amount+"<br/><br/>Session Details<br/>"+card_name+"<br/>"+date+", "+time+",<br/>Booked By: "+booker_name+"<br/>Location: "+location+"<br/>Receipt: "+receipt+"<br/><br/>"+booker_name+"'s default payment card is invalid and will result in an unsuccessful payment for your session.<br/><br/>Next Steps:<br/><br/><ul><li>You should encourage "+booker_name+" to update their payment information immediately. It’s up to you whether or not you want to perform a session without upfront payment.</li><li>"+booker_name+" will be unable to continue transacting on Resonance until the payment has been authorized and completed.</li><li>Once payment details have been updated, we will attempt to collect the funds and immediately disburse your earnings to you.</li></ul><br/><br/>We’re sorry this happened and are working to resolve the situation as soon as possible!<br/><br/>If you have any questions, please email us at info@yourresonance.com<br/><br/>Thanks for using Resonance!<br/><br/>The Resonance Team"
    return content
