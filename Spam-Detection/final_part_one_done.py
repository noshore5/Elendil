import csv
#read the spam csv file into a list

def read_data_from_file():

    data = []

    with open('spam.csv',encoding="latin-1") as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        # skip the first row

        next(csv_reader)

        for row in csv_reader:

            data.append(row)

    return data

#write features to a file

def write_features_to_file(text_length, does_have_spammy_words, does_have_links, class_label):

    # writing to csv file

    row = [text_length, does_have_spammy_words, does_have_links, class_label]

    with open("features.csv", 'a', newline='', encoding='utf-8') as csvfile:

        # creating a csv writer object

        csvwriter = csv.writer(csvfile)



        # writing the data rows

        csvwriter.writerow(row)

def does_have_links(sms_message):
    links = ['https','.com','.net','www.','.tv','http']
    text = sms_message.lower()

    for string in links:
        if (text.find(string)!= -1):
            return 'TRUE'

    return 'FALSE'

def does_have_spammy_words(sms_message): # returns true or false for whether it has spammy words
    spammy_words = ['WINNER','URGENT', 'FreeMsg','Congrats!','free','FREE', 'winner','PRIVATE!', 'URGENT!',
                    '4U', 'Free trial']

    text = sms_message.lower()

    for string in spammy_words:
        if (text.find(string) != -1):
            return 'TRUE'

    return 'FALSE'

def length_of_text(sms_message): # returns length of text
    return len(sms_message)


def main():
    data = read_data_from_file()

    for row in data:
        c1 = length_of_text(row[1])
        c2 = does_have_spammy_words(row[1])
        c3 = does_have_links(row[1])
        c4 = row[0]
        write_features_to_file(c1,c2,c3,c4)

main()

