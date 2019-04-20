## Notify endgame

It polls bookmyshow every 15s to check for update. It is setup to be deployed on heroku. 

To follow the steps you need a [Heroku](https://www.heroku.com/) account and [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).

## Setup

Following changes are required:

* In [notify-endgame.py](https://github.com/gyanesh-m/notify.endgame/blob/master/notify-endgame.py#L9), fill in the following details of a gmail account.

    ``` python
    sender_email = any_gmail_id
    password = its_pass
    ```
* In [reciever.txt](https://github.com/gyanesh-m/notify.endgame/blob/master/reciever.txt) , add emails which have to be notified for the booking.

## Usage

Follow the steps below to deploy it on heroku.
1. Clone this repo and push code to heroku.
``` bash
git clone https://github.com/gyanesh-m/notify.endgame.git
cd notify.endgame
git init
heroku create
git push heroku master
```
2. Spawn a worker to start the task.
``` bash
heroku ps:scale worker=1
```

To view logs, type 
` heroku logs `
