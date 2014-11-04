# -*- coding: utf-8 -*-
import os
import csv
from settings import *

class ProcesarCsv(object):
	"""docstring for ProcesarCsv"""
	def __init__(self):
		self.datos_csv_aban = ABANQ #archivo productos de abanq
		self.datos_prodct_product = PRODUCT_PRODUCT#archivo base de openerp
		self.datos_product_template = PRODUCT_TEMPLATE#archivo base de openerp
		self.datos_product_category = PRODUCT_CATEGORY#archivo base de openerp
		self.datos_product_category1 = PRODUCT_CATEGORY1 #archivo base de openerp


	def datos_csv(self, nombre, modo):
		datos_csv=open(nombre, modo)
		datos = csv.DictReader(datos_csv, delimiter=',', quotechar='"', escapechar='\\')

		return datos

	def escribir_datos_product(self):
		count = 4
		aban = self.datos_csv(self.datos_csv_aban, 'r')
		product = self.datos_csv(self.datos_prodct_product, 'r')
		nombre_orden = product.fieldnames
		with open(CARPETA_FILE + 'product_product1.csv', 'wb') as nuevo:
		 	for plantilla in product:
		 		#nuevo_product = csv.DictWriter(nuevo,quotechar='"', quoting=csv.QUOTE_ALL, fieldnames = nombre_orden)
		 		nuevo_product = csv.DictWriter(nuevo, fieldnames = nombre_orden)
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
		product_category = self.datos_csv(self.datos_product_category1, 'r')
		nombre_orden = product.fieldnames
		temporal_category = dict((_['name'], _['id']) for _ in product_category)
		with open(CARPETA_FILE + 'product_template1.csv', 'wb') as nuevo:
		 	for plantilla in product:
		 		nuevo_product = csv.DictWriter(nuevo, fieldnames = nombre_orden)
		 		nuevo_product.writerow(dict((_, _) for _ in nombre_orden))
		 		valores_plantilla = plantilla
		 		for valor_master in  aban:
		 			valores_plantilla.update({'id':'%s' % count})
		 			valores_plantilla.update({'list_price':'%s' % valor_master['pvp']})
		 			valores_plantilla.update({'name':'%s' % valor_master['referencia']})
		 			valores_plantilla.update({'description':'%s' % valor_master['descripcion']})
	 				if valor_master['codfamilia'] in  temporal_category:
	 					valores_plantilla.update({'categ_id':'%s' % temporal_category[valor_master['codfamilia']]})
		 			nuevo_product.writerow(valores_plantilla)
		 			count += 1
		 		break


	def escribir_datos_category(self):
		count = 3
		aban = self.datos_csv(self.datos_csv_aban, 'r')
		product = self.datos_csv(self.datos_product_category, 'r')
		nombre_orden = product.fieldnames
		familias = [_['codfamilia'] for _ in aban]
		familias_category = set(familias)
		with open(CARPETA_FILE + 'product_category1.csv', 'wb') as nuevo:
		 	for plantilla in product:
		 		nuevo_product = csv.DictWriter(nuevo, fieldnames = nombre_orden)
		 		nuevo_product.writerow(dict((_, _) for _ in nombre_orden))
		 		valores_plantilla = plantilla
		 		for valor_master in  familias_category:
		 			if valor_master:
			 			valores_plantilla.update({'id':'%s' % count})
			 			valores_plantilla.update({'name':'%s' % valor_master})
			 			nuevo_product.writerow(valores_plantilla)
			 			count += 1
		 		break


