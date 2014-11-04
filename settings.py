# -*- coding: utf-8 -*-
import os


#carpeta donde se guardan los archivos master y salidas de creacion
CARPETA_FILE = os.path.join(os.path.dirname(__file__), 'db_files/')#archivo productos de abanq

#configuracion de los archivos para leer y crear con el proceso csv_dict
ABANQ = CARPETA_FILE + 'articulos.csv'#archivo base de openerp
PRODUCT_PRODUCT = CARPETA_FILE + 'product_product.csv'#archivo base de openerp
PRODUCT_TEMPLATE = CARPETA_FILE + 'product_template.csv'#archivo base de openerp
PRODUCT_CATEGORY = CARPETA_FILE + 'product_category.csv'#archivo base de openerp
PRODUCT_CATEGORY1 = CARPETA_FILE + 'product_category1.csv'#archivo base de openerp

INPORTFILES_ABANQ = ['articulos',]
INPORTFILES_OPENERP = ['product_category', 'product_template', 'product_product',]

DATABASES = {
	'abanq': {
	'ENGINE':'', #mysql or postgresql_psycopg2
        'NAME': '',#name for Database
        'USER': '', #user form Database
        'PASSWORD': '', #password fron database
        'HOST': '', #host from you server
        'PORT': '',#postgres 5432 mysql 3306
        'TABLAS': INPORTFILES_ABANQ,
	},
	'postgres': {
		'ENGINE':'', #mysql or postgresql_psycopg2
        'NAME': '',#name for Database
        'USER': '', #user form Database
        'PASSWORD': '', #password fron database
        'HOST': '', #host from you server
        'PORT': '',#postgres 5432 mysql 3306
        'TABLAS': INPORTFILES_OPENERP,
	},
}
