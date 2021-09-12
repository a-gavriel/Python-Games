import csv, json, random

## global variable of score for easy access
global scores
scores = []

# First row contains the header of the table
def getindexscore(user_data):
    global scores
    if int(user_data[1]) > int(scores[1][1]):
        return 1
    elif int(user_data[1]) > int(scores[2][1]):
        return 2
    elif int(user_data[1]) > int(scores[3][1]):
        return 3
    elif int(user_data[1]) > int(scores[4][1]):
        return 4
    elif int(user_data[1]) > int(scores[5][1]):
        return 5
    else:
        return -1

# Inserts the user data in the given index, and deletes the last element
def replacescore(user_data, index):
    global scores
    scores.insert(index,user_data)
    scores.pop(-1)

# Loads the scores from the CSV
def readcsv():
    global scores
    scores = []
    with open('scores.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            scores += [row]
    
    csvFile.close()

def read_json():
    global scores
    scores = [["Name","Score"]]
    with open('scores.json', 'r') as jsonFile:
        data = json.load(jsonFile)
    jsonFile.close()

    score_list = data['Scoreboard']
    for score in score_list:
        scores.append([score['Name'], score['Score']])
    
def csv_to_json():
    # read CSV
    with open('scores.csv','w+', newline='') as outfilecsv: # w+ truncates file first
        writer = csv.writer(outfilecsv)
        writer.writerows(scores)
    outfilecsv.close()


    ## generates JSON from CSV
    jsonfile = open("scores.json", "w+")
    jsonfile.write('{\n "Scoreboard":')
    with open("scores.csv","r+") as csvfile:
        next(csvfile,None)
        reader = csv.DictReader(csvfile,fieldnames = ["Name","Score"])
        json.dump([row for row in reader], jsonfile, indent=4)
    
    jsonfile.write('\n}')
    jsonfile.close()
    csvfile.close()

def add_random_score():
    ## current user score and name
    user_name = 'A' + str(random.randint(1, 100))
    user_score = random.randint(1, 1000)
    ## Places the player data in the top5 scoreboard
    user_data = [user_name, str(user_score)]
    print("Inserting new user data: ",user_data)
    scoreboardindex = getindexscore(user_data)
    if (scoreboardindex != -1):
        replacescore(user_data, scoreboardindex)
    print(scores)


def main():
    global scores


    default_values = True
    if default_values:
        scores = [["Name","Score"]]+[["None","0"]]*5
        print("Using default scoreboard")
        print(scores)

    loadCSV = False
    if loadCSV:
        readcsv()
        print("Loaded scores from CSV file:")
        print(scores)
    
    loadJSON = False
    if loadJSON:
        read_json()
        print("Loaded scores from JSON file:")
        print(scores)

    add_random_score()


    #csv_to_json()

main()
