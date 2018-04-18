# -*- coding: utf-8 -*-

from openerp import api,  exceptions,  fields,  models,  _


class HrPlanFormation(models.Model):
    _name = 'hr.plan.formation'

    name = fields.Char(string=u'Libellé')
    objectif_id = fields.Many2one('hr.formation.objectif', string='Objectif', required=True)
    branche_id = fields.Many2one('hr.employee.branche', string='Branche', required=True)
    module_id = fields.Many2one('hr.employee.formation.module', string='Module', required=True)
    date_start = fields.Date(string=u'Prévision début')
    date_end= fields.Date(string=u'Prévision fin')
    intervenant = fields.Char(string='Intervenant')
    total_besoin = fields.Integer(string=u'Besoin exprimé')
    budget_euro = fields.Float(string='Budget en Euros', digits=(6, 2))
    budget_ariary = fields.Float(string='Budget en Ariary', digits=(6, 2))
    besoin_accorde = fields.Integer(string=u'Besoin accordé')
    beneficiaire = fields.Integer(string=u'Bénéficiaire')
    taken_seats=fields.Float( string='Taux', digits=(4, 2), compute="_taken_seats_2")
    cout = fields.Float(string=u'Coût engagé', digits=(6, 2),compute='get_total_cost')
    test_besoin = fields.Char(string='Besoin Test')
    session_plan_ids = fields.One2many('hr.session.plan', 'plan_formation_id', string='session')
    observations = fields.Text(string='Observations')
    code_plan = fields.Char(string='Code plan')
    active = fields.Boolean(string='Actif', default=True)

    _order = "name asc"

    # compute field
    @api.depends ('beneficiaire', 'besoin_accorde')
    def _taken_seats_2(self):
        for r in self:
            if not r.besoin_accorde:
                r.taken_seats=0.0
            else:
                r.taken_seats=100 * r.beneficiaire/r.besoin_accorde

    @api.multi
    def name_get(self):
        result = super(HrPlanFormation,self).name_get()
        res = []
        print("result = %s" % result)
        for rec in result:
            # rec = (rec.id,  r_name)
            el_obj = self.browse(rec[0])
            r_name = rec[1] + ' '+ '[' + el_obj.objectif_id.name + '] ' +' ' + '[' + el_obj.branche_id.name + '] '+''+'[' + el_obj.module_id.name + ']'
            res.append((el_obj.id,  r_name))
        return res

    @api.multi
    def get_total_cost(self):
        for cost in self:
            session_plan=len(cost.session_plan_ids)
            count=0
            i=0
            while i < session_plan:
                for session_cost in  cost.session_plan_ids:
                    count=count+session_cost.cout_session
                    i=i+1
                    cost.cout=count
    
    @api.constrains('date_start','date_end')
    def check_date_plan(self):
        for plan in self:
            if plan.date_start > plan.date_end:
                raise exceptions.ValidationError(u"Les dates de vos prévisions ne sont pas cohérentes, merci de vérifier")
