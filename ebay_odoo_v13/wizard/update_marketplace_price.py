from odoo import models, fields, api, _
import logging

logger = logging.getLogger(__name__)


class update_marketplace_price(models.TransientModel):
    _name = 'update.marketplace.price'
    _inherit = 'update.marketplace.price'

    # on_ebay = fields.Boolean(string='On Ebay')
    # ebay_shop_id = fields.Many2one('sale.shop', string='Shop Name',domain=[('ebay_shop','=',True)])

    def update_price(self):

        (data,) = self

        # if data.on_ebay:
        if data.shop_id.instance_id.module_id == 'ebay_odoo_v13':
            context = self._context.copy()
            product_obj = self.env['product.product']
            pobj = product_obj.browse(context.get('active_id'))
            l_ids = [p.id for p in pobj.prodlisting_ids if p.active_ebay]
            context.update({'eactive_ids': l_ids, 'update_price': True})
            data.shop_id.with_context(context).export_stock_and_price()
        super(update_marketplace_price, self).update_price()
        return True

    #
    def update_stock(self):

        (data,) = self

        if data.shop_id.instance_id.module_id == 'ebay_odoo_v13':
            context = self._context.copy()
            product_obj = self.env['product.product']
            pobj = product_obj.browse(context.get('active_id'))
            l_ids = [p.id for p in pobj.prodlisting_ids if p.active_ebay]
            context.update({'eactive_ids': l_ids, 'update_stock': True})
            data.shop_id.with_context(context).export_stock_and_price()
        super(update_marketplace_price, self).update_stock()
        return True

    def update_stock_price(self):

        (data,) = self
        if data.shop_id.instance_id.module_id == 'ebay_odoo_v13':
            context = self._context.copy()
            product_obj = self.env['product.product']
            pobj = product_obj.browse(context.get('active_id'))
            l_ids = [p.id for p in pobj.prodlisting_ids if p.active_ebay]
            context.update({'eactive_ids': l_ids, 'update_stock': True, 'update_price': True})
            data.shop_id.with_context(context).export_stock_and_price()
        return True


update_marketplace_price()
