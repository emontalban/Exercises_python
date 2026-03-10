'''
La idea es crear una función llamada heading_generator
que reciba dos argumentos:
title → el texto del título
heading_type → el número del encabezado HTML
que devuelva <h1>Greeting</h1>
'''
# 1ª forma
def heading_generator(title, heading_type):
    code = f'<h{heading_type}> {title} </h{heading_type}>'
    return code
print(heading_generator("Hello", '2'))

# 2ª forma
def heading_generator(title, heading_type):
    code = '<h{0}> {1} </h{0}>'.format(heading_type, title)
    return code
print(heading_generator("Gretting", '1'))

# 3ª forma
def heading_generator(title, heading_type):
    code = '<h' + heading_type + '> ' + title + ' </h'+ heading_type +'>'
    return code
print(heading_generator("Bye", '2'))

