import csv

with open('users.csv', 'wb') as f:
    filewriter=csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['username','email','phone','password'])

username=f'username: {input()}'
email=f'username: {input()}'
phone=f'username: {input()}'
password=f'username: {input()}'

filewriter.writerow([str(username), str(email), str(phone), str(password)])

with open('users.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)




