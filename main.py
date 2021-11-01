from person import person as pers
ann = pers(59,43,997)

p="Всем привет!"
s=ann.shifr(p)

print("зашифрованная '",p,"' будет ", s)
des=ann.deshifr(s)
print("Расшифруем обратно - ", des)
