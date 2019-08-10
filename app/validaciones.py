import datetime


def usuario(value):
    if not isinstance(value, str) or value == '' or value is None:
        return True
    elif value.find('E') != 0:
        return True
    else:
        return False


def texto(value):
    pass


def fecha(value):
    if not isinstance(value, datetime.datetime):
        return True
    return False


def numero(value):
    pass


def no_vacio(value):
    if value is None or value == '':
        return True
    return False


def monitor_cz(value):
    if value == '***REMOVED***':
        return False
    return True


def sino(value):
    if value == 'SI' or value == 'NO':
        return False
    return True


def fcr(value):
    pass


def no_si(value):
    if value == 'SI':
        return True
    return False


def detalle_nofcr(value):
    pass


def vacio(value):
    if value is None or value == '':
        return False
    return True


def obs_recomendacion(value):
    if value == '---' or value == '--' or value == '-':
        return True
    return False


def sn(value):
    pass
