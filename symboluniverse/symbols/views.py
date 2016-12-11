from django.shortcuts import render
from django.http import HttpResponse

def symbol(request, html_number_string="", unicode_hexadecimal_string=""):
    if html_number_string == "":
        # Use the `unicode_hexadecimal_string`
        unicode_number_int = int(unicode_hexadecimal_string, 16)
        original_symbol = chr(unicode_number_int)
        display_symbol = original_symbol # TODO: Set then`display_symbol` to
                                         # something else, if needed. For
                                         # example, ''' should be rendered as
                                         # '␀' and '' should be rendered as
                                         # '␁'.
    else:
        # Use the `html_number_string`
        html_number_int = int(html_number_string)
        original_symbol = chr(html_number_int)
        display_symbol = original_symbol # TODO: Set then`display_symbol` to
                                         # something else, if needed. For
                                         # example, ''' should be rendered as
                                         # '␀' and '' should be rendered as
                                         # '␁'.

    context = {'original_symbol': original_symbol,
               'display_symbol': display_symbol}
    response = render(request, 'symbols/symbol.html', context)

    return HttpResponse(response)
