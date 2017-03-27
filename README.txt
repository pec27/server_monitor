
Steps:

1. Copy example_servers.txt into servers.txt, setting your e-mail address and 
   the list of servers you want to monitor
2. Edit your crontab (crontab -e) with a line something like 
   */15 * * * * python ./codes/server_monitor/ping_servers.py codes/server_monitor/servers.txt
