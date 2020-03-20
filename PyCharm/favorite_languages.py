favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','hasekell'],
}
for name,languages in favorite_languages.items():
    print(name.title())
    for language in languages:
        print(language.title())