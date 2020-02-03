"""
4. На вход функции передается строка с xml документом
  (тэги без аттрибутов, корневой элемент только один).
  Нужно выполнить следующее преобразование и вывести максимальную вложенность.
  Пример:
       a = '<root><element1 /><element2 />
       <element3><element4 /></element3></root>'
       foo(a) ->
       {
           'name': 'root',
           'children': [
               {'name': 'element1', 'children': []},
               {'name': 'element2', 'children': []},
               {
                   'name': 'element3',
                   'children': [
                       {'name': 'element4', 'children': []}
                   ]
               }
           ]
       }, 2
     в данном случае у element4 тэга вложенность/глубина 2
"""

import xml.dom.minidom


def function(xml_text, t=1):
    """провести преобразование и вывести максимальную вложенность"""
    string = ""
    for i in range(t):
        string += '\t'
    number = 1
    dom = xml.dom.minidom.parseString(xml_text)
    dom.normalize()
    print("%s{" % string)
    node_array = dom.getElementsByTagName(dom.firstChild.tagName)[0]

    print("%s'name': '%s'," % (string, node_array.nodeName))
    child_list = node_array.childNodes
    print("%s'children': [ " % string)
    t += 1
    for i in range(t):
        string += '\t'
    for child in child_list:
        if child.firstChild is None:
            print("%s{'name': '%s', 'children': []},"
                  % (string, child.nodeName))
        else:
            number += function(str(child.toxml()), t)

    print("%s]" % string)
    print("%s}" % string)
    return number


xml_text = '<root><element1 /><element2 />' \
           '<element3><element4><element5 /></element4></element3></root>'
print("Вложенность :", function(xml_text))
