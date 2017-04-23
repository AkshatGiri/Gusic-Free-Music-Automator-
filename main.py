from flask import Flask, request, redirect, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import ytdownloader as ytd
import upGmusic as upG


# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)




@app.route("/sms", methods=['GET', 'POST'])
def letsGo():
    
    counter = session.get('counter', 0)

    # increment the counter
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter
    
    #Getting the song and the artists name
    msgBody = request.form['Body']
    ytd.DownloadSong(msgBody)
    ttl = ytd.title

    #Uploading the song to Google Music
    upG.uploadSong(ttl)

    #Deleteing the file after the upload
    ytd.deleteSong()

    print('Done')

    resp = MessagingResponse()
    resp.message("Mission Accomplished.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)