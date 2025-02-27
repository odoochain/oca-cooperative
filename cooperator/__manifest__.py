# Copyright 2013-2018 Open Architects Consulting SPRL.
# Copyright 2018      Coop IT Easy SC (<http://www.coopiteasy.be>)
#   Houssine BAKKALI <houssine@coopiteasy.be>
#   Robin Keunen <robin@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Cooperators",
    "summary": "Manage your cooperators",
    "version": "14.0.2.0.1",
    "depends": [
        "account",
        "base_iban",
        "mail",
        "web",
        # todo split into cooperator_partner_firstname
        "partner_firstname",
        # todo split into cooperator partner_contact_birthdate
        "partner_contact_birthdate",
        # todo split into cooperator_partner_contact_gender
        "partner_contact_gender",
    ],
    "author": "Coop IT Easy SC, Odoo Community Association (OCA)",
    "category": "Cooperative management",
    "website": "https://github.com/OCA/cooperative",
    "license": "AGPL-3",
    "data": [
        "data/data.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/ir_rule.xml",
        "wizard/create_subscription_from_partner.xml",
        "wizard/validate_subscription_request.xml",
        "wizard/update_share_line.xml",
        "views/subscription_request_view.xml",
        "views/mail_template_view.xml",
        "views/res_partner_view.xml",
        "views/subscription_register_view.xml",
        "views/operation_request_view.xml",
        "views/account_move_views.xml",
        "views/product_view.xml",
        "views/res_company_view.xml",
        "views/account_journal_views.xml",
        "views/menus.xml",
        "report/reports.xml",
        "report/layout.xml",
        "report/cooperator_invoice_G002.xml",
        "report/cooperator_certificat_G001.xml",
        "report/cooperator_subscription_G001.xml",
        "report/cooperator_register_G001.xml",
        "data/mail_template_data.xml",  # Must be loaded after reports
    ],
    "demo": [
        "demo/coop.xml",
        "demo/users.xml",
    ],
    "application": True,
}
