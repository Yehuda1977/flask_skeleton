#!/usr/bin/python3

##############################################
#
# utils.py
# webapp
#
##############################################

from wtforms.fields.core import Field, UnboundField

def get_form_fields(form):
    """
    This function extracts the fields from a Flask_WTForms object
    """

    fields = []
    for attr in dir(form):
        # Skip the attrs with double underscore
        if attr.startswith('__'): continue

        # Check if this attribute is a field

        # Retrieve the attribute value
        value = getattr(form, attr)

        # Check if its class is a subclass of field
        if issubclass(value.__class__, Field) or issubclass(value.__class__, UnboundField) :
            # Append the name and the field itself
            fields.append((attr, value))

    return fields



