def read_ips():
    attack_ues=["imsi-208930000000105", 
                    "imsi-208930000000111",
                    "imsi-208930000000128",
                        "imsi-208930000000130", 
                        "imsi-208930000000133", 
                        "imsi-208930000000138",
                            "imsi-208930000000140", 
                            "imsi-208930000000143", 
                                "imsi-208930000000148", 
                                "imsi-208930000000151", 
                                    "imsi-208930000000153"]

    attack_ues_ip = []
    for i in range (0, len(attack_ues)):
        filename = f"{attack_ues[i]}_attack_ip.txt"
        with open(filename, 'r') as file:
            ip = file.read() 
            attack_ues_ip.append(ip)
    return attack_ues_ip