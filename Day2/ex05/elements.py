from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('html', attr, content, 'double')

class Head(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('head', attr, content, 'double')

class Body(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('body', attr, content, 'double')
    
class Title(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('title', attr, content, 'double')

class Meta(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('meta', attr, content, 'simple')
        
class Img(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('img', attr, content, 'simple')
        
class Table(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('table', attr, content, 'double')
        
class Th(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('th', attr, content, 'double')
        
class Tr(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('tr', attr, content, 'double')
        
class Td(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('td', attr, content, 'double')
        
class Ul(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('ul', attr, content, 'double')
        
class Ol(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('ol', attr, content, 'double')
        
class Li(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('li', attr, content, 'double')
        
class H1(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('h1', attr, content, 'double')
        
class H2(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('h2', attr, content, 'double')
        
class P(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('p', attr, content, 'double')
        
class Div(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('div', attr, content, 'double')
        
class Span(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('span', attr, content, 'double')
        
class Hr(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('hr', attr, content, 'simple')
        
class Br(Elem):
    def __init__(self, content=None, attr = {}):
        super().__init__('br', attr, content, 'simple')




def main():
    result = Html(content=[
        Head(content=Title(content=Text('"Hello ground!"'))),
        Body(content=[
            H1(content=Text('"Oh no, not again!"')),
            Img(attr={'src': 'https://i.imgur.com/pfp3T.jpg'})
        ])
    ])

    print(result)

    page = Html(content=[
        Head(content=[
            Meta(attr={'charset': 'UTF-8'}),
            Title(Text("Sample Page"))
        ]),
        Body(content=[
            H1(Text("Welcome to the Test Page")),
            H2(Text("A Subtitle")),
            P(content=[
                Text("This is a sample paragraph with a "),
                Span(Text("span")),
                Text(" and a "),
                Br(),
                Text("line break.")
            ]),
            Hr(),
            Img(attr={'src': 'https://i.imgur.com/pfp3T.jpg', 'alt': 'Sample image'}),
            Div(content=[
                P(Text("Inside a div!"))
            ]),
            Table(content=[
                Tr(content=[
                    Th(Text("Name")),
                    Th(Text("Age"))
                ]),
                Tr(content=[
                    Td(Text("Alice")),
                    Td(Text("30"))
                ]),
                Tr(content=[
                    Td(Text("Bob")),
                    Td(Text("25"))
                ])
            ]),
            Ul(content=[
                Li(Text("Unordered Item 1")),
                Li(Text("Unordered Item 2"))
            ]),
            Ol(content=[
                Li(Text("Ordered Item A")),
                Li(Text("Ordered Item B"))
            ])
        ])
    ])

    print(page)

if __name__ == '__main__':
    main()
