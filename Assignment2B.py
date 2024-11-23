animal = input("Enter a name of an animal: ")
mammals = "dog", "cat", "human", "whale"
birds = "eagle", "parrot", "penguin", "sparrow"
reptiles = "snake", "lizard", "crocodile", "turtle"
fish = "salmon", "goldfish", "shark", "tuna"
amphibians = "frog", "toad", "salamander", "newt"

if animal in mammals:
    print('The animal is a Mammal.')
elif animal in birds:
    print('The animal is a Bird.')
elif animal in reptiles:
    print('The animal is a Reptile')
elif animal in fish:
    print('The animal is a Fish.')
elif animal in amphibians:
    print('The animal is a Amphibian.')
else:
    print('Unknown category.')
