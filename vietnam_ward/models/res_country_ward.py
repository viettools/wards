from odoo import api, fields, models, _

class CountryWard(models.Model):
    _name = 'res.country.ward'
    _description = 'Vietnam Wards'
    
    name = fields.Char(string='Name', required=True, index='trigram', tracking=True)
    code = fields.Char(string='Code')
    state_id = fields.Many2one('res.country.state', string='State', required=True)
    active = fields.Boolean(default=True)