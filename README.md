# mysql-dumper
MySQL remote dump and local crontab dump.

# Install
install web.py
```
sudo pip install web.py
```
# Usage
Using the following command to run app. 
```
python dumper.py 8080 --mysql-dump-dir ~/ --mysql-host localhost --mysql-user root --mysql-password root --mysql-database mysql-dumper
```

After the app is running, We can use the following address to dump mysql remote.
```
curl "http://*.*>*.*:8080/dump?password=mysql-dumper"
```

