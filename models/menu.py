# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('Shop'), False, URL('default', 'shop'), []),
        (T('My Account'), False, URL('default', 'my_account'), []),
        (T('Register'), False, '#', [
            (T('Representative'), False, URL('default', 'register_representative')),
            (T('Distributor'), False, URL('default', 'register_distributor')),
            (T('Installer'), False, URL('default', 'register_installer')),
            (T('Developer'), False, URL('default', 'register_developer')),
        ]),
    ] 
