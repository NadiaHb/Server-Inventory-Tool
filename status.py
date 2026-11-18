#These are the only allowed statuses
status_varden = ["up", "down", "unknown"]


def kontrollera_status(status):#Cheking for valid status
    if status in status_varden:
        return True
    else:
        return False


def visa_status(status):#
    if status == "up":
        return "Servern är på"
    elif status == "down":
        return "Servern svarar ej"
    elif status == "unknown":
        return "Var god kontrollera servern"
    else:
        return "Ogiltlig status"