#python3! - Write a program that scans through your email account, finds all the unsubscribe
#links in all your emails, and automatically opens them in a browser.

import webbrowser
import imaplib #for more understanding use this link - https://www.youtube.com/watch?v=Gql_NQv3ND4&ab_channel=CodingEntrepreneurs
import bs4
import imapclient
import pyzmail #https://pypi.org/project/pyzmail/
#if you get errors when installing this module use: pip install setuptools==20.1.1, and then pip install pyzmail36
#(if still not working try also: pip3 install --upgrade supertools, pip3 install --upgrade pip)

#other option will be to install ez_setup and then use easy_install pyzmail (this didn't work for me)
def unsub_scan(user_name, user_pass):
    """Returns a list of the unsubscribe links in a Gmail inbox."""
    unsub_links = []
    imaplib._MAXLINE = 10000000
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(user_name, user_pass)
    imap_obj.select_folder('INBOX', readonly=True)
    unique_ids = imap_obj.search(['ALL'])

    for identifier in unique_ids:
        raw_message = imap_obj.fetch([identifier], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_message[identifier][b'BODY[]'])
        html = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html, 'lxml')
        link_elems = soup.select('a')
        for selected in link_elems:
            if 'unsubscribe' in str(selected):
                unsub_links.append(selected.get('href'))

    imap_obj.logout()

    return unsub_links

email = input('Enter your email username: ')
password = input('Enter your email password: ')
links = unsub_scan(email, password)

for link in links:
    webbrowser.open(link)

print('All unsubscribe links have been opened.')
