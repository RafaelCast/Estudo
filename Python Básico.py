import unicodedata

#26
def sum_num(a: int, b: int) -> int:
    return a + b

#27
def check_pair(number: int) -> bool:
    return number % 2 == 0


result = check_pair(3)
print(result)

#28
list_numb = list(range(1,11))

#29
def vowel_quant(text: str) -> int:
    without_accent = ''.join(
    ch
    for ch in unicodedata.normalize('NFD', text)
    if not unicodedata.combining(ch)
)

    return sum(1 for ch in without_accent.lower() if ch in 'aeiou')

print(vowel_quant("Programação")) # 5

#30
data = {'name': 'Rafael', 'idade': '22', 'cidade': 'São Paulo'}
print('Ola', data['name'], 'voce tem', data['idade'], 'e mora em', data['cidade'])
