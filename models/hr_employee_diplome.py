# -*- coding: utf-8 -*-

from openerp import fields, models


class hrEmployeeDiplome(models.Model):

    _name = 'hr.employee.diplome'

    employee_id = fields.Many2one('hr.employee', string=u'Employé')
    ordre = fields.Char(string='Ordre')
    annee = fields.Integer(string=u'Année')
    diplome_id = fields.Many2one(comodel_name='qual.type', string=u'Diplôme')
    niveau_id = fields.Many2one(comodel_name='hr.niveau.etudes', string='Niveau', related='diplome_id.niveau_id')
    #niveau = fields.Char(related='diplome_id.niveau_id.name',readonly=True,string='Niveau')
    branche_id = fields.Many2one('hr.employee.branche', string='Branche')
    specialite = fields.Char(string=u'Spécialité')
    lieu = fields.Char(string='Lieu')
