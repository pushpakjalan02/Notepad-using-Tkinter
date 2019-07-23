import tkinter
import os
import webbrowser
from tkinter.filedialog import *
from tkinter import ttk

window = tkinter.Tk()
window.title('Untitled.txt - Notepad')

menu = tkinter.Menu(window)

text_area = tkinter.Text(window, state = NORMAL, undo = True)    

file_name = None

prev_find_string = ""
start_from = 0
previous_check_box_state = False     # True means checked state

def new_function():
    
    global window, menu, text_area, file_name
    
    file_name = None
    text_area.delete(1.0, tkinter.END)
    window.title("Untitled.txt - Notepad")
    return

def open_function():
    
    global window, menu, text_area, file_name
    
    file_name = askopenfilename(defaultextension = ".txt", filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
    
    if(file_name == ""):
        file_name = None
    else:
        window.title(os.path.basename(file_name) + " - Notepad")
        text_area.delete(1.0, tkinter.END)
        open_file = open(file_name, "r")
        text_area.insert(1.0,open_file.read()[:-1])
        open_file.close()
    return

def save_function():
    
    global window, menu, text_area, file_name
    
    if(file_name == None):
        file_name = asksaveasfilename(initialfile="Untitled.txt", defaultextension = ".txt", filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
        if(file_name == ""):
            file_name = None
    
    if(file_name != None):
        save_file = open(file_name, "w")
        save_file.write(text_area.get(1.0, tkinter.END))
        save_file.close()
        window.title(os.path.basename(file_name) + " - Notepad")
        return

def save_as_function():
    
    global window, menu, text_area, file_name
    
    temp_file_name = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes = [("All Files","*.*"),("Text Documents",".txt")])
    
    if(temp_file_name != ""):
        file_name = temp_file_name
        save_file = open(file_name, "w")
        save_file.write(text_area.get(1.0, tkinter.END))
        save_file.close()
        window.title(os.path.basename(file_name) + " - Notepad")
    return

def copy():
    
    global window, menu, text_area, file_name
    
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
    global window, menu, text_area, file_name
    
    try:
        copy()
        text_area.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    
    except:
        pass
    
    finally:
        return

def paste():
    global window, menu, text_area, file_name
    
    paste_val = text_area.clipboard_get()
    try:
        if len(tkinter.SEL) > 0:
            text_area.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    
    except:
        pass
    
    finally:
        text_area.insert(tkinter.INSERT, paste_val)

def select_all():
    length = "1." + str(len(text_area.get("1.0", tkinter.END)))
    text_area.tag_add(tkinter.SEL, "1.0", length) 
    text_area.focus_set()
    return  

def find_in_content(find_text_box, find_window, check_var):
    global text_area, prev_find_string, start_from, previous_check_box_state
    
    try:
        if len(tkinter.SEL) > 0:
            text_area.tag_remove(tkinter.SEL, "1.0", tkinter.END)
    
    except:
        pass
    
    finally:
        string_to_find = find_text_box.get()
        if(prev_find_string != string_to_find or check_var != previous_check_box_state):
            start_from = 0
            prev_find_string = string_to_find
            previous_check_box_state = check_var
        content = text_area.get("1.0", tkinter.END)
        if(check_var == True):
            pass
        else:
            content = content.lower()
            string_to_find = string_to_find.lower()
        start_from = content.find(string_to_find, start_from)
        if(start_from == -1):
            start_from = 0
            start_from = content.find(string_to_find, start_from)
        if(start_from != -1):
            focus_start = "1." + str(start_from)
            focus_end = "1." + str(start_from + len(string_to_find))
            text_area.tag_add(tkinter.SEL, focus_start, focus_end)
            text_area.mark_set(tkinter.INSERT, focus_end)
        window.focus_force()
        text_area.focus_set()
        start_from += 1
        return

def find_function():
    
    find_window = tkinter.Tk()
    find_window.geometry('350x100')
    find_window.resizable(0, 0)
    find_window.title('Find')
    
    find_label = tkinter.Label(find_window, text = 'Find:')
    find_label.place(anchor = tkinter.W, relx = 0.02, rely = 0.2, relheight = 0.2)
    
    find_text_box = tkinter.Entry(find_window)
    find_text_box.place(anchor = tkinter.W, relx = 0.20, rely = 0.2, relheight = 0.22, relwidth = 0.45)
    
    find_text_button2 = tkinter.Button(find_window, text = 'Cancel', command = find_window.destroy)
    find_text_button2.place(anchor = tkinter.W, width = 100, relx = 0.70, rely = 0.5, relheight = 0.22)
    
    match_case_check = ttk.Checkbutton(find_window, text = 'Match Case')
    match_case_check.state(['!alternate'])
    match_case_check.state(['!selected'])
    match_case_check.place(anchor = tkinter.W, width = 100, relx = 0.02, rely = 0.8, relheight = 0.22)
    
    find_text_button = tkinter.Button(find_window, text = 'Find Next', command = lambda: find_in_content(find_text_box, find_window, match_case_check.instate(['selected'])))
    find_text_button.place(anchor = tkinter.W, width = 100, relx = 0.70, rely = 0.2, relheight = 0.22)
    
    find_window.mainloop
    return

def replace_in_content(replace_text_box, replace_window):
    global text_area, start_from
    
    try:
        if len(tkinter.SEL) > 0:
            text_area.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
            replace_value = replace_text_box.get()
            text_area.insert(tkinter.INSERT, replace_value)
            cursor_pos = int(text_area.index(tkinter.INSERT)[2:])
            focus_start = "1." + str(cursor_pos - len(replace_value))
            focus_end = "1." + str(cursor_pos)
            text_area.tag_add(tkinter.SEL, focus_start, focus_end)
            text_area.mark_set(tkinter.INSERT, focus_end)
            window.focus_force()
            text_area.focus_set()
            start_from = cursor_pos - len(replace_value) + 1
    
    except:
        pass
    
    finally:
        pass
    return

def replace_function():
    
    replace_window = tkinter.Tk()
    replace_window.geometry('350x100')
    replace_window.resizable(0, 0)
    replace_window.title('Replace')
    
    find_label = tkinter.Label(replace_window, text = 'Find:')
    find_label.place(anchor = tkinter.W, relx = 0.02, rely = 0.2, relheight = 0.2)
    
    find_text_box = tkinter.Entry(replace_window)
    find_text_box.place(anchor = tkinter.W, relx = 0.20, rely = 0.2, relheight = 0.22, relwidth = 0.45)
    
    replace_label = tkinter.Label(replace_window, text = 'Replace:')
    replace_label.place(anchor = tkinter.W, relx = 0.02, rely = 0.5, relheight = 0.2)
    replace_text_box = tkinter.Entry(replace_window)
    replace_text_box.place(anchor = tkinter.W, relx = 0.20, rely = 0.5, relheight = 0.22, relwidth = 0.45)
    
    cancel_button = tkinter.Button(replace_window, text = 'Cancel', command = replace_window.destroy)
    cancel_button.place(anchor = tkinter.W, width = 100, relx = 0.70, rely = 0.8, relheight = 0.22)
    
    match_case_check_button = ttk.Checkbutton(replace_window, text = 'Match Case')
    match_case_check_button.state(['!alternate'])
    match_case_check_button.state(['!selected'])
    match_case_check_button.place(anchor = tkinter.W, width = 100, relx = 0.02, rely = 0.8, relheight = 0.22)
    
    find_next_button = tkinter.Button(replace_window, text = 'Find Next', command = lambda: find_in_content(find_text_box, replace_window, match_case_check_button.instate(['selected'])))
    find_next_button.place(anchor = tkinter.W, width = 100, relx = 0.70, rely = 0.2, relheight = 0.22)
    
    replace_button = tkinter.Button(replace_window, text = 'Replace', command = lambda: replace_in_content(replace_text_box, replace_window))
    replace_button.place(anchor = tkinter.W, width = 100, relx = 0.70, rely = 0.5, relheight = 0.22)
    replace_window.mainloop
    return

def goto_content(line_no):
    global text_area, window
    
    # Format of 2nd parameter is: ("%d.%d" % (line, column))
    parameter = line_no + ".0"
    text_area.mark_set(tkinter.INSERT, parameter)
    
    window.focus_force()
    text_area.focus_set()
    return

def goto_function():
    
    goto_window = tkinter.Tk()
    goto_window.geometry('350x100')
    goto_window.resizable(0, 0)
    goto_window.title('Go To')
    
    line_no_label = tkinter.Label(goto_window, text = 'Line No. :')
    line_no_label.place(anchor = tkinter.W, relx = 0.02, rely = 0.2, relheight = 0.2)
    line_no_text_box = tkinter.Entry(goto_window)
    line_no_text_box.place(anchor = tkinter.W, relx = 0.20, rely = 0.2, relheight = 0.22, relwidth = 0.45)
    
    cancel_button = tkinter.Button(goto_window, text = 'Cancel', command = goto_window.destroy)
    cancel_button.place(anchor = tkinter.W, width = 100, relx = 0.70, rely = 0.5, relheight = 0.22)
    
    goto_button = tkinter.Button(goto_window, text = 'Go', command = lambda: goto_content(line_no_text_box.get()))
    goto_button.place(anchor = tkinter.W, width = 100, relx = 0.70, rely = 0.2, relheight = 0.22)
    
    goto_window.mainloop
    return

def file_menu(file):
    file.add_command(label='New', command = new_function)
    file.add_command(label='Open', command = open_function)
    file.add_command(label='Save', command = save_function)
    file.add_command(label='Save As', command = save_as_function)
    file.add_command(label='Close', command = window.destroy)
    return

def edit_menu(edit):
    edit.add_command(label='Undo', command = text_area.edit_undo)
    edit.add_command(label='Redo', command = text_area.edit_redo)
    
    edit.add_separator()
    
    edit.add_command(label='Cut', command = cut)
    edit.add_command(label='Copy', command = copy)
    edit.add_command(label='Paste', command = paste)
    edit.add_command(label='Select All', command = select_all)
    
    edit.add_separator()
    
    edit.add_command(label='Find', command = find_function)
    edit.add_command(label='Replace', command = replace_function)
    edit.add_command(label='Go To', command = goto_function)
    return

def link_to(url):
    webbrowser.open_new(url)
    return

def help_menu(help_menu_option):
    help_menu_option.add_command(label='Help', command = lambda: link_to("https://www.google.com"))
    
    help_menu_option.add_separator()
    
    help_menu_option.add_command(label='About', command = lambda: link_to("https://www.facebook.com"))
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
    global window, menu, text_area, file_name
    
    main_menu(menu)
    
    text_area.pack(expand = True, fill = 'both')
    
    window.config(menu=menu)
    window.mainloop()

if __name__ == '__main__':
    main()