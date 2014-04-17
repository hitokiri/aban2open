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

		aban = self.datos_csv(self.datos_csv_aban, 'r')
		product = self.datos_csv(self.datos_prodct_product, 'r')
		with open('db_files/product_product1.csv', 'wb') as nuevo:
		 	for master, plantilla in zip(aban, product):
		 		nuevo_product = csv.writer(nuevo,quotechar='"', quoting=csv.QUOTE_ALL)
		 		nuevo_product.writerow(plantilla.keys() )
		 		valores_plantilla = plantilla.values()
		 		for valor_master in  aban:
		 			valores = valor_master.values()
		 			valores_plantilla[7] = valores[2]
		 			nuevo_product.writerow(valores_plantilla)
		 		break
	def escribir_datos_template():
		pass


