def sheet_name():
    return 'Data'


def col_fecha_monitoreo():
    return 'F'


def col_fecha_llamada():
    return 'H'


def col_sn():
    return 'G'


def get_cz_tec():
    # return '***REMOVED***'
    return '***REMOVED***'


def get_cz_adm():
    return '***REMOVED***'


def get_cz_post():
    return '***REMOVED***'


validaciones_tec = [dict(cabecera='CODIGO DEL ASESOR', col='A', tipo='usuario'),
                    dict(cabecera='NOMBRE DEL ASESOR', col='B', tipo='texto'),
                    dict(cabecera='FECHA DE MONITOREO', col='F', tipo='fecha'),
                    dict(cabecera='SN - IPCC', col='G', tipo='sn'),
                    dict(cabecera='FECHA DE LA LLAMADA', col='H', tipo='fecha'),
                    dict(cabecera='NOMBRE DEL CLIENTE', col='K', tipo='texto_none'),
                    dict(cabecera='NRO° TELFONO DEL QUE LLAMA (MSISDN )', col='L', tipo='telf'),
                    dict(cabecera=' NRO°  INDENTIFICADO  (TELEFONO EN CONSULTA)', col='M', tipo='telf'),
                    dict(cabecera='TIPO DE LLAMADA', col='N', tipo='tipo_llamada'),
                    dict(cabecera='MOTIVO DE CONSULTA', col='O', tipo='no_vacio'),
                    dict(cabecera='NOMBRE DEL MONITOR', col='W', tipo='monitor_cz'),
                    dict(cabecera='SUB  CALIFICACIÓN', col='BH', tipo='numero'),
                    dict(cabecera='CALIFICACIÓN FINAL', col='BN', tipo='numero'),
                    dict(cabecera='FCR', col='BV', tipo='sino'),
                    dict(cabecera='RESPONSABILIDAD DE NO FCR', col='BW', tipo='fcr'),
                    dict(cabecera='MOTIVO DE NO FCR', col='BX', tipo='no_si'),
                    dict(cabecera='PROCESO CLARO NO FCR', col='BY', tipo='no_si'),
                    dict(cabecera='DETALLE DE NO FCR', col='BZ', tipo='detalle_nofcr'),
                    dict(cabecera='ACCION QUE REALIZO  EL ASESOR', col='CA', tipo='no_si'),
                    dict(cabecera='NPS', col='CB', tipo='vacio'),
                    dict(cabecera='TNPS ', col='CC', tipo='vacio'),
                    dict(cabecera='OBSERVACION / RECOMENDACIÓN', col='CE', tipo='obs_recomendacion')
                    ]

validaciones_post = [dict(cabecera='CODIGO DEL ASESOR', col='A', tipo='usuario'),
                     dict(cabecera='NOMBRE DEL ASESOR', col='B', tipo='texto'),
                     dict(cabecera='FECHA DE MONITOREO', col='F', tipo='fecha'),
                     dict(cabecera='SN - IPCC', col='G', tipo='sn'),
                     dict(cabecera='FECHA DE LA LLAMADA', col='H', tipo='fecha'),
                     dict(cabecera='NOMBRE DEL CLIENTE', col='K', tipo='texto_none'),
                     dict(cabecera='NRO° TELFONO DEL QUE LLAMA (MSISDN )', col='L', tipo='telf'),
                     dict(cabecera=' NRO°  INDENTIFICADO  (TELEFONO EN CONSULTA)', col='M', tipo='telf'),
                     dict(cabecera='TIPO DE LLAMADA', col='N', tipo='tipo_llamada'),
                     dict(cabecera='MOTIVO DE CONSULTA', col='O', tipo='no_vacio'),
                     dict(cabecera='NOMBRE DEL MONITOR', col='W', tipo='monitor_cz'),
                     dict(cabecera='SUB  CALIFICACIÓN', col='AZ', tipo='numero'),  # Varia en cuanto a tec
                     dict(cabecera='CALIFICACIÓN FINAL', col='BF', tipo='numero'),  # varia en cuanto a tec
                     dict(cabecera='FCR', col='BN', tipo='sino'),  # varia en cuanto a tec
                     dict(cabecera='RESPONSABILIDAD DE NO FCR', col='BO', tipo='fcr'),  # Varia
                     dict(cabecera='MOTIVO DE NO FCR', col='BP', tipo='no_si'),  # varia
                     dict(cabecera='PROCESO CLARO NO FCR', col='BQ', tipo='no_si'),  # Varia
                     dict(cabecera='DETALLE DE NO FCR', col='BR', tipo='detalle_nofcr'),  # Varia
                     dict(cabecera='ACCION QUE REALIZO  EL ASESOR', col='BS', tipo='no_si'),  # Varia
                     dict(cabecera='NPS', col='BT', tipo='vacio'),
                     dict(cabecera='TNPS ', col='BU', tipo='vacio'),
                     dict(cabecera='OBSERVACION / RECOMENDACIÓN', col='BW', tipo='obs_recomendacion'),
                     ]

validaciones_adm = [dict(cabecera='CODIGO DEL ASESOR', col='A', tipo='usuario'),
                    dict(cabecera='NOMBRE DEL ASESOR', col='B', tipo='texto'),
                    dict(cabecera='FECHA DE MONITOREO', col='F', tipo='fecha'),
                    dict(cabecera='SN - IPCC', col='G', tipo='sn'),
                    dict(cabecera='FECHA DE LA LLAMADA', col='H', tipo='fecha'),
                    dict(cabecera='NOMBRE DEL CLIENTE', col='K', tipo='texto_none'),
                    dict(cabecera='NRO° TELFONO DEL QUE LLAMA (MSISDN )', col='L', tipo='telf'),
                    dict(cabecera=' NRO°  INDENTIFICADO  (TELEFONO EN CONSULTA)', col='M', tipo='telf'),
                    dict(cabecera='TIPO DE LLAMADA', col='N', tipo='tipo_llamada'),
                    dict(cabecera='MOTIVO DE CONSULTA', col='O', tipo='no_vacio'),
                    dict(cabecera='NOMBRE DEL MONITOR', col='W', tipo='monitor_cz'),
                    dict(cabecera='SUB  CALIFICACIÓN', col='BF', tipo='numero'),  # Varia en cuanto a tec
                    dict(cabecera='CALIFICACIÓN FINAL', col='BL', tipo='numero'),  # varia en cuanto a tec
                    dict(cabecera='FCR', col='BT', tipo='sino'),  # varia en cuanto a tec
                    dict(cabecera='RESPONSABILIDAD DE NO FCR', col='BU', tipo='fcr'),  # Varia
                    dict(cabecera='MOTIVO DE NO FCR', col='BV', tipo='no_si'),  # varia
                    dict(cabecera='PROCESO CLARO NO FCR', col='BW', tipo='no_si'),  # Varia
                    dict(cabecera='DETALLE DE NO FCR', col='BX', tipo='detalle_nofcr'),  # Varia
                    dict(cabecera='ACCION QUE REALIZO  EL ASESOR', col='BY', tipo='no_si'),  # Varia
                    dict(cabecera='NPS', col='BZ', tipo='vacio'),
                    dict(cabecera='TNPS ', col='CA', tipo='vacio'),
                    dict(cabecera='OBSERVACION / RECOMENDACIÓN', col='CC', tipo='obs_recomendacion'),
                    ]
