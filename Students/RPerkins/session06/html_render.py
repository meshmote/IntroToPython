__author__ = 'Robert W. Perkins'


#!/usr/bin/env python

"""
Python class example.
"""


class Element(object):

    tag = '<html>'
    endtag = '</html>'
    indent = ''

    def __init__(self, content=None, **attrib):
        self.attrib = attrib
        self.content = [content]

    def append(self, new_content):
        """Check for existing content and add new_content"""

        if self.content[0] is None:
            self.content = [new_content]
        else:
            self.content.append(new_content)

    def render(self, file_out, ind=""):
        """Write tags and call render method on content objects"""

        if self.attrib.get('style') is None:
            file_out.write('{tag_indent}{start_tag}\n'.format(tag_indent=self.indent, start_tag=self.tag,))
        else:
            file_out.write('{tag_indent}{tag_front} style="{ival}">\n'.format
                          (tag_indent=self.indent, tag_front=self.tag[:-1], ival=self.attrib.get('style')))
        for item in self.content:
            if type(item) == str:
                file_out.write('        {out_string}\n'.format(out_string=item))
            else:
                item.render(file_out, "    ")
        file_out.write('{tag_indent}{end_tag}\n'.format(tag_indent=self.indent, end_tag=self.endtag))


class Html(Element):

    tag = '<html>'
    endtag = '</html>'

    def render(self, file_out, ind=""):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, ind)


class P(Element):

    tag = '<p>'
    endtag = '</p>'
    indent = '        '

    def render(self, file_out, ind=""):
        """Write paragraph content and tags to the file_out StringIO object"""

        if self.attrib.get('style') is None:
            file_out.write('{tag_indent}{start_tag}\n'.format(tag_indent=self.indent, start_tag=self.tag,))
        else:
            file_out.write('{tag_indent}{tag_front} style="{ival}">\n{element_indent}{content}\n'
                           '{tag_indent}{end_tag}\n'.format(tag_indent=self.indent, tag_front=self.tag[:-1],
                                                            ival=self.attrib.get('style'),
                                                            element_indent=ind+self.indent, content=self.content[0],
                                                            end_tag=self.endtag))


class Body(Element):

    tag = '<body>'
    endtag = '</body>'
    indent = '    '


class Head(Element):

    tag = '<head>'
    endtag = '</head>'
    indent = '    '


class OneLineTag(Element):

    def render(self, file_out, ind=""):
        """Write single line elements to the file_out StringIO object"""

        file_out.write('{tag_indent}{start_tag}{content}{end_tag}\n'.format
                      (tag_indent=self.indent, start_tag=self.tag,
                       content=self.content[0], end_tag=self.endtag))


class Title(OneLineTag):

    tag = '<title>'
    endtag = '</title>'
    indent = '        '


class SelfClosingTag(Element):

    indent = '        '

    def render(self, file_out, ind=""):
        """Write tags and call render method on content objects"""
        if self.attrib.get('style') is None:
            file_out.write('{tag_indent}{start_tag}\n'.format(tag_indent=self.indent, start_tag=self.tag,))
        else:
            file_out.write('{tag_indent}{tag_front} style="{ival}"/>\n'.format
                          (tag_indent=self.indent, tag_front=self.tag[:-2], ival=self.attrib.get('style')))


class Hr(SelfClosingTag):
    tag = '<hr />'


class Br(SelfClosingTag):
    tag = '<br />'


class A(Element):

    tag = '<a>'
    endtag = '</a>'
    indent = '        '

    def __init__(self, link, content):
        self.link = {'href': link}
        self.content = content
        attrib = {}
        Element.__init__(self, content, **attrib)

    def render(self, file_out, ind=""):
        """Write element tags, link, and content to the file_out StringIO object"""

        l_string = '{m_key}={m_item}'.format(m_key=str(self.link)[2:6], m_item=str(self.link)[9:-1])
        file_out.write('{tag_indent}{start_tag} {link}>{end_tag}\n'.format
                      (tag_indent=self.indent, start_tag=self.tag[:-1],
                          link=l_string, end_tag=self.endtag))


class Ul(Element):
    tag = '<ul>'
    endtag = '</ul>'
    indent = '        '


class Li(Element):
    tag = '<li>'
    endtag = '</li>'
    indent = '            '


class H(OneLineTag):
    tag = '<h>'
    endtag = '</h>'
    indent = '        '

    def __init__(self, level, content):
        self.level = level
        self.tag = '{tag_open}{h_level}{tag_close}'.format(tag_open=self.tag[:-1], h_level=self.level,tag_close='>')
        self.endtag = '{tag_open}{h_level}{tag_close}'.format(tag_open=self.endtag[:-1], h_level=self.level, tag_close='>')
        Element.__init__(self, content)

    def render(self, file_out, ind=""):
        """Write single line elements to the file_out StringIO object"""
        file_out.write('{tag_indent}{start_tag}{content}{end_tag}\n'.format
                      (tag_indent=self.indent, start_tag=self.tag,
                       content=self.content[0], end_tag=self.endtag))


class Meta(SelfClosingTag):
    tag = '<meta />'

    def __init__(self, **meta):
        self.meta = meta
        m_string = '{m_key}={m_item}'.format(m_key=str(meta)[1:9], m_item=str(meta)[12:])
        self.tag = '{tag_open}{m_key}{tag_close}'.format(tag_open=self.tag[:-2], m_key=m_string[1:-1], tag_close=' />')
        Element.__init__(self, meta)