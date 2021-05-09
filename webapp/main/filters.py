# List of custom jinja filters
# A filter is just a function that receives a string and return a string

from . import main_blueprint

@main_blueprint.app_template_filter()
# Generate a function that encrypts a given string with <encryption_char>
def encrypt(s):
    """
    Encrypt a string "foostring" to "*********"
    :param s: The string to encrypt
    :return: The encrypted string
    """

    # Add as many <encryption_char> as the letters in s
    encrypted = encryption_char*len(s)

    return encrypted




