import imaplib
import email
from email.header import decode_header
import base64

ans = []

gmail_pass = "izgu gpfq ipzq orkt"
username = "hacatontest@gmail.com"
imap_server = "imap.gmail.com"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, gmail_pass)

imap.select("INBOX")

status, messages = imap.search(None, "UNSEEN")

if messages[0]:
    unseen_ids = messages[0].split()
    for email_id in unseen_ids:
        res, msg_data = imap.fetch(email_id, '(RFC822)')
        if msg_data and msg_data[0]:
            raw_email = msg_data[0][1]
            if isinstance(raw_email, bytes):
                msg = email.message_from_bytes(raw_email)
            else:
                continue

        letter_date = msg["Date"]
        letter_id = msg["Message-ID"]
        letter_from = msg["From"]

        subject_header = decode_header(msg["Subject"])[0]
        heading = subject_header[0]
        if isinstance(heading, bytes):
            heading = heading.decode(subject_header[1] or 'utf-8')

        text = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)
                    if payload:
                        payload = part.get_payload(decode=True)
                        if isinstance(payload, bytes):
                            text = payload.decode('utf-8', errors='ignore')
                        elif isinstance(payload, str):
                            text = payload
                        else:
                            text = ""
                    break
        else:
            payload = msg.get_payload(decode=True)
            if payload and isinstance(payload, bytes):
                text = payload.decode('utf-8', errors='ignore')

        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
                
            if part.get('Content-Disposition') is not None:
                filename = part.get_filename()
                if filename:
                    filename_header = decode_header(filename)[0]
                    filename = filename_header[0]
                    if isinstance(filename, bytes):
                        filename = filename.decode(filename_header[1] or 'utf-8')

                    file_data = part.get_payload(decode=True)
                    if file_data and filename and isinstance(file_data, bytes):
                        with open(filename, 'wb') as f:
                            f.write(file_data)

        print(letter_date)
        print(letter_from)
        print(heading)
        print(text)
        ans.append([letter_date, letter_from, heading, text])
        
print(ans)