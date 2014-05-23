##############################################################################
#
#    Semantics, module for Odoo, Open Source Management Solution
#    Copyright (C) 2014 InsPyration EURL (<http://www.inspyration.fr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Semantics',
    'version' : '1.0',
    'author' : 'Alicia FLOREZ & Sébastien CHAZALLET',
    'category': '',
    'summary': '',
    'description' : """
    """,
    'website': 'http://www.inspyration.fr',
    'images' : [],
    'depends' : ['base'],
    'data': [
        'views/semantics_view.xml',
        'data/semantics_data.xml',
    ],
    'js': [
    ],
    'qweb' : [
    ],
    'css':[
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}