# -*- coding: utf-8 -*-
import csv


class ProcesarCsv(object):
	"""docstring for ProcesarCsv"""
	def __init__(self):
		self.datos_csv_aban = 'db_files/db-colum.csv'
		self.datos_prodct_product = 'db_files/product_product.csv'
		self.datos_product_template = 'db_files/product_template.csv'

	def datos_csv(self, nombre, modo):
		datos_csv=open(nombre, modo)
		datos = csv.DictReader(datos_csv)

		return datos

	def escribir_datos_product(self):
		count = 4
		aban = self.datos_csv(self.datos_csv_aban, 'r')
		product = self.datos_csv(self.datos_prodct_product, 'r')
		nombre_orden = product.fieldnames
		orden_aban = aban.fieldnames
		with open('db_files/product_product1.csv', 'wb') as nuevo:
		 	for master, plantilla in zip(aban, product):
		 		nuevo_product = csv.DictWriter(nuevo,quotechar='"', quoting=csv.QUOTE_ALL, fieldnames = nombre_orden)
		 		nuevo_product.writerow(dict((fn,fn) for fn in nombre_orden))
		 		valores_plantilla = plantilla
		 		for valor_master in  aban:
		 			valores_plantilla.update({'id':'%s' % count})
		 			valores_plantilla.update({'product_tmpl_id':'%s' % count})
		 			valores_plantilla.update({'name_template':'%s' % valor_master['referencia']})
		 			nuevo_product.writerow(valores_plantilla)
		 			count += 1
		 		break
	def escribir_datos_template():
		pass


