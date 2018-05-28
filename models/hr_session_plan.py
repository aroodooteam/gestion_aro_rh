# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _


class HrSessionPlan(models.Model):
    _name = 'hr.session.plan'

    plan_formation_id = fields.Many2one('hr.plan.formation', string=u'Année')
    objectif_id = fields.Many2one('hr.formation.objectif',string='Objectif')
    branche_id = fields.Many2one('hr.employee.branche',string='Branche')
    module_id= fields.Many2one('hr.employee.formation.module',string='Module')
    specificite_id = fields.Many2one('hr.employee.module.specificite',string=u'Spécificité')
    date_session = fields.Date(string=u'Date Début')
    session_place = fields.Char(string='Lieu')
    instructor_id = fields.Many2one('hr.formation.instructor',string='Animateur')
    session_plan_ids = fields.Many2many('hr.plan.formation',string='Session')
    attendee_ids = fields.Many2many('hr.employee',string='Attendee')
    plan_formation_objectif_id = fields.Char(related='plan_formation_id.objectif_id.name', readonly=True, string='Objectif')
    plan_formation_branche_id = fields.Char(related='plan_formation_id.branche_id.name', readonly=True,string='Branche')
    #plan_formation_module_id = fields.Char(related='plan_formation_id.module_id.name', readonly=True,string='Module',store=True)
    plan_formation_module_id = fields.Many2one(related='plan_formation_id.module_id', readonly=True,string='Module',store=True)
    #plan_formation_id_beneficiaire= fields.Integer(string='Beneficiaire',related='plan_formation_id.module_id.id')
    date_fin_session = fields.Date(string='Date Fin')
    cout_session = fields.Float(string=u'Coût',digits=(10, 2))
    observations = fields.Text(string='Observations')
    duree_session = fields.Float(string=u'Durée en heure',digits=(6,2))
    active = fields.Boolean(string='Actif', default=True)
    session_external_attendee_ids = fields.One2many('hr.session.plan.attendee','session_plan_id',string='Externe')

    _order = "date_session asc"

    @api.constrains('date_session','date_fin_session')
    def check_date_session(self):
        for session in self:
            if session.date_session > session.date_fin_session:
                raise exceptions.ValidationError(u"Les dates de votre session ne sont pas cohérentes, merci de vérifier")

class HrSessionPlanAttendee(models.Model):
    _name = 'hr.session.plan.attendee'
    _description = 'Liste des participants appartenant aux agences generales'

    #name = fields.Char(string='Nom participant',size=64)
    external_attendee_id = fields.Many2one('hr.external.attendee', string='Nom participant')
    agency_name = fields.Char(string='Agence',size=50,related="external_attendee_id.agency")
    session_plan_id = fields.Many2one('hr.session.plan',string='Session de formation')

class HrExternalAttendee(models.Model):
    _name = 'hr.external.attendee'
    _description = 'Agents generaux'

    name = fields.Char(string='Nom',size=64)
    agency = fields.Char(string='Agence',size=50)


