# დავალების შესასრულებლად გამოიყენეთ movies.json
#
# წაიკითხეთ მოცემული ფაილი და ამავე ფაილში ჩაწერეთ ის ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე მეტი და ჟანრი
# არის Crime, ხოლო Crime სიტყვა ჟანრში შეცვალეთ New_Crime-ით. ამავე ფაილში ჩაწერეთ ისეთი ფილმები, რომელთა გამოშვების
# თარიღიც არის 2000-ზე ნაკლები, ჟანრი არის Drama და ჟანრის სახელი ჩაუწერეთ Old_Drama. იმ ფილმებს, რომელიც 2000 წელს არის
# გამოშვებული ჟანრში ჩაუმატეთ New_Century და ეს ფილმებიც ამავე ფაილში ჩაწერეთ.

import json

with open('movies.json', 'r') as f:
    data = json.load(f)

new_crime = []
old_drama = []
new_century = []

def reorganize(film: dict):
    release_date = int(film['release_date'][:4])
    genres = film['genres']
    if release_date > 2000 and 'Crime' in genres:
        film['genres'] = ['New_Crime' if genre == 'Crime' else genre for genre in genres]
        new_crime.append(film)
    elif release_date < 2000 and 'Drama' in genres:
        film['genres'] = ['Old_Drama' if genre == 'Drama' else genre for genre in genres]
        old_drama.append(film)
    elif release_date == 2000:
        film['genres'].append('New_Century')
        new_century.append(film)


for film in data[0]['results']:
    reorganize(film)

combined_data = new_crime + old_drama + new_century

with open('movies.json', 'w') as f:
    json.dump(combined_data, f, indent=4)
