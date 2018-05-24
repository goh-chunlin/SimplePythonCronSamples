# SimplePythonCronSamples
Collection of samples showing how Python can be used in Cron.

## About simple01.py
This simple sample is to show a Python script that will be called by a cron job and append a line to a text file called Cron.txt.

### Setting of Cron Job
Made the Cron Job to be executable by executing the following command.

```
chmod +x cron-script.sh
```

After that, schedule it in crontab by using the following command. Crontab is the program used to install, remove or list the tables used to serve the cron(8) daemon (Reference: man crontab).

```
crontab -e
```

Then, we need to specify how frequent we need the cronjob to be running at. For example, if we want to make it run the Python script every 2 minutes, we can set it as follows.

```
*/2 * * * * /root/Documents/cron-script.sh
```
