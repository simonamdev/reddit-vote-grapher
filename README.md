# reddit-vote-grapher
Python scripts to gather and store vote data on specific submissions and then visualise the data.

# Installation

Requirements:

* Python 3.x+

* A valid Reddit Oauth.ini file

Run the following to install the requirements:

> pip3 install -r requirements.txt

# Data collection

It is suggested that you run this behind screen to keep it running in the background.

> screen

> python3 scrape_votes.py

> ctrl+a, ctrl+d

# Data Visualisation

> screen

> python3 visualise.py

> ctrl+a, ctrl+d

Follow up by navigating to http://ip\_of\_device:5000/ in your web browser.

![Browser view](http://imgur.com/KHYmECN)

Clicking on **Graph** then on **Draw Graphs** for a given submission will visualise the stored data:

![Drawn graphs](http://imgur.com/Mmvq5JC)