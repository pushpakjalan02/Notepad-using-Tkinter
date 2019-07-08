import tkinter

window = tkinter.Tk()
window.title('Notepad by Pushpak')

menu = tkinter.Menu(window)

text_area = tkinter.Text(window, undo = True)    

def copy():
    text_area.clipboard_clear()
    try:
        copy_val = text_area.selection_get()
        #   copy_val = text_area.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text_area.clipboard_append(copy_val)
    except:
        pass
    finally:
        return

def cut():
    try:
        copy()
        text_area.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    except:
        pass
    finally:
        return

def paste():
    paste_val = text_area.clipboard_get()
    try:
        if len(tkinter.SEL) > 0:
            text_area.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    except:
        pass
    finally:
        text_area.insert(tkinter.INSERT, paste_val)

def file_menu(file):
    file.add_command(label='New')
    file.add_command(label='Open')
    file.add_command(label='Save')
    file.add_command(label='Save As')
    file.add_command(label='Close')
    return

def edit_menu(edit):
    edit.add_command(label='Undo', command = text_area.edit_undo)
    edit.add_command(label='Redo', command = text_area.edit_redo)
    edit.add_separator()
    edit.add_command(label='Cut', command = cut)
    edit.add_command(label='Copy', command = copy)
    edit.add_command(label='Paste', command = paste)
    edit.add_command(label='Select All')
    edit.add_separator()
    edit.add_command(label='Find')
    edit.add_command(label='Find Next')
    edit.add_command(label='Replace')
    edit.add_command(label='Go To')
    return

def help_menu(help_menu_option):
    help_menu_option.add_command(label='Help')
    help_menu_option.add_separator()
    help_menu_option.add_command(label='About')
    return

def main_menu(menu):
    
    file = tkinter.Menu(menu, tearoff = 0)
    file_menu(file)
    
    edit = tkinter.Menu(menu, tearoff = 0)
    edit_menu(edit)
    
    help_menu_option = tkinter.Menu(menu, tearoff = 0)
    help_menu(help_menu_option)
    
    menu.add_cascade(label = 'File', menu = file)
    menu.add_cascade(label = 'Edit', menu = edit)
    menu.add_cascade(label = 'Help', menu = help_menu_option)
    return

def main():
    main_menu(menu)
    
    text_area.pack(expand = True, fill = 'both')
    
    window.config(menu=menu)
    window.mainloop()

if __name__ == '__main__':
    main()