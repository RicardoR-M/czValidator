import datetime
from re import search

from conf import get_cz_tec, col_fecha_monitoreo, col_fecha_llamada, get_cz_adm, get_cz_post
from plantillas import ErrorValidacion


def usuario(value):
    # return Resp(bool(search(r'^E', str(value))), '')
    return bool(not search(r'^E', str(value)) or search(r'[^E0-9]+', str(value)))


def texto(value):
    if value is None:
        return True
    return bool(search(r'[\#\!\_\-\+\!\¡\.0-9]+', value))


def texto_none(value):
    if value is None:
        return False
    return bool(search(r'[\#\!\_\-\+\!\¡0-9]+', value))


def fecha(value):
    if not isinstance(value, datetime.datetime):
        return True
    return False


def numero(value):
    if value is None:
        return True
    return not bool(search(r'[\d.]+', str(value)))


def telf(value):
    if value is None or value == '':
        return False
    return not bool(search(r'[\d.]+', str(value)))


def no_vacio(value):
    if value is None or value == '':
        return True
    return False


def monitor_cz(value):
    if value == get_cz_tec() or value == get_cz_adm() or value == get_cz_post():
        return False
    return True


def sino(value):
    if value == 'SI' or value == 'NO':
        return False
    return True


def fcr(value):
    if value is None:
        return False
    if value.upper() == 'CLARO' or value.upper() == 'ASESOR' or value.upper() == 'CLIENTE' or value == '':
        return False
    return True


def no_si(value):
    if value == 'SI':
        return True
    return False


def detalle_nofcr(value):
    if value is None:
        return False
    return bool(search(r'\>', value))


def vacio(value):
    if value is None or value == '':
        return False
    return True


def obs_recomendacion(value):
    if value == '---' or value == '--' or value == '-':
        return True
    return False


def sn(value):
    if value is None:
        return True
    return bool(search(r'[^0-9]+', value))


def fechas_cz(monitoreo, llamada, fila):
    if monitoreo is None or llamada is None:
        return ErrorValidacion(fila=fila,
                               col=f'{col_fecha_monitoreo()}-{col_fecha_llamada()}',
                               cabecera='F.Monitoreo - F.Llamada',
                               valor=f'{monitoreo}-{llamada}', msg='Fecha de monitoreo o llamada con valor incorrecto')

    res = monitoreo.day - llamada.day
    if res > 2 or res == 0:
        return ErrorValidacion(fila=fila,
                               col=f'{col_fecha_monitoreo()}-{col_fecha_llamada()}',
                               cabecera='F.Monitoreo - F.Llamada',
                               valor=res, msg='Inconsistencia entre la fecha de monitoreo y llamada')
    return False


def tipo_llamada(value):
    if value is None:
        return True
    elif value != 'INFORMATIVO' and value != 'RECLAMO' and value != 'VARIACION':
        return True
    return False
