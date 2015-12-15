# -*- coding: utf-8 -*-
# © 2015 FactorLibre - Ismael Calvo <ismael.calvo@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Stock Lot Importer by Supplier",
    "summary": "Import Lots from xls by product's SKU or name.",
    "version": "8.0.1.0.0",
    "category": "Warehouse Management",
    "website": "https://factorlibre.com/",
    "author": "FactorLibre, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": ["xlrd"],
    },
    "depends": [
        "stock",
        "product",
    ],
    "data": [
        "wizards/stock_lot_supplier_importer_view.xml",
    ],
    "demo": [],
    "qweb": []
}
