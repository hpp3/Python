#a script written to test me on AP Latin vocabulary relating to potery analysis

import random as r
import pickle as p

terms = {"allegory":"a sustained metaphor", 
     "alliteration":"repetition of the same letter",
     "anaphora":"repetition of the same word to begin successive phrases",
     "anastrophe":"placing the preposition after the word it governs",
     "antithesis":"placing contrasted pairs in like order",
     "apostrophe":"a sudden break to address an absent person or thing",
     "aposiopesis":"an abrupt pause in a sentence",
     "assonance":"repetition of the same vowel sound",
     "asyndeton":"omission of connectives",
     "chiasmus":"an arrangement of words in an inverser order (ABBA)",
     "climax":"series of words with increasing force",
     "ecphrasis":"digression describing a place connected at end to main narrative by hic or huc",
     "ellipsis":"omission of words grammaticaly necessary for brevity",
     "enjambment":"closely related words of sentence fall into different line",
     "euphemism":"a mild expression used for an unpleasant one",
     "hendiadys":"one idea expressed by two nouns connected by a conjunction",
     "hyperbaton":"inversion of normal order of words for emphasis",
     "hyperbole":"exaggeration for rhetorical effect",
     "hysteron-proteron":"reversal of the natural or logical order of ideas",
     "irony":"words with meaning contrary to the situation",
     "juxtaposition":"setting words side-by-side for contrast or emphasis",
     "litotes":"affirmative expressed by the negative of its opposite",
     "metaphor":"an implied comparison",
     "metonymy":"use of one word for another that it suggests",
     "onomatopoeia":"adaptation of sound to sense in the use of words",
     "oxymoron":"use of contradictory terms",
     "patronym":"reference to the man as the son of his father",
     "periphrasis":"an imaginative circumlocution",
     "personification":"treatment of inanimate things as if they were persons",
     "pleonasm":"use of unnecessary words",
     "polysyndeton":"frequent repetition of the connective with several words",
     "polyptoton":"unnecessary use of conjunctions",
     "praeteritio":"pretense of omitting something for emphasis",
     "prolepsis":"use of a words before action makes it logically appropriate",
     "prosopopoeia":"assumption of another's persona for rhetorical or dramatic effect",
     "simile":"an expressed comparision",
     "synchisis":"interlocking word order (ABAB)",
     "syncope":"loss of a syllable within a word",
     "synecdoche":"use of a part for the whole",
     "synizesis":"2 syllables combined into one for scansion",
     "tmesis":"separation of the two parts of a compound word",
     "transferred epithet":"device of emphasis; transferal of a characteristic of a thing to another thing closely associated with it",
     "tricolon crescens":"3-part increase of emphasis or enlargement of meaning",
     "verbal irony":"stating the opposite of what is meant",
     "zeugma":"use of verb or adjective with 2 words to only one of which it is strictly appropriate"
     }

stats = {"allegory":[0,0], 
     "alliteration":[0,0],
     "anaphora":[0,0],
     "anastrophe":[0,0],
     "antithesis":[0,0],
     "apostrophe":[0,0],
     "aposiopesis":[0,0],
     "assonance":[0,0],
     "asyndeton":[0,0],
     "chiasmus":[0,0],
     "climax":[0,0],
     "ecphrasis":[0,0],
     "ellipsis":[0,0],
     "enjambment":[0,0],
     "euphemism":[0,0],
     "hendiadys":[0,0],
     "hyperbaton":[0,0],
     "hyperbole":[0,0],
     "hysteron-proteron":[0,0],
     "irony":[0,0],
     "juxtaposition":[0,0],
     "litotes":[0,0],
     "metaphor":[0,0],
     "metonymy":[0,0],
     "onomatopoeia":[0,0],
     "oxymoron":[0,0],
     "patronym":[0,0],
     "periphrasis":[0,0],
     "personification":[0,0],
     "pleonasm":[0,0],
     "polysyndeton":[0,0],
     "polyptoton":[0,0],
     "praeteritio":[0,0],
     "prolepsis":[0,0],
     "prosopopoeia":[0,0],
     "simile":[0,0],
     "synchisis":[0,0],
     "syncope":[0,0],
     "synecdoche":[0,0],
     "synizesis":[0,0],
     "tmesis":[0,0],
     "transferred epithet":[0,0],
     "tricolon crescens":[0,0],
     "verbal irony":[0,0],
     "zeugma":[0,0]
     }

recent = []




def save():
    f = open("latin-data.txt" , "w")
    p.dump(stats, f)
    f.close()

def randterm():
    while True:
        choice = r.choice(terms.keys())

        if recent.count(choice) == 2:
            if r.randint(0,2):
                continue
        elif choice in recent:
            if r.randint(0,1):
                continue

        if stats[choice][0] > 3:
            if r.randint(1,stats[choice][0]) <= stats[choice][1]:
                continue

        return choice

def ask(recent):
    choice = randterm()

    print ("Your term is: %s" % choice)

    raw_input("Your guess: ")

    ans = raw_input ("%s means %s. Did you guess right? " % (choice, terms[choice]))
    if ans != 'n' and ans != 'N':
        stats[choice][1]+=1
    stats[choice][0]+=1
    recent.append(choice)
    if len(recent) > 5:
        recent = recent[1:]
    print ("%s correct %d out of %d times (%f%%)" % (choice,stats[choice][1],stats[choice][0],stats[choice][1]/float(stats[choice][0])*100))

try:
    f = open("latin-data.txt")
    stats = p.load(f)
except:
    pass
while True:
    ask(recent)
