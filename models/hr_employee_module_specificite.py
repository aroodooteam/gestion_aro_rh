# -*- coding: utf-8 -*-

from openerp import fields, models

class HrEmployeeModuleSpecificite(models.Model):
    _name = 'hr.employee.module.specificite'
    _description = u'Spécificité du module'

    module_id = fields.Many2one('hr.employee.formation.module', string='Module')
    name = fields.Char(string=u'Spécificité',size=64)