##############################################################################
#
#    Copyright (C) 2022  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    "name": "stephanie16",
    "version": "16.0.1.0.0",
    "category": "Tools",
    "summary": "Test for v16 CE",
    "author": "SDH",
    "website": "http://github.com/sistemasdehudson/cl-stephanie16",
    "license": "AGPL-3",
    "depends": [],
    "installable": True,
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "CE",
    # Config to write in odoo.conf
    "config": [
        "workers = 0",
        "admin_password = admin",
    ],
    "port": "8069",
    "git-repos": [
        "https://github.com/sistemasdehudson/cl-stephanie16.git",
        #'git@github.com:jobiols/odoo-jeo-ce.git',
        'https://github.com/regaby/odoo-custom.git -b 16.0',
        'https://github.com/sistemasdehudson/sdehposaddons.git -b 16.0',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git -b 16.0',
        'https://github.com/ingadhoc/odoo-argentina-ce.git -b 16.0',
        'https://github.com/ingadhoc/argentina-sale.git -b 16.0',
        'https://github.com/ingadhoc/account-payment.git -b 16.0',
        'https://github.com/ingadhoc/account-invoicing.git -b 16.0',
        'https://github.com/ingadhoc/account-financial-tools.git -b 16.0',
        'https://github.com/ingadhoc/sale.git -b 16.0',
        'https://github.com/ingadhoc/stock.git -b 16.0',
        'https://github.com/ingadhoc/aeroo_reports.git -b 16.0',
        'https://github.com/ingadhoc/website.git -b 16.0',
        'https://github.com/OCA/account-financial-reporting.git -b 16.0',
        'https://github.com/OCA/reporting-engine.git -b 16.0',
        'https://github.com/OCA/server-ux.git -b 16.0',
        'https://github.com/OCA/mis-builder.git -b 16.0',
        'https://github.com/OCA/sale-workflow.git -b 16.0',
        'https://github.com/OCA/web.git -b 16.0',
        ##
        'https://github.com/OCA/contract.git -b 16.0',
        'https://github.com/odoomates/odooapps.git -b 16.0',
        'https://github.com/OCA/manufacture.git -b 16.0',
        'https://github.com/OCA/manufacture-reporting.git -b 16.0',
        'https://github.com/OCA/helpdesk -b 16.0',
        'https://github.com/OCA/bank-statement-import -b 16.0',
        'https://github.com/OCA/pos.git -b 16.0',
        'https://github.com/OCA/report-print-send.git -b 16.0',
        'https://github.com/OCA/project -b 16.0',
        'https://github.com/ingadhoc/purchase -b 16.0',
        'https://github.com/ingadhoc/product -b 16.0',
        'https://github.com/ingadhoc/website -b 16.0',
        'https://github.com/OCA/project-reporting -b 16.0',
        'https://github.com/OCA/purchase-workflow -b 16.0',
        'https://github.com/Yenthe666/auto_backup.git yenthe666/auto_backup -b 16.0',
        'https://github.com/OCA/e-commerce -b 16.0',
        'https://github.com/OCA/brand -b 16.0',
        'https://github.com/OCA/stock-logistics-workflow -b 16.0',
        'https://github.com/OCA/stock-logistics-workflow -b 16.0',
        'https://github.com/regaby/mercadopago -b 16.0',
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-jeo:16.0",
        "postgres postgres:15.1-alpine",
    ],
}
