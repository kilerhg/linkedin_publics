# Import Libs
import re

# Dict with some userfull RegEX expressions
dict_pattern_regex = {
    'cep':r"^\d{5}-\d{3}$",
    'cpf':r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
    'cnpj':r"^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$",
    'rg':r"^\d{2}\.\d{3}\.\d{3}-\d{1}$",
    'cellphone':r"^\(\d{2}\)\d{4}-\d{4}$",
    'email':r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    'date':r"^\d{2}\/\d{2}\/\d{4}$",
    'time':r"^\d{2}:\d{2}$",
    'date_time':r"^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}$",
    'ipv4':r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
    'url':r"^(http|https):\/\/[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(([0-9]{1,5})?\/.*)?$",
    'name':r"^[a-zA-Zà-úÀ-Ú]]+$",
    'full_name':r"^[a-zA-Zà-úÀ-Ú]\s]+$",
    'html_tag':r"/^<([a-z1-6]+)([^<]+)*(?:>(.*)<\/\1>| *\/>)$/",
    'hex_color':r"/^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$/",
}


# CPF: 000.000.000-00
value_input = str(input('Value: ')).strip()

# cpf
option_regex_pattern = str(input('Option_Pattern: ')).strip().lower()

if option_regex_pattern in dict_pattern_regex.keys():

    regex_pattern = dict_pattern_regex[option_regex_pattern]

    # Use the re.search when you want to find all occurrences
    result_one = re.match(regex_pattern, value_input)

    # Use the re.findall when you want to find all occurrences
    result_all = re.findall(regex_pattern, value_input)

    print(result_one)
    # <re.Match object; span=(0, 14), match='000.000.000-00'

    print(result_one.group())
    # 000.000.000-00

    print(result_all)
    # ['000.000.000-00']