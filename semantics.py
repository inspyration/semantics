# -*- coding: utf-8 -*-
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

__author__ = "Sébastien CHAZALLET & Alicia FLOREZ"
__copyright__ = "Copyright 2014"
__credits__ = ["Sébastien CHAZALLET", "Alicia FLOREZ", "www.insPyration.fr", "www.formation-python.com"]
__license__ = "AGPL"
__version__ = "1.0"
__maintainer__ = "Alicia FLOREZ"
__email__ = "contact@inspyration.fr"
__status__ = "Production"

import openerp
from openerp.osv import fields, osv


#==============================================================================#
#                                class Field                                   #
#==============================================================================#
class Field(osv.Model):
    
    _name = 'semantics.field'
    _description = "Field"
    
    def _get_signifier_items(self, cr, uid, ids, field, arg, context=None):
        result = {}
        for field in self.browse(cr, uid, ids, context=context):
            res = []
            for signifier in field.signifier_ids:
                res.append({'id': signifier.id, 'name': signifier.name})
            result[field.id] = res
        return result
    
    
    
    _columns = {
        'name': fields.char(
            'Name',
            size=256,
            required=True,
            select=True,
            unique=True,
        ),
        'signifier_ids': fields.one2many(
            'semantics.signifier',
            'field_id',
            string="Signifiers"
        ),
        'signifier_items': fields.function(
            _get_signifier_items,
            type="text",
            string="Signifier Items",
        ),
        'active': fields.boolean(
            string="Active",
        ),
    }

    _defaults = {
        'active': True,
    } 




#==============================================================================#
#                            class Signifier                                   #
#==============================================================================#
class Signifier(osv.Model):
    
    _name = 'semantics.signifier'
    _description = "Signifier"
    
    _columns = {
        'name': fields.char(
            'Name',
            size=256,
            required=True,
            select=True,
            unique=True,
        ),
        'field_id': fields.many2one(
            'semantics.field',
            string="Field"
        ),
        'active': fields.boolean(
            string="Active",
        ),
    }

    _defaults = {
        'active': True,
    } 







