import gui
import commands

command = gui.chose_func()
if command == '1':
    commands.add_contact()
if command == '2':
    commands.find_contact()
if command == '3':
    commands.delete_contact()
if command == '4':
    commands.show_all_contacts()