import io

import click

from comparacion.infComp import comparator_cz
from conf import validaciones_tec, validaciones_adm, validaciones_post
from validacion.infValidator import check_cz


@click.command()
@click.argument('inf_anterior')
@click.argument('inf_now')
@click.argument('skill')
def aplicacion(inf_anterior, inf_now, skill):
    with open(inf_anterior, 'rb') as f:
        mem_file_anterior = io.BytesIO(f.read())

    with open(inf_now, 'rb') as f:
        mem_file_now = io.BytesIO(f.read())

    print('#' * 60)
    print('REPORTE DE COMPARACIÓN:')
    print('-' * 40)
    comparator_cz(mem_file_anterior, mem_file_now)
    print('#' * 60)
    if skill.upper() == 'TEC':
        validaciones = validaciones_tec
    elif skill.upper() == 'ADM':
        validaciones = validaciones_adm
    elif skill.upper() == 'POS':
        validaciones = validaciones_post
    else:
        raise RuntimeError('No se selecciono un skill correcto')

    print('#' * 60)
    print('REPORTE DE VALIDACIONES:')
    print('-' * 40)
    check_cz(inf_now, validaciones)
    print('#' * 60)


if __name__ == '__main__':
    aplicacion()
