# -*- coding: utf-8 -*-
import csv


class ProcesarCsv(object):
	"""docstring for ProcesarCsv"""
	def __init__(self):
		self.datos_csv_aban = 'db_files/db-colum.csv'
		self.datos_prodct_product = 'db_files/product_product.csv'
		self.datos_product_template = 'db_files/product_template.csv'
		self.datos_product_category = 'db_files/product_category1.csv'

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

	def escribir_datos_template(self):
		count = 4
		aban = self.datos_csv(self.datos_csv_aban, 'r')
		product = self.datos_csv(self.datos_product_template, 'r')
		product_category = self.datos_csv(self.datos_product_category, 'r')
		nombre_orden = product.fieldnames
		orden_aban = aban.fieldnames
		with open('db_files/product_template1.csv', 'wb') as nuevo:
		 	for master, plantilla in zip(aban, product):
		 		nuevo_product = csv.DictWriter(nuevo,quotechar='"', quoting=csv.QUOTE_ALL, fieldnames = nombre_orden)
		 		nuevo_product.writerow(dict((_, _) for _ in nombre_orden))
		 		valores_plantilla = plantilla
		 		for valor_master in  aban:
		 			valores_plantilla.update({'id':'%s' % count})
		 			valores_plantilla.update({'list_price':'%s' % valor_master['pvp']})
		 			valores_plantilla.update({'name':'%s' % valor_master['referencia']})
		 			for category in product_category:
		 				if valor_master['codfamilia'] == category['name']:
		 					valores_plantilla.update({'categ_id':'%s' % category['id']})
		 			nuevo_product.writerow(valores_plantilla)
		 			product_category = self.datos_csv(self.datos_product_category, 'r')
		 			count += 1
		 		break

	def escribir_datos_category(self):
		count = 3
		aban = self.datos_csv(self.datos_csv_aban, 'r')
		product = self.datos_csv(self.datos_product_category, 'r')
		nombre_orden = product.fieldnames
		orden_aban = aban.fieldnamesvalores_plantilla.update({'id':'%s' % count})
		familias = [_['codfamilia'] for _ in aban]
		familias_category = set(familias)
		with open('db_files/product_category1.csv', 'wb') as nuevo:
		 	for plantilla in product:
		 		nuevo_product = csv.DictWriter(nuevo,quotechar='"', quoting=csv.QUOTE_ALL, fieldnames = nombre_orden)
		 		nuevo_product.writerow(dict((_, _) for _ in nombre_orden))
		 		valores_plantilla = plantilla
		 		for valor_master in  familias_category:
		 			if valor_master:
			 			valores_plantilla.update({'id':'%s' % count})
			 			valores_plantilla.update({'name':'%s' % valor_master})
			 			nuevo_product.writerow(valores_plantilla)
			 			count += 1
		 		break


