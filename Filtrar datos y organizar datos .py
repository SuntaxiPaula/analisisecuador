#============================= PLANTAMIENTO DE CODIGO =========================================
#   ENTIENDO QUE ESTO SE VEA HORRIBLE, PERO LO VOY A IR EXPLICANDO PASO A PASO
#  TU TIENES QUE ESCRIBIR EL CODIGO SEGUN TUS NECESIDADES, PERO LO QUE VAS A USAR SÍ O SÍ  SON LOS NOMBRES DE LAS CUENTAS
#   MIS CRITERIOS DE FILTRO PARA DIFERENCIAR PEQUEÑAS, MEDIANAS Y GRANDES EMPRESAS:
#   PEQUEÑAS EMPRESAS =  INGRESOS < 1000000
#   MEDIANAS EMPRESAS=  INGRESOS > 1000000 and INGRESOS < 5000000
#   GRANDES EMPRESAS = INGRESOS > 5000000
#   Ademas, solo debe ser consideradas las empresas que contengan la string 'C10'en la columna 'CIUU' 
#   EL CODIGO SE 


# EJEMPLO
# PASO 1, DEBES IMPORTAR LAS LIBRERIAS
import pandas as pd 
import nympy as np

#PASO 2: IMPORTAR EL ARCHIVO CON EL ESTADO FINANCIERO

pd.read_csv('2020.txt', sep = '\t', lowmemory = false)

## PASO 3:  DECLARAR TUS CRITERIOS DE FILTROS, YO FILTRÉ POR INGRESOS Y POR ACTIVIDAD ECONOMICA
#EN ESTE CASO SON LAS PEQUEÑAS EMPRESAS, TU FILTRA COMO QUIERAS SI NO SABES MIRA UN TUTORIAL DE FILTRO CON PANDAS


# PEQUEÑAS EMPRESAS (INGRESOS MENORES A 1M DOLARES)

income20= (df['TOTAL_INGRESOS__6999'] < 1000000) & (df['CIIU'].str.contains('C10'))  #AQUI TO FILTRÉ POR C10

#income_20= (df['TOTAL_INGRESOS__6999'] > 5000000) 
#& (df['CIIU'].str.contains('C10')) 


pequenas2020 = df.loc[income20, ['NOMBRE','CIIU','TOTAL_INGRESOS__6999','TOTAL_ACTIVO_CORRIENTE_361', 'CDB_CLI_REL_LOCALES_312',
                 'CDB_CLI_REL_EXTERIOR_313', 'DET_CTAS_COB_INC__314', 'CDB_CLI_NRE_LOCALES_315',
                 'CDB_CLI_NRE_EXTERIOR_316', 'INVENTARIO_MATERIA_PRIMA_340', 'INV_PRODUCTOS_PROCESO_341',
                 'INVENTARIO_PTE_MAL_342', 'INV_MAT_BIE_NO_CONSTR_343', 'INV_MAT_BIE_CONSTR_344', 'INV_OBRA_CONSTRUCCION_345',
                 'INV_OBRA_TERMINADA_346','PRV_INV_POR_VTR_347',
                 'TOTAL_ACTIVO__499',
                 'CDP_PVE_CRR_REL_LOCALES__511', 'CDP_PVE_CRR_REL_EXTERIOR__512', 'CDP_PVE_CRR_NRE_LOCALES__513', 'CDP_PVE_CRR_NRE_EXTERIOR__514',
                 'TOTAL_PASIVOS__599',
                 'CAPITAL_SUSCRITO_ASIGNADO_601', 'TOTAL_PATRIMONIO_NETO__698',
                  'VLN_EAF_TDC__6001', 'VEX_VLN_EAF_TDC__6002', 'VLN_EAF_TCE__6003', 'VEX_VLN_EAF_TCE__6004', 'PRE_LOC_SER_GRAV_TAR_12__6005',	'VEX_PRE_LOC_SER_GRA_TR_12_6006',	'PRE_LOC_SER_GRAV_TAR_0__6007', 'VEX_PRE_LOC_SER_GRA_TAR_0_6008', 'EXPORTACIONES_NETAS__6009', 'VEX_EXPORTACIONES_NETAS__6010',
                 'CTO_IVI_BIENES_NPP__7001',	'CTO_CLN_BIENES_NPP__7004'	, 'CTO_IPR_BIENES_NPP__7007',
	             'GTO_IPR_BIENES_NPP__7008',	'CTO_IVF_BIENES_NPP__7010', 'CTO_IVI_MATERIA_PRIMA__7013','CTO_CLN_MATERIA_PRIMA__7016',
                'CTO_IPR_MATERIA_PRIMA__7019','CTO_IVF_MATERIA_PRIMA__7022','COSTO_IVI_PPR__7025', 'COSTO_IVF_PPR__7028', 'COSTO_IVI_PTE__7031', 'COSTO_IVF_PTE__7034',
                 'UTILIDAD_GRAVABLE__836']]

#GRANDES EMPRESAS (INGRESOS MAYORES A 5M DOLARES)

income_grandes20= (df['TOTAL_INGRESOS__6999'] > 5000000) & (df['CIIU'].str.contains('C10'))

grandes2020 = df.loc[income_grandes20, ['NOMBRE','CIIU','TOTAL_INGRESOS__6999','TOTAL_ACTIVO_CORRIENTE_361', 'CDB_CLI_REL_LOCALES_312',
                 'CDB_CLI_REL_EXTERIOR_313', 'DET_CTAS_COB_INC__314', 'CDB_CLI_NRE_LOCALES_315',
                 'CDB_CLI_NRE_EXTERIOR_316', 'INVENTARIO_MATERIA_PRIMA_340', 'INV_PRODUCTOS_PROCESO_341',
                 'INVENTARIO_PTE_MAL_342', 'INV_MAT_BIE_NO_CONSTR_343', 'INV_MAT_BIE_CONSTR_344', 'INV_OBRA_CONSTRUCCION_345',
                 'INV_OBRA_TERMINADA_346','PRV_INV_POR_VTR_347',
                 'TOTAL_ACTIVO__499',
                 'CDP_PVE_CRR_REL_LOCALES__511', 'CDP_PVE_CRR_REL_EXTERIOR__512', 'CDP_PVE_CRR_NRE_LOCALES__513', 'CDP_PVE_CRR_NRE_EXTERIOR__514',
                 'TOTAL_PASIVOS__599',
                 'CAPITAL_SUSCRITO_ASIGNADO_601', 'TOTAL_PATRIMONIO_NETO__698',
                  'VLN_EAF_TDC__6001', 'VEX_VLN_EAF_TDC__6002', 'VLN_EAF_TCE__6003', 'VEX_VLN_EAF_TCE__6004', 'PRE_LOC_SER_GRAV_TAR_12__6005',  'VEX_PRE_LOC_SER_GRA_TR_12_6006',   'PRE_LOC_SER_GRAV_TAR_0__6007', 'VEX_PRE_LOC_SER_GRA_TAR_0_6008', 'EXPORTACIONES_NETAS__6009', 'VEX_EXPORTACIONES_NETAS__6010',
                 'CTO_IVI_BIENES_NPP__7001',    'CTO_CLN_BIENES_NPP__7004'  , 'CTO_IPR_BIENES_NPP__7007',
                 'GTO_IPR_BIENES_NPP__7008',    'CTO_IVF_BIENES_NPP__7010', 'CTO_IVI_MATERIA_PRIMA__7013','CTO_CLN_MATERIA_PRIMA__7016',
                'CTO_IPR_MATERIA_PRIMA__7019','CTO_IVF_MATERIA_PRIMA__7022','COSTO_IVI_PPR__7025', 'COSTO_IVF_PPR__7028', 'COSTO_IVI_PTE__7031', 'COSTO_IVF_PTE__7034',
                 'UTILIDAD_GRAVABLE__836']]



#MEDIANAS EMPRESAS (INGRESOS ENTRE 1M Y 5M)

medianas2020 = (df['TOTAL_INGRESOS__6999'] > 1000000) & (df['CIIU'].str.contains('C10')& 
(df['TOTAL_INGRESOS__6999'] < 5000000))

medianas = df.loc[medianas2020, ['NOMBRE','CIIU','TOTAL_INGRESOS__6999','TOTAL_ACTIVO_CORRIENTE_361', 'CDB_CLI_REL_LOCALES_312',
                 'CDB_CLI_REL_EXTERIOR_313', 'DET_CTAS_COB_INC__314', 'CDB_CLI_NRE_LOCALES_315',
                 'CDB_CLI_NRE_EXTERIOR_316', 'INVENTARIO_MATERIA_PRIMA_340', 'INV_PRODUCTOS_PROCESO_341',
                 'INVENTARIO_PTE_MAL_342', 'INV_MAT_BIE_NO_CONSTR_343', 'INV_MAT_BIE_CONSTR_344', 'INV_OBRA_CONSTRUCCION_345',
                 'INV_OBRA_TERMINADA_346','PRV_INV_POR_VTR_347',
                 'TOTAL_ACTIVO__499',
                 'CDP_PVE_CRR_REL_LOCALES__511', 'CDP_PVE_CRR_REL_EXTERIOR__512', 'CDP_PVE_CRR_NRE_LOCALES__513', 'CDP_PVE_CRR_NRE_EXTERIOR__514',
                 'TOTAL_PASIVOS__599',
                 'CAPITAL_SUSCRITO_ASIGNADO_601', 'TOTAL_PATRIMONIO_NETO__698',
                  'VLN_EAF_TDC__6001', 'VEX_VLN_EAF_TDC__6002', 'VLN_EAF_TCE__6003', 'VEX_VLN_EAF_TCE__6004', 'PRE_LOC_SER_GRAV_TAR_12__6005',  'VEX_PRE_LOC_SER_GRA_TR_12_6006',   'PRE_LOC_SER_GRAV_TAR_0__6007', 'VEX_PRE_LOC_SER_GRA_TAR_0_6008', 'EXPORTACIONES_NETAS__6009', 'VEX_EXPORTACIONES_NETAS__6010',
                 'CTO_IVI_BIENES_NPP__7001',    'CTO_CLN_BIENES_NPP__7004'  , 'CTO_IPR_BIENES_NPP__7007',
                 'GTO_IPR_BIENES_NPP__7008',    'CTO_IVF_BIENES_NPP__7010', 'CTO_IVI_MATERIA_PRIMA__7013','CTO_CLN_MATERIA_PRIMA__7016',
                'CTO_IPR_MATERIA_PRIMA__7019','CTO_IVF_MATERIA_PRIMA__7022','COSTO_IVI_PPR__7025', 'COSTO_IVF_PPR__7028', 'COSTO_IVI_PTE__7031', 'COSTO_IVF_PTE__7034',
                 'UTILIDAD_GRAVABLE__836']]


# PASO 4: EXPORTAR YA TUS DATOS FILTRADOS A FORMATO CSV PARA QUE PUEDAS LEERLOS CON EXCEL Y ORGANIZARLOS
# A TU GUSTO

grandes2020.to_csv('pequenas empresas.csv')
pequenas20202.to_csv('pequenas empresas.csv')
medianas2020.to_csv('medianas empresas.csv')

#PASO 5:  REALIZAR REGRESION (ESTO LO EXPLICO EN EL OTRO CODIGO)

#IMPORTANTE:  EJECUTALO SOLO HASTA AQUÍ! PORQUE EN OTROS AÑOS CAMBIAN LOS NOMBRES DE LAS CUENTAS
#PERO NO TE PREOCUPES DEJO TODOS LOS NUEVOS NOMBRES, AÑO POR AÑO ABAJO. SOLO REPITE EL PROCESO, PERO CON 
#EL CODIGO DE ABAJO

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#REPETIR EL PROCESO PARA CADA AÑO,
#Formula para importar cada ano
# pd.read_csv('2019.txt', sep = '\t')

#ESTOS NOMBRES DE LAS CUENTAS SIRVEN PARA LOS AÑOS 2020,2019,2017,2016,2015,2014

#small business
income_pequenas17 = (df['TOTAL_INGRESOS__6999'] < 1000000 ) & (df['CIIU'].str.contains('C10'))

pequenas = df.loc [income_pequenas17, ['NOMBRE','CIIU','TOTAL_INGRESOS__6999','TOTAL_ACTIVO_CORRIENTE_361', 'CDB_CLI_REL_LOCALES_312',
                 'CDB_CLI_REL_EXTERIOR_313', 'DET_CTAS_COB_INC__314', 'CDB_CLI_NRE_LOCALES_315',
                 'CDB_CLI_NRE_EXTERIOR_316', 'MERCADERIAS_TRANSITO_339', 'INVENTARIO_MATERIA_PRIMA_340', 'INV_PRODUCTOS_PROCESO_341',
                 'INVENTARIO_PTE_MAL_342', 'INV_MAT_BIE_NO_CONSTR_343', 'INV_MAT_BIE_CONSTR_344', 'INV_OBRA_CONSTRUCCION_345',
                 'INV_OBRA_TERMINADA_346','PRV_INV_POR_VTR_347',
                 'TOTAL_ACTIVO__499',
                 'CDP_PVE_CRR_REL_LOCALES__511', 'CDP_PVE_CRR_REL_EXTERIOR__512', 'CDP_PVE_CRR_NRE_LOCALES__513', 'CDP_PVE_CRR_NRE_EXTERIOR__514',
                 'TOTAL_PASIVOS__599',
                 'CAPITAL_SUSCRITO_ASIGNADO_601', 'TOTAL_PATRIMONIO_NETO__698',
                  'VLN_EAF_TDC__6001', 'VEX_VLN_EAF_TDC__6002', 'VLN_EAF_TCE__6003', 'VEX_VLN_EAF_TCE__6004', 'PRE_LOC_SER_GRAV_TAR_12__6005',  'VEX_PRE_LOC_SER_GRA_TR_12_6006',   'PRE_LOC_SER_GRAV_TAR_0__6007', 'VEX_PRE_LOC_SER_GRA_TAR_0_6008', 'EXPORTACIONES_NETAS__6009', 'VEX_EXPORTACIONES_NETAS__6010',
                 'CTO_IVI_BIENES_NPP__7001',    'CTO_CLN_BIENES_NPP__7004'  , 'CTO_IPR_BIENES_NPP__7007',
                 'GTO_IPR_BIENES_NPP__7008',    'CTO_IVF_BIENES_NPP__7010', 'CTO_IVI_MATERIA_PRIMA__7013','CTO_CLN_MATERIA_PRIMA__7016',
                'CTO_IPR_MATERIA_PRIMA__7019','CTO_IVF_MATERIA_PRIMA__7022','COSTO_IVI_PPR__7025', 'COSTO_IVF_PPR__7028', 'COSTO_IVI_PTE__7031', 'COSTO_IVF_PTE__7034',
                 'UTILIDAD_GRAVABLE__836']]

#big companies
income_grandes17 = (df['TOTAL_INGRESOS__6999'] > 5000000 ) & (df['CIIU'].str.contains('C10'))

grandes = df.loc [income_grandes17, ['NOMBRE','CIIU','TOTAL_INGRESOS__6999','TOTAL_ACTIVO_CORRIENTE_361', 'CDB_CLI_REL_LOCALES_312',
                 'CDB_CLI_REL_EXTERIOR_313', 'DET_CTAS_COB_INC__314', 'CDB_CLI_NRE_LOCALES_315',
                 'CDB_CLI_NRE_EXTERIOR_316', 'MERCADERIAS_TRANSITO_339', 'INVENTARIO_MATERIA_PRIMA_340', 'INV_PRODUCTOS_PROCESO_341',
                 'INVENTARIO_PTE_MAL_342', 'INV_MAT_BIE_NO_CONSTR_343', 'INV_MAT_BIE_CONSTR_344', 'INV_OBRA_CONSTRUCCION_345',
                 'INV_OBRA_TERMINADA_346','PRV_INV_POR_VTR_347',
                 'TOTAL_ACTIVO__499',
                 'CDP_PVE_CRR_REL_LOCALES__511', 'CDP_PVE_CRR_REL_EXTERIOR__512', 'CDP_PVE_CRR_NRE_LOCALES__513', 'CDP_PVE_CRR_NRE_EXTERIOR__514',
                 'TOTAL_PASIVOS__599',
                 'CAPITAL_SUSCRITO_ASIGNADO_601', 'TOTAL_PATRIMONIO_NETO__698',
                  'VLN_EAF_TDC__6001', 'VEX_VLN_EAF_TDC__6002', 'VLN_EAF_TCE__6003', 'VEX_VLN_EAF_TCE__6004', 'PRE_LOC_SER_GRAV_TAR_12__6005',  'VEX_PRE_LOC_SER_GRA_TR_12_6006',   'PRE_LOC_SER_GRAV_TAR_0__6007', 'VEX_PRE_LOC_SER_GRA_TAR_0_6008', 'EXPORTACIONES_NETAS__6009', 'VEX_EXPORTACIONES_NETAS__6010',
                 'CTO_IVI_BIENES_NPP__7001',    'CTO_CLN_BIENES_NPP__7004'  , 'CTO_IPR_BIENES_NPP__7007',
                 'GTO_IPR_BIENES_NPP__7008',    'CTO_IVF_BIENES_NPP__7010', 'CTO_IVI_MATERIA_PRIMA__7013','CTO_CLN_MATERIA_PRIMA__7016',
                'CTO_IPR_MATERIA_PRIMA__7019','CTO_IVF_MATERIA_PRIMA__7022','COSTO_IVI_PPR__7025', 'COSTO_IVF_PPR__7028', 'COSTO_IVI_PTE__7031', 'COSTO_IVF_PTE__7034',
                 'UTILIDAD_GRAVABLE__836']]

#medium business

income_medianas17 = (df['TOTAL_INGRESOS__6999'] > 1000000) & (df['CIIU'].str.contains('C10') &
(df['TOTAL_INGRESOS__6999'] < 5000000))

medianas = df.loc [income_medianas17, ['NOMBRE','CIIU','TOTAL_INGRESOS__6999','TOTAL_ACTIVO_CORRIENTE_361', 'CDB_CLI_REL_LOCALES_312',
                 'CDB_CLI_REL_EXTERIOR_313', 'DET_CTAS_COB_INC__314', 'CDB_CLI_NRE_LOCALES_315',
                 'CDB_CLI_NRE_EXTERIOR_316', 'MERCADERIAS_TRANSITO_339', 'INVENTARIO_MATERIA_PRIMA_340', 'INV_PRODUCTOS_PROCESO_341',
                 'INVENTARIO_PTE_MAL_342', 'INV_MAT_BIE_NO_CONSTR_343', 'INV_MAT_BIE_CONSTR_344', 'INV_OBRA_CONSTRUCCION_345',
                 'INV_OBRA_TERMINADA_346','PRV_INV_POR_VTR_347',
                 'TOTAL_ACTIVO__499',
                 'CDP_PVE_CRR_REL_LOCALES__511', 'CDP_PVE_CRR_REL_EXTERIOR__512', 'CDP_PVE_CRR_NRE_LOCALES__513', 'CDP_PVE_CRR_NRE_EXTERIOR__514',
                 'TOTAL_PASIVOS__599',
                 'CAPITAL_SUSCRITO_ASIGNADO_601', 'TOTAL_PATRIMONIO_NETO__698',
                  'VLN_EAF_TDC__6001', 'VEX_VLN_EAF_TDC__6002', 'VLN_EAF_TCE__6003', 'VEX_VLN_EAF_TCE__6004', 'PRE_LOC_SER_GRAV_TAR_12__6005',  'VEX_PRE_LOC_SER_GRA_TR_12_6006',   'PRE_LOC_SER_GRAV_TAR_0__6007', 'VEX_PRE_LOC_SER_GRA_TAR_0_6008', 'EXPORTACIONES_NETAS__6009', 'VEX_EXPORTACIONES_NETAS__6010',
                 'CTO_IVI_BIENES_NPP__7001',    'CTO_CLN_BIENES_NPP__7004'  , 'CTO_IPR_BIENES_NPP__7007',
                 'GTO_IPR_BIENES_NPP__7008',    'CTO_IVF_BIENES_NPP__7010', 'CTO_IVI_MATERIA_PRIMA__7013','CTO_CLN_MATERIA_PRIMA__7016',
                'CTO_IPR_MATERIA_PRIMA__7019','CTO_IVF_MATERIA_PRIMA__7022','COSTO_IVI_PPR__7025', 'COSTO_IVF_PPR__7028', 'COSTO_IVI_PTE__7031', 'COSTO_IVF_PTE__7034',
                 'UTILIDAD_GRAVABLE__836']]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#REPETIR ESTE PROCESO PARA CADA ANO. SIN EMBARGO, DESDE EL PERIODO 2012 PARA ATRAS ES OTRO FORMATO, ENTONCES SE VUELVEN
#A DECLARAR LAS VARIABLES CON LOS NUEVOS NOMBRES DE LAS CUENTAS, PORQUE SÍ, LES GUSTA CAMBIARLE EL NOMBRE A LAS CUENTAS
#CADA CIERTO TIEMPO 

#ESTOS NOMBRES DE LAS CUENTAS SIRVEN PARA LOS AÑOS:  2013,2012
#small
income_pequenas13 = (df['VENTA_DE_BIENES_4101'] < 1000000 ) & (df['CIIU'].str.contains('C10'))


pequenas = df.loc [income_pequenas13,['NOMBRE','CIIU', 'ACTIVO_CORRIENTE_101', 'DOCUMENTOS_Y_CUENT_1010205' , 'DOCUMENTOS_Y_CUENT_1010206',
                            'INVENTARIOS_10103', 'ACTIVO_1', 'CUENTAS_Y_DOCUMENT_20103', 'PASIVO_2', 'CAPITAL_301', 'PATRIMONIO_NETO_3', 
                            'INGRESOS_DE_ACTIVI_41', 'COSTO_DE_VENTAS_Y__51', 'GANANCIA_PERDIDA_62']]

#big
income_grande13 = (df['VENTA_DE_BIENES_4101'] > 5000000 ) & (df['CIIU'].str.contains('C10'))


grande = df.loc [income_grande13,['NOMBRE','CIIU', 'ACTIVO_CORRIENTE_101', 'DOCUMENTOS_Y_CUENT_1010205' , 'DOCUMENTOS_Y_CUENT_1010206',
                            'INVENTARIOS_10103', 'ACTIVO_1', 'CUENTAS_Y_DOCUMENT_20103', 'PASIVO_2', 'CAPITAL_301', 'PATRIMONIO_NETO_3', 
                            'INGRESOS_DE_ACTIVI_41', 'COSTO_DE_VENTAS_Y__51', 'GANANCIA_PERDIDA_62']]
#medium

income_mediana13 = (df['VENTA_DE_BIENES_4101'] > 1000000) & (df['CIIU'].str.contains('C10') &
(df['VENTA_DE_BIENES_4101'] < 5000000))

mediana = df.loc [income_mediana13,['NOMBRE','CIIU', 'ACTIVO_CORRIENTE_101', 'DOCUMENTOS_Y_CUENT_1010205' , 'DOCUMENTOS_Y_CUENT_1010206',
                            'INVENTARIOS_10103', 'ACTIVO_1', 'CUENTAS_Y_DOCUMENT_20103', 'PASIVO_2', 'CAPITAL_301', 'PATRIMONIO_NETO_3', 
                            'INGRESOS_DE_ACTIVI_41', 'COSTO_DE_VENTAS_Y__51', 'GANANCIA_PERDIDA_62']]


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#pequena
income_pequenas11 = (df['TOTAL_INGRESOS_699'] < 1000000 ) & (df['CIIU'].str.contains('C10'))
#grane
income_grande13 = (df['TOTAL_INGRESOS_699'] > 5000000 ) & (df['CIIU'].str.contains('C10'))
#mediana
income_mediana13 = (df['TOTAL_INGRESOS_699'] > 1000000) & (df['CIIU'].str.contains('C10') &
(df['TOTAL_INGRESOS_699'] < 5000000))

pequenas_1 = df.loc [income_pequenas11, ['NOMBRE','CIIU', 'TOTAL_INGRESOS_699','TOTAL_ACTIVO_CORRIENTE_339', 'CUENTAS_Y_DOCUMENTOS_POR__313', 
       'CUENTAS_Y_DOCUMENTOS_POR__314','CUENTAS_Y_DOCUMENTOS_POR__315', 'CUENTAS_Y_DOCUMENTOS_POR__316',
        'INVENTARIO_DE_MATERIA_PRI_325' , 'INVENTARIO_DE_PRODUCTOS_E_326'  ,'MERCADERIAS_EN_TRANSITO_329', 'TOTAL_DEL_ACTIVO_399',
        'CUENTAS_Y_DOCUMENTOS_POR__411', 'CUENTAS_Y_DOCUMENTOS_POR__412','CUENTAS_Y_DOCUMENTOS_POR__413', 'CUENTAS_Y_DOCUMENTOS_POR__414',
        'TOTAL_DEL_PASIVO_499', 'CAPITAL_SUSCRITO_Y_O_ASIG_501', 'TOTAL_PATRIMONIO_NETO_598', 
        'VENTAS_NETAS_LOCALES_GRAV_601','VENTAS_NETAS_LOCALES_GRAV_602','EXPORTACIONES_NETAS_603', 'TOTAL_COSTOS_797',
        'GANANCIA_PERDIDA_ANTES_DE_815']]
        
#PARECEN QUE TIENEN LOS MISMOS NOMBRES, PERO NO ALGUNAS TIENEN ESPACIOS O CAMBIAN EN UN NUMERO 

pequenas_2 = [income_pequenas11,['NOMBRE','CIIU', 'ACTIVO_CORRIENTE_101', 'DOCUMENTOS_Y_CUENTA_1010205',  'DOCUMENTOS_Y_CUENTA_1010206',
                            'INVENTARIOS_10103', 'ACTIVO_1', 'CUENTAS_Y_DOCUMENTO_20103', 'PASIVO_2', 'CAPITAL_301', 'PATRIMONIO_NETO_3', 
                            'INGRESOS_DE_ACTIVID_41', 'COSTO_DE_VENTAS_Y_P_51', 'GANANCIA_PERDIDA_AN_62']]

pequenas_3 = [income_pequenas11, ['NOMBRE','CIIU', 'ACTIVO_CORRIENTE_101', 'DOCUMENTOS_Y_CUENT_1010206',  'DOCUMENTOS_Y_CUENT_1010206',
                            'INVENTARIOS_10103', 'ACTIVO_1', 'CUENTAS_Y_DOCUMENT_20103', 'PASIVO_2', 'CAPITAL_301', 'PATRIMONIO_NETO_3', 
                            'INGRESOS_DE_ACTIVI_41', 'COSTO_DE_VENTAS_Y__51', 'GANANCIA_PERDIDA_62']]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#CUENTAS PARA AÑO 2009, 2008 

df.loc [income_pequenas09, ['NOMBRE','CIIU', 'TOTAL_INGRESOS_699','TOTAL_ACTIVO_CORRIENTE_339', 'CUENTAS_Y_DOCUMENTOS_POR_313', 
       'CUENTAS_Y_DOCUMENTOS_POR_314','CUENTAS_Y_DOCUMENTOS_POR_315', 'CUENTAS_Y_DOCUMENTOS_POR_316',
        'INVENTARIO_DE_MATERIA_PRI_325' , 'INVENTARIO_DE_PRODUCTOS_E_326'  ,'MERCADERIAS_EN_TRANSITO_329', 'TOTAL_DEL_ACTIVO_399',
        'CUENTAS_Y_DOCUMENTOS_POR_411', 'CUENTAS_Y_DOCUMENTOS_POR_412','CUENTAS_Y_DOCUMENTOS_POR_413', 'CUENTAS_Y_DOCUMENTOS_POR_414',
        'TOTAL_DEL_PASIVO_499', 'CAPITAL_SUSCRITO_Y_O_ASIG_501', 'TOTAL_PATRIMONIO_NETO_598', 
        'VENTAS_NETAS_LOCALES_GRAV_601','VENTAS_NETAS_LOCALES_GRAV_602','EXPORTACIONES_NETAS_603', 'TOTAL_COSTOS_797',
        'UTILIDAD_GRAVABLE_829']]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CUENTAS PARA EL AÑO 2007
df.loc[income_pequenas07, ['CIIU','NOMBRE','CIIU', 'TOTAL_INGRESOS_699','TOTAL_ACTIVO_CORRIENTE_339', 'CTAS_Y_DOCS_POR_COBRAR_CL_315', 
       'CTAS_Y_DOC_POR_COBRAR_CLI_319','OTRAS_CUENTAS_POR_COBRAR_321',
        'INVENTARIO_DE_MATERIA_PRI_326' , 'INVENTARIO_DE_PRODUCTOS_E_327'  ,'INVENTARIO_DE_SUMINISTROS_328','INVENTARIO_DE_PROD_TERM_Y_329', 'MERCADERIAS_EN_TRANSITO_330', 'INVENTARIO_REPUESTOS_HERR_331', 'TOTAL_DEL_ACTIVO_399',
        'CTAS_Y_DOCMTOS_POR_PAGAR__411', 'CTAS_Y_DOCMTOS_POR_PAGAR__413', 
        'TOTAL_DEL_PASIVO_499', 'CAPITAL_SUSCRITO_ASIGNADO_501', 'TOTAL_PATRIMONIO_NETO_598', 
        'VENTAS_NETAS_LOCALES_GRAV_601','VENTAS_NETAS_LOCALES_GRAV_602','EXPORTACIONES_NETAS_603', 'INV_INICIAL_D_BIENES_NO_P_711' , 'COMPRAS_NETAS_LOCD_BIENES_712' , 'IMPORTACIONES_DE_BIENES_N_713' , 'INVFINAL_BIENES_NO_PRODUC_714' , 'INVENTARIO_INICIAL_DE_MAT_715' , 'COMPRAS_NETAS_LOCALES_DE__716' , 'IMPORTACIONES_DE_MATERIA__717'  ,'INVENTARIO_FINAL_DE_MATER_718'    ,'INVENTARIO_INICIAL_DE_PRO_719'    ,'INVENTARIO_FINAL_DE_PRODU_720'    , 'INVENTARIO_INICIAL_DE_PRO_721'   , 'INVENTARIO_FINAL_DE_PRODU_722'    ,'BAJA_DE_INVENTARIOS_723',
        'UTILIDAD_GRAVABLE_814']]

        