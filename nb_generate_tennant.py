#!/usr/bin/env python3

import argparse
import sys
from json import dumps


# noinspection SqlNoDataSourceInspection
def main(args):
    admin_group_id = args.admin_group_id
    view_group_id = args.view_group_id

    tenant_group_name = args.tenant_group_name
    wireless_lan_group_name = args.wireless_lan_group_name
    cluster_group_name = args.cluster_group_name
    contact_group_name = args.contact_group_name
    user_view_group_name = args.user_view_group_name
    user_admin_group_name = args.user_admin_group_name

    actions = ['add', 'change', 'delete', 'view']

    # TODO: get live from database
    ct = {
        'auth': {
            'group': {
                'actions': ['view'],
                'id': 2,
                'constraints': [{"name": user_view_group_name}, {"name": user_admin_group_name}],
            },
            'user': {
                'actions': ['view', 'add'],
                'id': 4,
                'constraints': [{"groups__name": user_view_group_name}, {"groups__name": user_admin_group_name}],
            },
        },

        'circuits': {
            'circuit': {
                'actions': actions,
                'id': 10,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'circuittermination': {
                'actions': actions,
                'id': 8,
                'constraints': {"circuit__tenant__group__name": tenant_group_name},
            },

            # only allow view for Tenant Admin
            'circuittype': {
                'actions': ['view'],
                'id': 7,
                'constraints': None,
            },
            'provider': {
                'actions': ['view'],
                'id': 9,
                'constraints': {"name": "Bauamt Erlangen"},
            },
            'provideraccount': {
                'actions': actions,
                'id': 137,
                'constraints': {"provider__name": "Bauamt Erlangen"},
            },
            'providernetwork': {
                'actions': actions,
                'id': 89,
                'constraints': {"provider__name": "Bauamt Erlangen"},
            },
        },

        'core': {
            'autosyncrecord': {
                'actions': ['view'],
                'id': 134,
                'constraints': None,
            },
            'datafile': {
                'actions': ['view'],
                'id': 133,
                'constraints': None,
            },
            'datasource': {
                'actions': ['view'],
                'id': 132,
                'constraints': None,
            },
            'job': {
                'actions': ['view'],
                'id': 136,
                'constraints': None,
            },
            'managedfile': {
                'actions': ['view'],
                'id': 135,
                'constraints': None,
            },
        },

        'dcim': {
            'cable': {
                'actions': actions,
                'id': 70,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'cablepath': {
                'actions': ['view'],
                'id': 90,
                'constraints': None,
            },
            'cabletermination': {
                'actions': actions,
                'id': 125,
                'constraints': {"cable__tenant__group__name": tenant_group_name},
            },
            'consoleport': {
                'actions': actions,
                'id': 28,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'consoleporttemplate': {
                'actions': ['view'],
                'id': 30,
                'constraints': None,
            },
            'consoleserverport': {
                'actions': actions,
                'id': 12,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'consoleserverporttemplate': {
                'actions': ['view'],
                'id': 23,
                'constraints': None,
            },

            'device': {
                'actions': ['add', 'change', 'delete', 'napalm_read', 'napalm_write', 'view'],
                'id': 13,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'devicebay': {
                'actions': actions,
                'id': 36,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'devicebaytemplate': {
                'actions': ['view'],
                'id': 17,
                'constraints': None,
            },
            'devicerole': {
                'actions': ['view'],
                'id': 22,
                'constraints': None,
            },
            'devicetype': {
                'actions': ['view'],
                'id': 15,
                'constraints': None,
            },
            'frontport': {
                'actions': actions,
                'id': 72,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'frontporttemplate': {
                'actions': ['view'],
                'id': 73,
                'constraints': None,
            },
            'interface': {
                'actions': ['view'],
                'id': 24,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'interfacetemplate': {
                'actions': ['view'],
                'id': 21,
                'constraints': None,
            },
            'inventoryitem': {
                'actions': ['view'],
                'id': 27,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'inventoryitemrole': {
                'actions': ['view'],
                'id': 120,
                'constraints': None,
            },
            'inventoryitemtemplate': {
                'actions': ['view'],
                'id': 121,
                'constraints': None,
            },
            'location': {
                'actions': actions,
                'id': 20,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'manufacturer': {
                'actions': ['view'],
                'id': 29,
                'constraints': None,
            },
            'module': {
                'actions': actions,
                'id': 118,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'modulebay': {
                'actions': ['view'],
                'id': 117,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'modulebaytemplate': {
                'actions': ['view'],
                'id': 119,
                'constraints': None,
            },
            'moduletype': {
                'actions': ['view'],
                'id': 116,
                'constraints': None,
            },
            'platform': {
                'actions': ['view'],
                'id': 18,
                'constraints': None,
            },

            'powerfeed': {
                'actions': actions,
                'id': 74,
                'constraints': {"power_panel__site__tenant__group__name": tenant_group_name},
            },
            'poweroutlet': {
                'actions': actions,
                'id': 14,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'poweroutlettemplate': {
                'actions': ['view'],
                'id': 25,
                'constraints': None,
            },
            'powerpanel': {
                'actions': actions,
                'id': 68,
                'constraints': {"site__tenant__group__name": tenant_group_name},
            },
            'powerport': {
                'actions': actions,
                'id': 34,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'powerporttemplate': {
                'actions': ['view'],
                'id': 31,
                'constraints': None,
            },

            'rack': {
                'actions': actions,
                'id': 32,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'rackreservation': {
                'actions': actions,
                'id': 26,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'rackrole': {
                'actions': ['view'],
                'id': 19,
                'constraints': None,
            },
            'rearport': {
                'actions': actions,
                'id': 71,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
            'rearporttemplate': {
                'actions': ['view'],
                'id': 69,
                'constraints': None,
            },
            'region': {
                'actions': ['view'],
                'id': 16,
                'constraints': None,
            },
            'site': {
                'actions': actions,
                'id': 11,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'sitegroup': {
                'actions': ['view'],
                'id': 91,
                'constraints': None,
            },
            'virtualchassis': {
                'actions': actions,
                'id': 35,
                'constraints': {"master__tenant__group__name": tenant_group_name},
            },
            'virtualdevicecontext': {
                'actions': actions,
                'id': 123,
                'constraints': {"device__tenant__group__name": tenant_group_name},
            },
        },

        'django_rq': {
            'queue': {
                'actions': ['view'],
                'id': 111,
                'constraints': None,
            },
        },

        'extras': {
            'branch': {
                'actions': ['view'],
                'id': 129,
                'constraints': None,
            },
            'cachedvalue': {
                'actions': ['view'],
                'id': 128,
                'constraints': None,
            },
            'configcontext': {
                'actions': ['view'],
                'id': 75,
                'constraints': None,
            },
            'configrevision': {
                'actions': ['view'],
                'id': 103,
                'constraints': None,
            },
            'configtemplate': {
                'actions': ['view'],
                'id': 139,
                'constraints': None,
            },
            'customfield': {
                'actions': ['view'],
                'id': 48,
                'constraints': None,
            },
            'customlink': {
                'actions': ['view'],
                'id': 77,
                'constraints': None,
            },
            'dashboard': {
                'actions': ['view'],
                'id': 140,
                'constraints': None,
            },
            'exporttemplate': {
                'actions': ['view'],
                'id': 53,
                'constraints': None,
            },
            'imageattachment': {
                'actions': ['view'],
                'id': 51,
                'constraints': None,
            },
            'journalentry': {
                'actions': ['view'],
                'id': 93,
                'constraints': None,
            },
            'objectchange': {
                'actions': ['view'],
                'id': 78,
                'constraints': None,
            },
            'report': {
                'actions': ['view'],
                'id': 84,
                'constraints': None,
            },
            'reportmodule': {
                'actions': ['view'],
                'id': 141,
                'constraints': None,
            },
            'savedfilter': {
                'actions': ['view'],
                'id': 127,
                'constraints': None,
            },
            'script': {
                'actions': ['view'],
                'id': 81,
                'constraints': None,
            },
            'scriptmodule': {
                'actions': ['view'],
                'id': 142,
                'constraints': None,
            },
            'stagedchange': {
                'actions': ['view'],
                'id': 130,
                'constraints': None,
            },
            'tag': {
                'actions': ['view'],
                'id': 79,
                'constraints': None,
            },
            'taggeditem': {
                'actions': ['view'],
                'id': 76,
                'constraints': None,
            },
            'webhook': {
                'actions': ['view'],
                'id': 80,
                'constraints': None,
            },
        },

        'ipam': {
            'aggregate': {
                'actions': actions,
                'id': 41,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'asn': {
                'actions': actions,
                'id': 102,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'asnrange': {
                'actions': actions,
                'id': 138,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'fhrpgroup': {
                'actions': ['view'],
                'id': 100,
                'constraints': None,
            },
            'fhrpgroupassignment': {
                'actions': ['view'],
                'id': 101,
                'constraints': None,
            },
            'ipaddress': {
                'actions': actions,
                'id': 39,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'iprange': {
                'actions': actions,
                'id': 99,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'l2vpn': {
                'actions': actions,
                'id': 124,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'l2vpntermination': {
                'actions': actions,
                'id': 126,
                'constraints': {"l2vpn__tenant__group__name": tenant_group_name},
            },
            'prefix': {
                'actions': actions,
                'id': 40,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'rir': {
                'actions': ['view'],
                'id': 42,
                'constraints': None,
            },
            'role': {
                'actions': ['view'],
                'id': 44,
                'constraints': None,
            },
            'routetarget': {
                'actions': actions,
                'id': 92,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'service': {
                'actions': actions,
                'id': 37,
                'constraints': [
                    {"device__tenant__group__name": tenant_group_name},
                    {"virtual_machine__tenant__group__name": tenant_group_name}
                ],
            },
            'servicetemplate': {
                'actions': ['view'],
                'id': 122,
                'constraints': None,
            },
            'vlan': {
                'actions': actions,
                'id': 43,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'vlangroup': {
                'actions': ['view'],
                'id': 45,
                'constraints': None,
            },
            'vrf': {
                'actions': actions,
                'id': 38,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
        },

        'netbox_inventory': {
            'asset': {
                'actions': actions,
                'id': 144,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'inventoryitemgroup': {
                'actions': ['view'],
                'id': 152,
                'constraints': None,
            },
            'inventoryitemtype': {
                'actions': ['view'],
                'id': 151,
                'constraints': None,
            },
            'purchase': {
                'actions': ['view'],
                'id': 150,
                'constraints': None,
            },
            'supplier': {
                'actions': ['view'],
                'id': 149,
                'constraints': None,
            },
        },

        # TODO: filter more
        'netbox_secrets': {
            'secret': {
                'actions': ['view'],
                'id': 145,
                'constraints': None,
            },
            'secretrole': {
                'actions': ['view'],
                'id': 146,
                'constraints': None,
            },
            'sessionkey': {
                'actions': ['view'],
                'id': 148,
                'constraints': None,
            },
            'userkey': {
                'actions': ['view', 'activate'],
                'id': 147,
                'constraints': [
                    {"user__groups__name": user_admin_group_name},
                    {"user__groups__name": user_view_group_name}
                ],
            },
        },

        'netbox_topology_views': {
            'individualoptions': {
                'actions': ['view'],
                'id': 143,
                'constraints': None,
            },
            'roleimage': {
                'actions': ['view'],
                'id': 131,
                'constraints': None,
            },
        },

        'tenancy': {
            'contact': {
                'actions': actions,
                'id': 106,
                'constraints': {"group__name": contact_group_name},
            },
            'contactassignment': {
                'actions': ['view'],
                'id': 107,
                'constraints': {"contact__group__name": contact_group_name},
            },
            'contactgroup': {
                'actions': ['view'],
                'id': 105,
                'constraints': {"name": contact_group_name},
            },
            'contactrole': {
                'actions': ['view'],
                'id': 104,
                'constraints': None,
            },
            'tenant': {
                'actions': actions,
                'id': 60,
                'constraints': {"group__name": tenant_group_name},
            },
            'tenantgroup': {
                'actions': ['view'],
                'id': 59,
                'constraints': {"name": tenant_group_name},
            },
        },

        'users': {
            'objectpermission': {
                'actions': ['view'],
                'id': 88,
                'constraints': None,
            },
            # 'token': {
            #     'actions': ['view'],
            #     'id': 61,
            #     'constraints': [{"user__groups__name": user_admin_group_name},
            #     {"user__groups__name": user_view_group_name}],
            # },
        },

        'virtualization': {
            'cluster': {
                'actions': actions,
                'id': 64,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'clustergroup': {
                'actions': ['view'],
                'id': 65,
                'constraints': {"name": cluster_group_name},
            },
            'clustertype': {
                'actions': ['view'],
                'id': 63,
                'constraints': None,
            },
            'virtualmachine': {
                'actions': actions,
                'id': 62,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'vminterface': {
                'actions': actions,
                'id': 83,
                'constraints': {"virtual_machine__tenant__group__name": tenant_group_name},
            },
        },

        'wireless': {
            'wirelesslan': {
                'actions': actions,
                'id': 109,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
            'wirelesslangroup': {
                'actions': ['view'],
                'id': 108,
                'constraints': {"name": wireless_lan_group_name},
            },
            'wirelesslink': {
                'actions': actions,
                'id': 110,
                'constraints': {"tenant__group__name": tenant_group_name},
            },
        },
    }

    count = 0
    for app, models in ct.items():
        for model, model_config in models.items():
            constraint = 'null' if model_config['constraints'] is None \
                else ("'" + dumps(model_config['constraints']) + "'")
            ct_id = model_config['id']
            for action in model_config.get('actions', actions):
                count += 1

                print(f'INSERT INTO public.users_objectpermission (name, description, enabled, constraints, actions) '
                      f'VALUES (\'{app}.{action}_{model}\', \'\', true, {constraint}, \'{{{action}}}\');')
                print(f'INSERT INTO public.users_objectpermission_object_types (objectpermission_id, contenttype_id) '
                      f'VALUES ((select currval(\'public.users_objectpermission_id_seq\')), {ct_id});')
                print(f'INSERT INTO public.users_objectpermission_groups (objectpermission_id, group_id) '
                      f'VALUES ((select currval(\'public.users_objectpermission_id_seq\')), {admin_group_id});')

                if action in ['view']:
                    print(f'INSERT INTO public.users_objectpermission_groups (objectpermission_id, group_id) '
                          f'VALUES ((select currval(\'public.users_objectpermission_id_seq\')), {view_group_id});')

    print(f'{count} items')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Permissions based on Tenants for NetBox.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    parser.add_argument('--admin_group_id', default=2, help='The ID of the admin group for this Tenant')
    parser.add_argument('--view_group_id', default=3, help='The ID of the view group for this Tenant')

    parser.add_argument('--tenant_group_name', default='scoutnet', help='The tenant_group_name for this Tenant')
    parser.add_argument('--wireless_lan_group_name', default='scoutnet',
                        help='The wireless_lan_group_name for this Tenant')
    parser.add_argument('--cluster_group_name', default='scoutnet', help='The cluster_group_name for this Tenant')
    parser.add_argument('--contact_group_name', default='scoutnet', help='The contact_group_name for this Tenant')
    parser.add_argument('--user_view_group_name', default='scoutnet_view',
                        help='The user_view_group_name for this Tenant')
    parser.add_argument('--user_admin_group_name', default='scoutnet_admin',
                        help='The user_admin_group_name for this Tenant')

    sys.exit(main(parser.parse_args()))
