import pandas as pd

winemag = pd.read_csv('datasets\wm.csv')

blog = pd.read_csv('datasets\BlogOsVinhos.csv')

MATCHES = 0

for i, winemag_row in winemag.iterrows():
    winemag_title = winemag_row['title']
    for _, blog_row in blog.iterrows():
        blog_title_arr = blog_row['Name'].split()
        if set(blog_title_arr) <= set(winemag_title.split()):
            winemag_row['BJudge'] = blog_row['Judge']
            winemag_row['BJudgeRating'] = blog_row['JudgeRating']
            winemag_row['BJudgeNotes'] = blog_row['JudgeNotes']
            MATCHES += 1
            if MATCHES % 100 == 0:
                print(str(MATCHES) + ' matches')


print(MATCHES)

winemag.to_csv('datasets/wm2.csv')
