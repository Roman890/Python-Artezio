# 4. На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент только один).
#    Нужно выполнить следующее преобразование и вывести максимальную вложенность.
#    Пример:
#         a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
#         foo(a) ->
#         {
#             'name': 'root',
#             'children': [
#                 {'name': 'element1', 'children': []},
#                 {'name': 'element2', 'children': []},
#                 {
#                     'name': 'element3',
#                     'children': [
#                         {'name': 'element4', 'children': []}
#                     ]
#                 }
#             ]
#         }, 2
#       в данном случае у element4 тэга вложенность/глубина 2


import xml.dom.minidom


a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
dom = xml.dom.minidom.parseString(a)
dom.normalize()

print("{")
nodeArray=dom.getElementsByTagName("root")[0]
print("\t'name': '%s'," % nodeArray.nodeName)
childList=nodeArray.childNodes
print("\t'children': [ ")
for child in childList:
    print("\t\t'name': '%s'," % child.nodeName)
print("}")


