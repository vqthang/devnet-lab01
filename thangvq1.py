print("Vo Quoc Thang")
hocsinh1 = {}
hocsinh1["Ten"] = "Vo Quoc Thang"
hocsinh1["Tuoi"] = "36"
hocsinh1["Don vi"] = "Viettel"
hocsinh2 = {}
hocsinh2["Ten"] = "AAA"
hocsinh2["Tuoi"] = "30"
hocsinh2["Don vi"] = "Viettel"
hocsinh3 = {}
hocsinh3["Ten"] = "BBB"
hocsinh3["Tuoi"] = "31"
hocsinh3["Don vi"] = "Viettel"
hocsinh4 = {}
hocsinh4["Ten"] = "CCC"
hocsinh4["Tuoi"] = "32"
hocsinh4["Don vi"] = "Viettel"
hocsinh5 = {}
hocsinh5["Ten"] = "DDD"
hocsinh5["Tuoi"] = "33"
hocsinh5["Don vi"] = "Viettel"
lophoc = [hocsinh1,hocsinh2,hocsinh3,hocsinh4,hocsinh5]
for x in lophoc:
    print("--------------------")
    print("Ten:" + x['Ten'])
    print("Tuoi:" + x['Tuoi'])
    print("Don vi:" + x['Don vi'])
print("---------------")
