# -*- coding: utf-8 -*-
# from procesar_csv import ProcesarCsv
from csv_creacion.procesar_csv_dict import ProcesarCsv

# if __name__ =="__main__":
# 	obj = ProcesarCsv()
# 	obj.escribir_datos_product()

if __name__ =="__main__":
	obj = ProcesarCsv()
	obj.escribir_datos_category()
	obj.escribir_datos_template()
	obj.escribir_datos_product()


