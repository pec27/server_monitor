import smtplib
import subprocess
from sys import argv

def email(me, txt="A test message"):
    to = [me]

    s = smtplib.SMTP('localhost')
    s.sendmail(me, to, txt)
    s.quit()

def check_responds(host = "charon1"):

    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
        )
    out, err = ping.communicate()
    responds = "0 received" not in out
    return responds
    
        
if __name__=='__main__':
    name = argv[1]
    f = open(name, "r")
    output = ''
    lines = f.readlines()
    eml_addr = lines[0].split()[0]

    output += lines[0]
    response = ''
    for line in lines[1:]:
        machine, status = line.split(' ')
        status = status[:-1] # remove carriage return
        new_status = {True:'up',False:'down'}[check_responds(machine)]
        if status != new_status:
            response += '%s is now %s (was %s)\n'%(machine, new_status, status)


        output += ' '.join((machine,new_status)) + '\n'

    f.close()
    
    if len(response):
        email(eml_addr, response)
        # update the status
        f = open(name, "w")
        f.write(output)
        f.close()





