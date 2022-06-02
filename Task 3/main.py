dannie = 'yourflagis{fhke37_kdrjknbmpr_04374j}'
kluch = 'thekey'
a = 'qwertyuiopasdfghjklzxcvbnm_{}1234567890'
otvet = ""
number = 0

for b in dannie:
    if b in a:
        otvet += a[(a.find(kluch[number%len(kluch)])+ \
        a.find(b)+2)%len(a)]
        number += 1
    else:
        otvet += b
print(otvet)
