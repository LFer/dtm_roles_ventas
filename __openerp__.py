# -*- encoding: utf-8 -*-
##########################################################################
#    Copyright (C) OpenERP Uruguay (<http://openerp.com.uy>).
#    All Rights Reserved
# Credits######################################################
#    Coded by: Felipe Ferreira
#    Planified by: Felipe Ferreira
#    Finance by: Datamatic S.A. - www.datamatic.com.uy
#
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
{
    'name': 'Roles de Ventas',
    'version': '1.0',
    'website' : 'www.datamatic.com.uy',
    'category': 'Seguridad',
    'summary': 'Crea Roles especiales para la aplicaion de ventas',
    'description': """
Este modulo crea roles de seguridad personalizados
==================================================

Este modulo permite establecer de manera eficiente roles de usabilidad


Caracteristicas Principales
---------------------------
* Rol Vendedor Externo
* Rol Vendedor Interno
""",
    'author': 'Felipe Ferreira',
    'depends': ['base'],
    'data': [
        'security/dtm_roles_ventas.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
