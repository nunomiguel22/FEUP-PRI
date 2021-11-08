import pandas as pd

winemag = pd.read_csv('datasets\winemag-filtered.csv')

blog = pd.read_csv('datasets\BlogOsVinhos.csv')


winemag_titles = winemag['title']
blog_titles = blog['Name']

MATCHES = 0

print(winemag_titles)
print(blog_titles)



for winemag_title in winemag_titles:
    for blog_title in blog_titles: 
        blog_title_arr = blog_title.split()
        if set(blog_title_arr) <= set(winemag_title.split()):
            MATCHES += 1
            if MATCHES % 100 == 0:
                print(str(MATCHES) + ' matches')


print(MATCHES)


