import re

re_obj = re.compile(r'([.+]?(.yafo-document))')
regex = re_obj.sub('haha', "my_project.ajal.lasj_jfa_-.yafo-documnet")
print(regex)