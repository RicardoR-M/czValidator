def sheet_name():
    return 'Data'


def col_fecha_monitoreo():
    return 'F'


def col_fecha_llamada():
    return 'I'


def col_sn():
    return 'H'


def get_cz_tec():
    return '***REMOVED***'


def get_cz_adm():
    return 'RAQUEL NAYSHA SORJANO ESPINOZA'


def get_cz_post():
    return '***REMOVED***'


validaciones_tec = [dict(cabecera='CODIGO DEL ASESOR', col='A', tipo='usuario'),
                    dict(cabecera='NOMBRE DEL ASESOR', col='B', tipo='texto'),
                    dict(cabecera='FECHA DE MONITOREO', col='F', tipo='fecha'),
                    dict(cabecera='SN - IPCC', col='H', tipo='sn'),
                    dict(cabecera='FECHA DE LA LLAMADA', col='I', tipo='fecha'),
                    dict(cabecera='NOMBRE DEL CLIENTE', col='L', tipo='texto'),
                    dict(cabecera='NRO° TELFONO DEL QUE LLAMA (MSISDN )', col='M', tipo='numero'),
                    dict(cabecera=' NRO°  INDENTIFICADO  (TELEFONO EN CONSULTA)', col='N', tipo='numero'),
                    dict(cabecera='TIPO DE LLAMADA', col='O', tipo='texto'),
                    dict(cabecera='MOTIVO DE CONSULTA', col='P', tipo='no_vacio'),
                    dict(cabecera='NOMBRE DEL MONITOR', col='Z', tipo='monitor_cz'),
                    dict(cabecera='SUB  CALIFICACIÓN', col='BJ', tipo='numero'),
                    dict(cabecera='CALIFICACIÓN FINAL', col='BP', tipo='numero'),
                    dict(cabecera='FCR', col='BV', tipo='sino'),
                    dict(cabecera='RESPONSABILIDAD DE NO FCR', col='BW', tipo='fcr'),
                    dict(cabecera='MOTIVO DE NO FCR', col='BX', tipo='no_si'),
                    dict(cabecera='PROCESO CLARO NO FCR', col='BY', tipo='no_si'),
                    dict(cabecera='DETALLE DE NO FCR', col='BZ', tipo='detalle_nofcr'),
                    dict(cabecera='ACCION QUE REALIZO  EL ASESOR', col='CA', tipo='no_si'),
                    dict(cabecera='NPS', col='CB', tipo='vacio'),
                    dict(cabecera='TNPS ', col='CC', tipo='vacio'),
                    dict(cabecera='OBSERVACION / RECOMENDACIÓN', col='CE', tipo='obs_recomendacion'),
                    dict(cabecera='Semana de llamada', col='CF', tipo='vacio'),
                    dict(cabecera='Semana de monitoreo', col='CG', tipo='vacio'),
                    dict(cabecera='Adherencia al proceso', col='CH', tipo='sino')
                    ]

validaciones_post = [dict(cabecera='CODIGO DEL ASESOR', col='A', tipo='usuario'),
                     dict(cabecera='NOMBRE DEL ASESOR', col='B', tipo='texto'),
                     dict(cabecera='FECHA DE MONITOREO', col='F', tipo='fecha'),
                     dict(cabecera='SN - IPCC', col='H', tipo='sn'),
                     dict(cabecera='FECHA DE LA LLAMADA', col='I', tipo='fecha'),
                     dict(cabecera='NOMBRE DEL CLIENTE', col='L', tipo='texto'),
                     dict(cabecera='NRO° TELFONO DEL QUE LLAMA (MSISDN )', col='M', tipo='numero'),
                     dict(cabecera=' NRO°  INDENTIFICADO  (TELEFONO EN CONSULTA)', col='N', tipo='numero'),
                     dict(cabecera='TIPO DE LLAMADA', col='O', tipo='texto'),
                     dict(cabecera='MOTIVO DE CONSULTA', col='P', tipo='no_vacio'),
                     dict(cabecera='NOMBRE DEL MONITOR', col='Z', tipo='monitor_cz'),
                     dict(cabecera='SUB  CALIFICACIÓN', col='AZ', tipo='numero'),  # Varia en cuanto a tec
                     dict(cabecera='CALIFICACIÓN FINAL', col='BF', tipo='numero'),  # varia en cuanto a tec
                     dict(cabecera='FCR', col='BL', tipo='sino'),  # varia en cuanto a tec
                     dict(cabecera='RESPONSABILIDAD DE NO FCR', col='BM', tipo='fcr'),  # Varia
                     dict(cabecera='MOTIVO DE NO FCR', col='BN', tipo='no_si'),  # varia
                     dict(cabecera='PROCESO CLARO NO FCR', col='BO', tipo='no_si'),  # Varia
                     dict(cabecera='DETALLE DE NO FCR', col='BP', tipo='detalle_nofcr'),  # Varia
                     dict(cabecera='ACCION QUE REALIZO  EL ASESOR', col='BQ', tipo='no_si'),  # Varia
                     dict(cabecera='NPS', col='BR', tipo='vacio'),
                     dict(cabecera='TNPS ', col='BS', tipo='vacio'),
                     dict(cabecera='OBSERVACION / RECOMENDACIÓN', col='BU', tipo='obs_recomendacion'),
                     # dict(cabecera='Semana de llamada', col='CH', tipo='vacio'),
                     # dict(cabecera='Semana de monitoreo', col='CI', tipo='vacio'),
                     # dict(cabecera='Adherencia al proceso', col='CJ', tipo='sino')
                     ]

validaciones_adm = [dict(cabecera='CODIGO DEL ASESOR', col='A', tipo='usuario'),
                    dict(cabecera='NOMBRE DEL ASESOR', col='B', tipo='texto'),
                    dict(cabecera='FECHA DE MONITOREO', col='F', tipo='fecha'),
                    dict(cabecera='SN - IPCC', col='H', tipo='sn'),
                    dict(cabecera='FECHA DE LA LLAMADA', col='I', tipo='fecha'),
                    dict(cabecera='NOMBRE DEL CLIENTE', col='L', tipo='texto'),
                    dict(cabecera='NRO° TELFONO DEL QUE LLAMA (MSISDN )', col='M', tipo='numero'),
                    dict(cabecera=' NRO°  INDENTIFICADO  (TELEFONO EN CONSULTA)', col='N', tipo='numero'),
                    dict(cabecera='TIPO DE LLAMADA', col='O', tipo='texto'),
                    dict(cabecera='MOTIVO DE CONSULTA', col='P', tipo='no_vacio'),
                    dict(cabecera='NOMBRE DEL MONITOR', col='Z', tipo='monitor_cz'),
                    dict(cabecera='SUB  CALIFICACIÓN', col='BL', tipo='numero'),  # Varia en cuanto a tec
                    dict(cabecera='CALIFICACIÓN FINAL', col='BR', tipo='numero'),  # varia en cuanto a tec
                    dict(cabecera='FCR', col='BX', tipo='sino'),  # varia en cuanto a tec
                    dict(cabecera='RESPONSABILIDAD DE NO FCR', col='BY', tipo='fcr'),  # Varia
                    dict(cabecera='MOTIVO DE NO FCR', col='BZ', tipo='no_si'),  # varia
                    dict(cabecera='PROCESO CLARO NO FCR', col='CA', tipo='no_si'),  # Varia
                    dict(cabecera='DETALLE DE NO FCR', col='CB', tipo='detalle_nofcr'),  # Varia
                    dict(cabecera='ACCION QUE REALIZO  EL ASESOR', col='CC', tipo='no_si'),  # Varia
                    dict(cabecera='NPS', col='CD', tipo='vacio'),
                    dict(cabecera='TNPS ', col='CE', tipo='vacio'),
                    dict(cabecera='OBSERVACION / RECOMENDACIÓN', col='CG', tipo='obs_recomendacion'),
                    dict(cabecera='Semana de llamada', col='CH', tipo='vacio'),
                    dict(cabecera='Semana de monitoreo', col='CI', tipo='vacio'),
                    dict(cabecera='Adherencia al proceso', col='CJ', tipo='sino')
                    ]
