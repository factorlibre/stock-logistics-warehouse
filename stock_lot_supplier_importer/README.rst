.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============================
Stock Lot Importer by Supplier
==============================

This module allows to import Serial Number (lots) by the product_code
(SKU - Stock-Keeping Unit) from a xls file.

The purpose is to have the lots created before processing the picking in. The
supplier give us a list of serial number associated with a sku number before
send the products. So we have not to read the serial numbers of each product
when they come.

The program will search the file sku columns on 'Product Code' field
from product info.

Usage
=====

To use this module, you need to:

* Create a xls file with, at least, the columns 'sku_no' and 'serial_no' (no
  matter whether it is case sensitive).
* Go to Warehouse > Traceability > Lots Supplier Importer
* Will display a popup. Then enter the xls file created previously and click on
  'Import' button.

If any error occurs while importing, the program will show a list of explained
errors in the same popup.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/153/8.0


Known issues / Roadmap
======================

* May be useful to allow csv files.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/stock-logistics-warehouse/issues>`_. In case of
trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/OCA/
stock-logistics-warehouse/issues/new?body=module:%20
stock_lot_supplier_importer%0Aversion:%20
8.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Ismael Calvo <ismael.calvo@factorlibre.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.