# -*- coding: utf-8 -*-

from openerp import fields, models


class hrEmployeeFormationModule(models.Model):

    _inherit = 'hr.employee.formation.module'

    branche_id = fields.Many2one('hr.employee.branche', string='Branche')
    specialite = fields.Char(string=u'Spécialité')
    specificite_ids = fields.One2many('hr.employee.module.specificite','module_id', string=u'Spécificité')
    active = fields.Boolean(string='Actif',default=True)
