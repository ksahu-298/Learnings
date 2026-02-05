# You are given a list of programming languages: ["Python", "Java", "C++", "Python", "Java", "C"], Convert it into a set and print how many unique languages you knows.

languages_list = ["Python", "Java", "C++", "Python", "Java", "C"]
unique_languages = set(languages_list)
print(f"You know {len(unique_languages)} unique programming languages: {unique_languages}")
