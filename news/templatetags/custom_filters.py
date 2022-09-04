from django import template
from news.resources import BAD_WORDS


register = template.Library()


@register.filter()
def censor(text: str):
    new_text = text
    for one_word in BAD_WORDS:
        if new_text.lower().find(one_word):
            new_text = new_text.replace(one_word, f' {one_word[:1]}{(len(one_word)-1)*"*"}', new_text.count(one_word))
    return f'{new_text}'



#from django import template

#register = template.Library()

#@register.filter(name='Censor')
#def censor(value, arg):
#    value = value.replace("жесть", "В ШОКЕ")
#   value = value.replace("афигенно", "ЗДОРОВО")
#    value = value.replace("хрень", "ПЛОХО")
#    return value



#@register.filter(name='Censor1')
#def Censor1(value, arg):
#    if ("жесть" in value) or ("афигенно" in value) or ("хрень" in value):
#        arg = 'Вы используете плохие слова'
#        return arg
#    else:
#        return value
