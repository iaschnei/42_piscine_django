from elem import Elem, Text

from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br

class Page:
    VALID_TAGS = {
        'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr',
        'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'
    }

    def __init__(self, root: Elem):
        self.root = root

    def is_valid(self):
        def validate(node):
            if not isinstance(node, (Elem, Text)):
                return False

            if isinstance(node, Text):
                return True

            if node.tag not in Page.VALID_TAGS:
                return False

            content = node.content or []
            if not isinstance(content, list):
                content = [content]

            if not self._check_structure(node.tag, content):
                return False

            for child in content:
                if not validate(child):
                    return False

            return True

        return validate(self.root)

    def _check_structure(self, tag, content):
        if tag == 'html':
            return self._html_rule(content)
        elif tag == 'head':
            return self._head_rule(content)
        elif tag == 'body':
            return self._body_or_div_rule(content)
        elif tag == 'div':
            return self._body_or_div_rule(content)
        elif tag == 'title':
            return self._single_text_rule(content)
        elif tag == 'h1':
            return self._single_text_rule(content)
        elif tag == 'h2':
            return self._single_text_rule(content)
        elif tag == 'li':
            return self._single_text_rule(content)
        elif tag == 'th':
            return self._single_text_rule(content)
        elif tag == 'td':
            return self._single_text_rule(content)
        elif tag == 'p':
            return self._p_rule(content)
        elif tag == 'span':
            return self._span_rule(content)
        elif tag == 'ul':
            return self._ul_ol_rule(content)
        elif tag == 'ol':
            return self._ul_ol_rule(content)
        elif tag == 'tr':
            return self._tr_rule(content)
        elif tag == 'table':
            return self._table_rule(content)
        return True  # for tags with no rules

    def _html_rule(self, content):
        return (
            len(content) == 2 and
            isinstance(content[0], Head) and
            isinstance(content[1], Body)
        )

    def _head_rule(self, content):
        return len(content) == 1 and isinstance(content[0], Title)

    def _body_or_div_rule(self, content):
        allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text)
        return all(isinstance(e, allowed) for e in content)

    def _single_text_rule(self, content):
        return len(content) == 1 and isinstance(content[0], Text)

    def _p_rule(self, content):
        return all(isinstance(e, Text) for e in content)

    def _span_rule(self, content):
        return all(isinstance(e, (Text, P)) for e in content)

    def _ul_ol_rule(self, content):
        return len(content) >= 1 and all(isinstance(e, Li) for e in content)

    def _tr_rule(self, content):
        if len(content) == 0:
            return False
        all_th = all(isinstance(e, Th) for e in content)
        all_td = all(isinstance(e, Td) for e in content)
        return all_th or all_td

    def _table_rule(self, content):
        return all(isinstance(e, Tr) for e in content)

    def __str__(self):
        html = str(self.root)
        if isinstance(self.root, Html):
            return "<!DOCTYPE html>\n" + html
        return html

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

def test_valid_page():
    page = Page(Html(content=[
        Head(content=Title(Text("Test Page"))),
        Body(content=[
            H1(Text("Hello")),
            Div(content=[
                P(content=[Text("Text in paragraph")]),
                Span(content=[Text("inline span")]),
                Ul(content=[Li(Text("Item 1"))]),
                Table(content=[
                    Tr(content=[Th(Text("Name")), Th(Text("Age"))]),
                    Tr(content=[Td(Text("Alice")), Td(Text("30"))])
                ])
            ])
        ])
    ]))

    print("Is valid:", page.is_valid())
    print(page)
    page.write_to_file("output.html")

def test_invalid_page():
    page = Page(Html(content=[
        Head(content=[Title(Text("T")), Meta()]),
        Body(content=[H1(Text("Oops"))])
    ]))

    print("Is valid:", page.is_valid())

def main():
    test_valid_page()
    test_invalid_page()

if __name__ == '__main__':
    main()
