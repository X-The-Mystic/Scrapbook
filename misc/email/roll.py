import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import google.auth
import os
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time

#recipient = "gduser1@workspacesamples.dev"
recipient = input("Recipient?")
sender = "me"

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def auth():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  return creds

def rick(sender:str, recipient:str, delay_ms:int=500, reversed:bool=True, lyrics_file:str="lyrics.txt", config:dict=None) -> list:
  if config:
    if not config.get("preview"):
      config["preview"] = "Bon Appétit!"
    if not config.get("text"):
      config["text"] = "You've been rick-rolled! Enjoy the prank, or reply STOP to this email to prevent future rickroll attempts."
    if not config.get("html"):
      config["html"] = "<h1>You've been rick-rolled!</h1><small><a style='color:#666666' href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Unsubscribe</a></small>"
  else:
    config = {
      "preview":  "Bon Appétit!",
      "text":     "You've been rick-rolled! Enjoy the prank, or reply STOP to this email to prevent future rickroll attempts.",
      "html":     "<h1>You've been rick-rolled!</h1><small><a style='color:#666666' href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Unsubscribe</a></small>"
      }

  creds = auth()
  fin = open(lyrics_file, mode="r")
  lyrics = [x.strip() for x in fin.readlines()]
  fin.close()
  if reversed:
    lyrics.reverse()
  total = len(lyrics)

  logs = []
  times = []

  try:
    service = build("gmail", "v1", credentials=creds)
    print(f"{total} (lines) * {delay_ms} (ms/line) = {total*delay_ms/1000} (sec) estimated time")

    for i, line in enumerate(lyrics):
      t0 = time.time()

      i += 1
      percent = (i*100)//total
      #print(percent)
      bar = f"{i}/{total} {line if len(line)+len(str(total))+len(str(i))+2<=100 else line[:100-len(str(total))-len(str(i))-5]+'...'}{' '*(100-(len(line)+len(str(total))+len(str(i))+2))}"
      bar = "\x1b[42m"+bar[:percent]+"\x1b[0m"+bar[percent:]
      if len(times) >= 5:
        rawtime = int((sum(times[-len(times):])/len(times))*(total-i))
        eta = f"{str(rawtime//60).rjust(2,'0')}:{str(rawtime%60).rjust(2,'0')}"
        print(f"\x1b[2K\rSending: [ {bar} ] {percent}% - {eta} ETA ", end="")
      else:
        print(f"\x1b[2K\rSending: [ {bar} ] {percent}% ", end="")

      message = MIMEMultipart('alternative')
      message["To"] = recipient
      message["From"] = sender
      message["Subject"] = str(total-i) + ". " + (line if line else "​")
      text = config['text']
      html = f"""<div style="display: none; max-height: 0px; overflow: hidden;">{config['preview']}</div><div style="display: none; max-height: 0px; overflow: hidden;"> &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;  &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;  &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;  &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;  &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;  &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;  &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;  &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; </div>
      {config['html']}"""
      message.attach(MIMEText(text, 'plain'))
      message.attach(MIMEText(html, 'html'))

      # encoded message
      encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
      create_message = {"raw": encoded_message}
      send_message = service.users().messages().send(userId="me", body=create_message).execute()
      logs.append(send_message)
      time.sleep(delay_ms/1000)
      t1 = time.time()
      times.append(t1-t0)

    print("\x1b[2K\rSending: [ "+'\x1b[42m'+('Done!'+' '*95)+'\x1b[0m'+" ] 100% - ETA 00:00 ")
    
  except HttpError as error:
    print(f"An error occurred: {error}")
    logs = []
  return logs


if __name__ == "__main__":
  res = rick(sender, recipient, config={"preview": "​"})
  for i in res:
    print("Message Id:", i['id'])
