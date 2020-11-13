import datetime
import sys

last_id = 0

class Note:
    def __init__(self, memo):
        self.memo = memo
        self.cdate = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo):
        self.notes.append(Note(memo))
        print(f'{memo} is added to the Notebook')
        
    def _find_note(self, id):
        for note in self.notes:
            if str(note.id) == str(id):
                return note
        return None

    def modify_memo(self, id, memo):
        note = self._find_note(id)
        if note:
            note.memo = memo
            return True
        return False

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.actions = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        print(''' 
Notebook Menu
1. Show all notes
2. Search notes
3. Add a note
4. Modify a note
5. Quit
        ''')

    def run(self):
        while True:
            self.display_menu()
            choice = input('Select a Item: ')
            action = self.actions.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid option')

    def show_notes(self, notes = None):
        if notes is None:
            notes = self.notebook.notes

        for note in notes:
            print(f'ID:{note.id} Memo:{note.memo}')

    def search_notes(self):
        filter = input('Enter a filter: ')
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input('Add a memory: ')
        self.notebook.new_note(memo)

    def modify_note(self):
        id = input('Put the Note ID: ')
        memo = input('Add a memory: ')
        self.notebook.modify_memo(id, memo)

    def quit(self):
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()