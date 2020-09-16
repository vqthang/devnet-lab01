router_list = [{'Name':'R1','IP':'36.37.255.1','OS':'Juniper'},{'Name':'R2','IP':'36.37.255.2','OS':'Juniper'},{'Name':'R3','IP':'36.37.254.1','OS':'Juniper'},{'Name':'R4','IP':'36.37.254.2','OS':'Juniper'},{'Name':'R5','IP':'36.37.255.3','OS':'Juniper'}]
def FindRouter(rlist,name):
    for router in rlist:
        #for i in router:
        if router['Name'] == name:
            print('Name :' + router['Name'])
            print('IP :' + router['IP'])
            print('OS :' + router['OS'])
            break
        #print('------------------------')
        #break
FindRouter(router_list,"R2")