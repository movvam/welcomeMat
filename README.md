# welcomeMat
Code to randomly select a welcome message for your lock screen

#### Set up
Run the following command in your terminal and paste the command

```sh
$ env EDITOR=nano crontab -e

0 */1 * * * /usr/bin/python ~/Path/welcomeMat/welcomeMat.py
```

Google 'crontab' to learn more about the above command and customize to your liking!

Clone the repository and change into it
```
$ git clone https://github.com/movvam/welcomeMat.git
$ cd welcomeMat
```

Allow the Python script to executable
```chmod +x welcomeMat.py```


--------

You may find that sudo requires you type in a password. If this is the case for you, you can change this by opening the sudoers file:

```
$ sudo visudo
```

and adding the following line:
```
YourUserName ALL=(ALL) NOPASSWD: ALL
```
--------

Now you're all set! You can customize your welcome messages in the python script.


Now you're all set! You can customize your welcome messages in the python script.

