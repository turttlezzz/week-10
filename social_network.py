class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists.")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = []

            for friend in person.friends:
                friend_names.append(friend.name)

            print(f"{name} is friends with: {', '.join(friend_names)}")


# Test your code here

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate person
network.add_person("Alex")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Print network
network.print_network()

"""
DESIGN MEMO:
Why is a graph the right structure to represent a social network?
A graph is correct because it shows how different people are connected to each other. Each person is represented by a node, and their friendships are the connections between the nodes. In this program, I used a list to keep track of who is friends with who. This way you can see who each person is connected to. 
Why wouldn’t a list or tree work as well for this?
So a list wouldn't work as well because it would make it harder to keep track of all the friendships. If you just had a list of names, that doesn't easily show how everybody is connected. A tree would not work as well because it would be focused on the parent-child structure, which wouldn't really make sense when trying to connect friendships. 
What performance or structural trade-offs did you notice when adding friends or printing the network?
Adding friends is very easy; all you have to do is use append. Printing the network, however, requires going through every single person and all of their friends. As the network size increases, there naturally is more information to go through. Using a dictionary also makes it easier to find people by their names instead of searching through a list.
""" 