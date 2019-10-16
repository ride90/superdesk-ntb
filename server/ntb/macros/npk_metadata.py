"""
NPKSisteNytt Metadata Macro will perform the following changes to current content item:
- change the byline to "(NPK-NTB)"
- change the signoff to "npk@npk.no"
- change the body footer to "(©NPK)" - NB: copyrightsign, not @
- change the service to "NPKSisteNytt"
"""


def npk_metadata_macro(item, **kwargs):
    item['byline'] = 'NPK-' + item.get('byline', '')
    item['sign_off'] = 'npk@npk.no'
    item['body_footer'] = '(©NPK)'
    item['language'] = 'nn-NO'
    item['anpa_category'] = [
        {
            'qcode': 's',
            'selection_type': 'single selection',
            'name': 'NPKSisteNytt',
            'language': 'nn-NO',
            'scheme': None
        }
    ]
    return item


name = 'NPKSisteNytt Metadata Macro'
label = 'NPKSisteNytt Metadata Macro'
callback = npk_metadata_macro
access_type = 'frontend'
action_type = 'direct'
