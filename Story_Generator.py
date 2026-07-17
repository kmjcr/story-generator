while True:
    story_elements = {
        "connectors": ["and", "but then", "and then", "right after that", "meanwhile", "suddenly", "later on", "in the end"],
        "pronouns_male": ["he", "him", "his", "himself", "they", "them", "their", "themselves"],
        "pronouns_female": ["she", "her", "hers", "herself", "they", "them", "their", "themselves"],
        "objectives_horror": ["escape the haunted house", "survive the night", "find the hidden treasure", "uncover the dark secret", "defeat the evil spirit"],
        "objectives_drama": ["reconcile with a loved one", "overcome personal struggles", "achieve a lifelong dream", "find true love", "make amends for past mistakes"],
        "objectives_comedy": ["win the talent show", "pull off a hilarious prank", "get the perfect date", "survive a series of awkward situations", "become the life of the party"],
        "objectives_fantasy": ["defeat the dragon", "find the magical artifact", "rescue the kidnapped prince/princess", "unite the warring kingdoms", "discover a hidden realm"],
        "settings_horror": ["a dark and stormy night", "an abandoned asylum", "a creepy forest", "a haunted mansion", "a desolate graveyard"],
        "settings_drama": ["a bustling city", "a small town", "a family home", "a high school", "a hospital"],
        "settings_comedy": ["a college campus", "a quirky neighborhood", "a comedy club", "a chaotic office", "a family reunion"],
        "settings_fantasy": ["a mystical forest", "a magical kingdom", "an enchanted castle", "a hidden village", "a floating island"],
        "characters_horror": ["a terrified teenager", "a brave ghost hunter", "a mysterious stranger", "a cursed child", "an evil spirit"],
        "characters_drama": ["a struggling artist", "a conflicted parent", "a determined athlete", "a heartbroken lover", "a wise mentor"],
        "characters_comedy": ["a clumsy comedian", "a witty best friend", "a quirky neighbor", "a bumbling detective", "a mischievous child"],
        "characters_fantasy": ["a noble knight", "a cunning thief", "a powerful wizard", "a brave princess", "a loyal companion"]
    }

    import random 

    Connectors = random.choice(story_elements["connectors"])
    pronouns_M = random.choice(story_elements["pronouns_male"])
    pronouns_F = random.choice(story_elements["pronouns_female"])
    objectives_HORROR = random.choice(story_elements["objectives_horror"])
    objectives_DRAMA = random.choice(story_elements["objectives_drama"])
    objectives_COMEDY = random.choice(story_elements["objectives_comedy"])
    objectives_FANTASY = random.choice(story_elements["objectives_fantasy"])
    settings_HORROR = random.choice(story_elements["settings_horror"])
    settings_DRAMA = random.choice(story_elements["settings_drama"])
    settings_COMEDY = random.choice(story_elements["settings_comedy"])
    settings_FANTASY = random.choice(story_elements["settings_fantasy"])
    characters_HORROR = random.choice(story_elements["characters_horror"])
    characters_DRAMA = random.choice(story_elements["characters_drama"])
    characters_COMEDY = random.choice(story_elements["characters_comedy"])
    characters_FANTASY = random.choice(story_elements["characters_fantasy"])

    print("Welcome to the story generator!")
    print("Please select a genre for your story:")
    print("1. Horror")
    print("2. Drama")
    print("3. Comedy")
    print("4. Fantasy")

    genre = input("Please select the genre you want: ")

    if genre == "1":
        print(f"Once upon a time, {characters_HORROR} found themselves in {settings_HORROR}. Their goal was to {objectives_HORROR}. {Connectors}, they faced many challenges and terrifying encounters. In the end, they managed to {objectives_HORROR} and survived the night.")
    elif genre == "2":
        print(f"Once upon a time, {characters_DRAMA} found themselves in {settings_DRAMA}. Their goal was to {objectives_DRAMA}. {Connectors}, they faced many challenges and emotional struggles. In the end, they managed to {objectives_DRAMA} and found peace.")
    elif genre == "3":
        print(f"Once upon a time, {characters_COMEDY} found themselves in {settings_COMEDY}. Their goal was to {objectives_COMEDY}. {Connectors}, they faced many humorous situations and comedic mishaps. In the end, they managed to {objectives_COMEDY} and had a great time.")
    elif genre == "4":
        print(f"Once upon a time, {characters_FANTASY} found themselves in {settings_FANTASY}. Their goal was to {objectives_FANTASY}. {Connectors}, they faced many magical challenges and adventures. In the end, they managed to {objectives_FANTASY} and lived happily ever after.")
    else:
        print("Invalid genre selection. Please choose a number between 1 and 4.")
