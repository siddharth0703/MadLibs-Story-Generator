import copy
from random import randint

story = ("{} is a very suave guy played by {}. He's done\
            some very bad things, but he's very cool .He has\
            long conversation with a {}, in which he makes {}\
            reference to a classic hollywood film that was based on the\
            obscure Japnese film  {}, then he kills him violently\
            by {}ing him in the {} and then {}ing his {} off. After making another\
            really great regfernec to {}, he drives a {} to the home of {}.They have a another very long, worddy,\
            sharp tongued conversation i twhich the cinermatorgrapy reference {}.\
            and the dialogue is an homage to {}, adn they then get in a very bloody {} fight in which they\
            {}each others {} with {} and talk about {}for a very long time\
            ")

# create a dictionay to look the words
word_dict = {
    'name': ['Brad', 'Matt', 'Damon', 'Patrick','Jane','Kevin','Robin','Matt','Ronin'],
    'verb': ['singing', 'dancing', 'killing', 'jogging','hopping','laughing','frangling','mixing'],
    'movie': ['The Devils Advocate', 'Last of Us', 'The Departed','Ppoint Arrow','The Dark Knight','Batman Begins'],
    'nouns': ['people', 'music', 'dog', 'hamster', 'ball', 'hotdog','bed','pot','mug','crowd','personality','friend','last','prank','discord','lost','joke','after'],
    'adjective': ['longing', 'strong', 'muscular'],
    'place': ['swamp', 'dumpyard', 'IOWA']

}

print(word_dict['name'][0])

# function to get the word


def get_word(key, dict):

    keycount = len(word_dict[key]) - 1
    numb = randint(0, keycount)
    word = word_dict[key].pop(numb)
    #print('The word is ', word)
    return word


def create_story():
    local_dictionary = copy.deepcopy(word_dict)
    return story.format(
        get_word('name', local_dictionary),
        get_word('name', local_dictionary),
        get_word('nouns', local_dictionary),
        get_word('adjective', local_dictionary),
        get_word('movie', local_dictionary),
        get_word('verb', local_dictionary),
        get_word('verb', local_dictionary),
        get_word('movie', local_dictionary),
        get_word('name', local_dictionary),
        get_word('verb', local_dictionary),
        get_word('verb', local_dictionary),
        get_word('verb', local_dictionary),
        get_word('nouns', local_dictionary),
        get_word('nouns', local_dictionary),
        get_word('nouns', local_dictionary),
        get_word('nouns', local_dictionary),
        get_word('nouns', local_dictionary),
        get_word('nouns', local_dictionary),
        get_word('movie', local_dictionary))


print("First Sotry")
print(create_story())
