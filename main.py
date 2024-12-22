import re
import codecs
import csv


print()
print('Задание 1')
print()

with open('task1-en.txt') as file:
    s = file.read()
    print(re.findall(r"\b[A-Za-z]+-[A-Za-z]+\b", s))
    print(re.findall(r"\(.*?\)", s))

print()
print('Задание 2')
print()

with codecs.open('task2.html', 'r', 'utf-8') as task2:
    s = task2.read()
    # print(re.findall(r'https:[a-zA-Z0-9\/.а-яА-Я]+\.com[a-zA-Z0-9\/.а-яА-Я=_?!]*', s))
    print(re.findall(r'https:[a-zA-Z0-9\/.а-яА-Я%$#@!+=_-]+\.com[^")\']*', s))
    # print(re.findall(r'https:[^ \'")\]\}]+\.com[^")\']*', s))

with open('result.csv', 'w') as file:

    writer = csv.writer(file, delimiter=' ', quotechar="|")
    writer.writerow(['ID', 'Name', 'Email', 'Date of Registration', 'Website'])

    with open('task3.txt') as text:
        text = text.read()
        text = re.sub(r' ', r'   ', text)
        text = ' ' + text
        IDs = re.findall(r' \d{1,3} ', text)
        Emails = re.findall(r' [^ ]+@[^ ]+ ', text)
        Names = re.findall(r' [A-Za-z]+ ', text)
        Dates = re.findall(r' [0-9]*-[0-9]*-[0-9]* ', text)
        Sites = re.findall(r' https?:[\/.@a-zA-Z-]+ ', text)
        
    for i in range(len(IDs)):
        writer.writerow([f'{IDs[i]}', f'{Names[i]}', f'{Emails[i]}', f'{Dates[i]}', f'{Sites[i]}'])
        


