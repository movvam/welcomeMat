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


Now you're all set! You can customize your welcome messages in the python script.
