from openerp import models, fields, api,exceptions

class vat_numeric_res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _defaults = {'country_id': lambda self, cr, uid, context:self.pool.get('res.country').browse(cr, uid, self.pool.get('res.country').search(cr, uid, [('code', '=', 'DO')]))[0].id, }

    @api.model
    def create(self,vals):
        #raise exceptions.ValidationError(vals['country_id'])
        if self.env['res.country'].browse(vals['country_id']).code == 'DO':
            if vals['vat'].isdigit() == False:
                raise exceptions.ValidationError('Solo puede colocar numeros en el campo RNC/Cedula')

        return super(vat_numeric_res_partner, self).create(vals)

    def update(self, vals):

        if self.env['res.country'].browse(vals['country_id']).code == 'DO':
            if vals['vat'].isdigit() == False:
                raise exceptions.ValidationError('Solo puede colocar numeros en el campo RNC/Cedula')


        super(vat_numeric_res_partner, self).update(vals)





