from pyorg import add_todo, Location


if __name__ == "__main__":
    location = Location(heading="Work")
    print "Storing todo at {}".format(location)
    add_todo("./test.org", "My test todo", location)
