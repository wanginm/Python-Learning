favorite_language={
    'jen':'python',
    'sarsh':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in favorite_language.keys():
    print(name.title())
if 'erin' not in favorite_language.keys():
    print("Erin,please take our poll")
for name in sorted(favorite_language.keys()):
    print(name.title())
for language in favorite_language.values():
    print(language.title())
print("=============")
for language in set(favorite_language.values()):
    print(language.title())