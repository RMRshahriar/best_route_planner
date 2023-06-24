import cgi

form_inputs = cgi.FieldStorage()

input_by_user = form_inputs.getvalue()