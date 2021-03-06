from contextlib import contextmanager

class Doc:
    """
    Generate xml/html documents using context managers

    c.f: https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager
    """

    def __init__(self):
        self._result = []

    def text(self, *args, safe=False):
        txt = []
        for atom in args:
            atom = str(atom)
            if not safe:
                atom = html_escape(atom)
            txt.append(atom)
        self._result.append(''.join(txt))

    @contextmanager
    def tag(self, name, *attrs, **kwattrs):
        self.text("<", name, _mkAttribs(attrs, kwattrs), ">", safe=True)
        yield
        self.text("</", name, ">", safe=True)

    def self_closing(self, name, *attrs, **kwattrs):
        self.text("<", name, _mkAttribs(attrs, kwattrs), "/>", safe=True)

    def line(self, name, cont, *args, **kwargs):
        with self.tag(name, *args, **kwargs):
            self.text(cont)

    def _mkTag(name, self_closing=False):
        if self_closing:
            def _inner(self, *attrs, **kwattrs):
                self.self_closing(name, *attrs, **kwattrs)
        else:
            @contextmanager
            def _inner(self, *attrs, **kwattrs):
                with self.tag(name, *attrs, **kwattrs):
                    yield
        return _inner

    html = _mkTag("html")
    p = _mkTag("p")
    div = _mkTag("div")
    a = _mkTag("a", self_closing=True)
    br = _mkTag("br", self_closing=True)


    def render(self):
        return '\n'.join(self._result)

def _mkAttribs(attrs, kwattrs):
    attrs = list(map(lambda a:' "'+str(a)+'"', attrs))
    for (k,v) in kwattrs.items():
        if k == "klass":
            k = "class"
        attrs.append(f' {k}="{str(v)}"')
    return ''.join(attrs)

def html_escape(txt):
    return str(txt).replace("&", "&amp;")\
                   .replace("<", "&lt;")\
                   .replace(">", "&gt;")\
                   .replace('"', "&quot;")

