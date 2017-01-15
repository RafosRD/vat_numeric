from openerp import models, fields, api,exceptions

class vat_numeric_res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _defaults = {'country_id': lambda self, cr, uid, context:self.pool.get('res.country').browse(cr, uid, self.pool.get('res.country').search(cr, uid, [('code', '=', 'DO')]))[0].id, }

    @api.one
    @api.constrains('vat','company_type')
    def vat_is_numeric(self):
        if self.country_id.code == 'DO':
            if self.vat.isdigit() == False:
                raise exceptions.ValidationError('Solo puede colocar numeros en el campo RNC/Cedula')





