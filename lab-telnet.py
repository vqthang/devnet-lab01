import pexpect

host="36.37.255.1"
username = "thangvq1"
password = "********"
command1 = "show interface description | no-more | match ae"
command2 = "show interface ae0 | no-more"
session = pexpect.spawn("telnet "+format(host)+" -l "+username, timeout=20)
result = session.expect ("Password:")
if result == 0:
    session.sendline (password)
#session.sendline("\r\n")
result = session.expect(["> ", pexpect.TIMEOUT])
if result == 0: #password was correct
    result = session.sendline("set cli screen-length 1000")
    result = session.sendline("set cli screen-width 1000")
    result = session.sendline(command1)
    #print("Result of sendline cmd1:")
    #print(format(result))
    #print("\n\r")
    output = format(session.read(1292))
    output.replace('\r','')
    print(output.replace('r\\n','\n'))
    #print("\n\r")
    #print(session.before)
    #print("\n\r")
    #print(session.after)
    #print("\n\r")
    #result = session.sendline(command2)
    #print("Result of sendline cmd2:")
    #print(format(result))
    #print("\n\r")
    #print(session.read(1572))
    print ("Success")
elif result == 1:
    print ("Bad Result")
session.close()