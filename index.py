from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

data = {
    'title': 'Dynamic HTML Template',
    'header': 'Welcome to my website!',
    'items': ['Item 1', 'Item 2', 'Item 3']
}

html_content = template.render(data)


print(html_content)