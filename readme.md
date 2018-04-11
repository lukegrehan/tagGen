Generate xml/html documents using context managers

c.f: https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager

```python
d = Doc()
with d.tag("html"):
  with d.tag("body"):
    d.text("Some links:")
    with d.tag("ul"):
      for i in range(5):
        with d.tag("li"):
          d.line("a", f"Link {i}", href=f"/somelink{i}.html")
print(d.render())
```

generates:

```html
<html>
  <body>
    Some links:
    <ul>
      <li> <a href="/somelink.html"> Link 0 </a> </li>
      <li> <a href="/somelink.html"> Link 1 </a> </li>
      <li> <a href="/somelink.html"> Link 2 </a> </li>
      <li> <a href="/somelink.html"> Link 3 </a> </li>
      <li> <a href="/somelink.html"> Link 4 </a> </li>
    </ul>
  </body>
</html>
```
