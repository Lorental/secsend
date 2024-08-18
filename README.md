# secsend
Secure way to send messages with confidential information (like login/passwords etc.) via proper web interface

## About
Secsend - little utility to send confidential information in companies.
Just forget about situations where you send login/pass to your mate and after firing this mate continue to use this data to use.
Just send him one time message.
(Yes, I know that we also have risks, that this person can save it in his personal keychain.
But, as a saw in big corps - usually people forget about it)

### Tech Stack
Python / Django / BootStrap

### Restrictions
You should disable preview in your corp. messenger and on your email server (or this things will destroy messages, because MS Exchange / Slack / Tg / other usually get first request to create preview)
You can also ban this things by user-agent in product code, if preview disabling is not your way.

### Access to server
By default, I set Allowed Hosts by *, because you can set it for your production environment by yourself.
