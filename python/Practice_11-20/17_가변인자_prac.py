# def profile(name, age, language1, language2, language3, language4, language5):
#     print("name: {0}\tage: {1}\t".format(name, age), end=" ")
#     print(language1, language2, language3, language4, language5)

# profile("John", 25, "Python", "Java", "C++", "C#", "Python")
# profile("John", 25, "Python", "Java"," "," "," ")

def profile(name, age, *language):
    print("name: {0}\tage: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("John", 25, "Python", "Java", "C++", "C#", "Python", "JavaScript")
profile("John", 25, "Python", "Java")
