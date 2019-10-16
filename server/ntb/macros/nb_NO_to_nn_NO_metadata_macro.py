"""
nb-NO to nn-NO Metadata Macro will perform the following changes to current content item:
- change the language to nn-NO
- change the body footer to "(©NPK)" - NB: copyrightsign, not @
- change the service (ANPA category) to "NPKTema"
"""


def nb_NO_to_nn_NO_metadata_macro(item, **kwargs):
    item['body_footer'] = '(©NPK)'
    item['language'] = 'nn-NO'
    item['anpa_category'] = [
        {
            'qcode': 'a',
            'selection_type': 'single selection',
            'name': 'NPKTema',
            'language': 'nn-NO',
            'scheme': None
        }
    ]
    return item


name = 'Bokmal to Nynorsk Metadata Macro'
label = 'Translate to Nynorsk Macro'
callback = nb_NO_to_nn_NO_metadata_macro
access_type = 'backend'
action_type = 'direct'
from_languages = ['nb-NO']
to_languages = ['nn-NO']
