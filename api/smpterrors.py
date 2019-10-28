
#Refrence : https://serversmtp.com/smtp-error/
#ignored error code 2xx

SMTPERRORS={
    '101':{'error':'The server is unable to connect','possiblesolution':'Try to change the server’s name (maybe it was spelt incorrectly) or the connection port.'},
    '111' :{'error':'Connection refused or inability to open an SMTP stream.','possiblesolution':'This error normally refers to a connection issue with the remote SMTP server, depending on firewalls or misspelled domains. Double-check all the configurations and in case ask your provider.'},
    '420' :{'error':'Timeout connection problem','possiblesolution':'This error message is produced only by GroupWise servers. Either your email has been blocked by the recipient’s firewall, or there’s a hardware problem. Check with your provider.'},
    '421' :{'error':'The service is unavailable due to a connection problem.','possiblesolution':'The server is not available at the moment, so the dispatch will be tried again later.'},
    '422' :{'error':'The recipient’s mailbox has exceeded its storage limit.','possiblesolution':'Best is to contact contact the user via another channel to alert him and ask to create some free room in his mailbox.'},
    '431' :{'error':'Not enough space on the disk','possiblesolution':'This error may depend on too many messages sent to a particular domain. '},
    '432' :{'error':'The recipient’s Exchange Server incoming mail queue has been stopped','possiblesolution':'Its a Microsoft Exchange Server’s SMTP error code, generally it’s due to a connection problem.'},
    '441' :{'error':'The recipient’s server is not responding.','possiblesolution':'There’s an issue with the user’s incoming server: yours will try again to contact it.'},
    '442' :{'error':'The connection was dropped during the transmission.','possiblesolution':'A typical network connection problem, probably due to your router: check it immediately.'},
    '446' :{'error':'The maximum hop count was exceeded for the message: an internal loop has occurred.','possiblesolution':'Ask your SMTP provider to verify what has happened.'},
    '447' :{'error':'Your outgoing message timed out because of issues concerning the incoming server.','possiblesolution':'This happens generally when you exceeded your server’s limit of number of recipients for a message. Try to send it again segmenting the list in different parts.'},
    '449' :{'error':'A routing error.','possiblesolution':' its related only to Microsoft Exchange. Use WinRoute.'},
    '450' :{'error':'Requested action not taken – The user’s mailbox is unavailable. The mailbox has been corrupted','possiblesolution':''},
    '451' :{'error':' Local error in processing','possiblesolution':'If it keeps repeating, ask your SMTP provider to check the situation'},
    '471' :{'error':'An error of your mail server, often due to an issue of the local antispam filter','possiblesolution':'Contact your SMTP service provider to fix the situation.'},
    '500' :{'error':'A syntax error: the server couldn’t recognize the command','possiblesolution':'It may be caused by a bad interaction of the server with your firewall or antivirus. Read carefully their instructions to solve it.'},
    '501' :{'error':'A syntax error: the server couldn’t recognize the command','possiblesolution':'It may be caused by a bad interaction of the server with your firewall or antivirus. Read carefully their instructions to solve it.'},
    '510' :{'error':'Bad email address.','possiblesolution':'Check again your recipient mail address'},
    '511' :{'error':'Bad email address.','possiblesolution':'Check again your recipient mail address'},
    '541' :{'error':'The recipient address rejected your message','possiblesolution':'Your message has been detected and labeled as spam. You must ask the recipient to whitelist you'},
    '550':{'error':'It usually defines a non-existent email address on the remote side.','possiblesolution':''}












































}