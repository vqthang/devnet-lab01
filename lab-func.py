def chia2so(sobichia,sochia):
    if type(sobichia) == int and type(sochia) == int:
        if (sochia == 0):
            print("Khong the chia cho 0.")
        else:
            print("So bi chia: " + format(sobichia))
            print ("So chia: " + format(sochia))
            print("Ket qua: " + format(sobichia/sochia))
    else:
        print("Sai dau vao.")
chia2so("10",5)