"""
Module for discovering classes
"""

from notebook import Notebook

def main():
    """
    None -> NOne
    Main program function
    """
    print("\tAnalising object")
    print("Creating obj 'notebook_obj'...")
    notebook_obj = Notebook()

    print("Type of notebook_obj: ", type(notebook_obj))

    print("Is notebook_obj is obj? (isinstance): ", isinstance(notebook_obj, object))

    print("dir of notebook_obj:")
    print(dir(notebook_obj))

    print("\n----------------------------------------------------------\n")

    print("Type of Notebook: ", type(Notebook))

    print("Is Notebook is obj? (isinstance): ", isinstance(Notebook, object))
    print("Is Notebook is class? (isinstance): ", isinstance(Notebook, type))

    print("dir of Notebook:")
    print(dir(Notebook))

    print("\n----------------------------------------------------------\n")

    print("Attributes of this class:")
    print("notebook_obj.notes: ", notebook_obj.notes)
    print("Appending some data here...")
    notebook_obj.new_note("First note")
    print("Again, notebook_obj.notes: ", notebook_obj.notes)
    print("Go deeper, notebook_obj.notes[0].memo: ",
          notebook_obj.notes[0].memo, "; notebook_obj.notes[0].id: ",
          notebook_obj.notes[0].id)
    print("so, attributes = some variables where data can be saved")

    print("\n----------------------------------------------------------\n")

    print("Using methods of this obj:")
    print("_find_note(1): ", notebook_obj._find_note(1))
    print("modify_memo(1, 'Second memo'): ", notebook_obj.modify_memo(1, 'Second memo'))
    print("Again, notebook_obj.notes[0].memo: ", notebook_obj.notes[0].memo)
    print("new_note('Third memo'): ", notebook_obj.new_note('Third memo'))
    print("Here, notebook_obj.notes[1].memo: ", notebook_obj.notes[1].memo)
    print("search(''): ", notebook_obj.search(''))
    print("So, methods are just funcion performed on class obj")
    print("type(notebook_obj._find_note): ", type(notebook_obj._find_note))
    print("dir(notebook_obj._find_note): ", dir(notebook_obj._find_note))

    print("\n----------------------------------------------------------\n")

    print("Discovering self:")
    print('notebook_obj.print_self() (this is my own written method to show what is self): ',
          notebook_obj.print_self())
    print("And just notebook_obj:", notebook_obj)
    print('notebook_obj.print_self() == notebook_obj: ', notebook_obj.print_self() == notebook_obj)
    print("As you see, they are identical, so self - is just link on the current object of class")

    print("\n----------------------------------------------------------\n")

    print("Discovering method __init__")
    print("dir(Notebook.__init__): ", dir(Notebook.__init__))
    print("notebook_obj.__init__():", notebook_obj.__init__())
    print("notebook_obj.notes: ", notebook_obj.notes)
    print("So __init__ generates (or re-generates) obj of this class")

    print("\n----------------------------------------------------------\n")

    print("Discovering method __str__")
    print("dir(Notebook.__str__): ", dir(Notebook.__str__))
    print("notebook_obj.__str__():", notebook_obj.__str__())
    print("notebook_obj: ", notebook_obj)
    print("As we see, be have basic __str__ method in this class. \
    Developer did not added pretty - looking form of showing this obj")
    print("Lets try to do it...")
    print("Creating obj 'notebook_obj'...")
    notebook_obj = Notebook()
    notebook_obj.new_note("First note")
    print("fake_str(notebook_obj): ", fake_str(notebook_obj))
    print("So, __str__ is just pretty - looking form of showing obj")


def fake_str(noootebook):
    """
    Notebook -> str
    This func simulates a __str__ method
    """
    return "Note id: {}, note memo: {}".format(noootebook.notes[0].id, noootebook.notes[0].memo)

if __name__ == '__main__':
    main()
