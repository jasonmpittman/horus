# horus
Horus is a cross-platform honeypot which seeks to maximize attacker sojourn time

## Basic, manual running:
```
sudo python3 horus.py
```

## Next thoughts:
1. Daemonize the horus process to constantly be accepting the traffic being sent to port 22. We would not want the user to run horus and then lose whatever shell they were currently using. As such, we would want the running of the horus engine to be outsourced to a child shell. Will have to think on this further. I believe daemonizing a python process is the best way to approach this problem.
2. Configure the horus host machine (i.e the server hosting Horus) to have another port open for remote connetions so we can maintain the server.
3. Create a subprocess call to handle the startup of a Docker container