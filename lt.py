from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
from tkinter.ttk import Combobox
from textblob import TextBlob
from tkinter import Label

root = Tk()
root.geometry('600x600')
root.title('Translator')
root.iconbitmap('trans.ico')
root.resizable(False, False)
root.configure(bg='plum')
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
            'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
            'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
            'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
            'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
            'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
            'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
            'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)':
                'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish':
                'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori':
                'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
            'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa',
            'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st',
            'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
            'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
            'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek':
                'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


def tt(event=NONE):
    try:
        word3 = TextBlob(varname1.get())
        lan = word3.detect_language()
        lan_to_dict = languages.get()
        lan_to = lan_dict[lan_to_dict]
        word3 = word3.translate(from_lang=lan, to=lan_to)
        label2.configure(text=word3)
        assert word3
        varname2.set(word3)
    except:
        varname2.set('f')


def main_exit():
    rr = messagebox.askyesno('Notification', 'Are you sure you want to exit?', parent=root)
    if rr:
        root.destroy()


def on_enter_entry1(e):
    entry1['bg'] = 'springgreen'


def on_leave_entry1(e):
    entry1['bg'] = 'MistyRose'


def on_enter_entry2(e):
    entry2['bg'] = 'springgreen'


def on_leave_entry2(e):
    entry2['bg'] = 'MistyRose'


def on_enter_button(e):
    button['bg'] = 'springgreen'


def on_leave_button(e):
    button['bg'] = 'hot pink'


def on_enter_button1(e):
    button1['bg'] = 'springgreen'


def on_leave_button1(e):
    button1['bg'] = 'hot pink'


languages = StringVar()
font_box = Combobox(root, width=30, textvariable=languages, state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300, y=0)

varname1 = StringVar()
entry1 = Entry(root, width=30, textvariable=varname1, font=('times', 15, 'italic bold'))
entry1.place(x=150, y=40)

varname2 = StringVar()
entry2 = Entry(root, width=30, textvariable=varname2, font=('times', 15, 'italic bold'))
entry2.place(x=150, y=100)

label = Label(root, text='Enter words: ', font=('times', 15, 'italic bold'), bg='plum')
label.place(x=5, y=40)

label1 = Label(root, text='Translated: ', font=('times', 15, 'italic bold'), bg='plum')
label1.place(x=5, y=100)

label2 = Label(root, text=' ', font=('times', 15, 'italic bold'), bg='plum')
label2.place(x=10, y=250)

imgbt = PhotoImage(file='click.png')
imgbt1 = PhotoImage(file='exit.png')

imgbt = imgbt.subsample(20, 10)
imgbt1 = imgbt1.subsample(20, 10)

button = Button(root, text='Click', bd=10, bg='hot pink', activebackground='MistyRose2', width='150',
                font=('times', 15, 'italic bold'), image=imgbt, compound=RIGHT, command=tt)
button.place(x=70, y=170)

button1 = Button(root, text='Exit', bd=10, bg='hot pink', activebackground='MistyRose2', width='150',
                 font=('times', 15, 'italic bold'), image=imgbt1, compound=RIGHT, command=main_exit)
button1.place(x=280, y=170)
root.bind('<Return>', tt)

entry1.bind('<Enter>', on_enter_entry1)
entry1.bind('<Leave>', on_leave_entry1)

entry2.bind('<Enter>', on_enter_entry2)
entry2.bind('<Leave>', on_leave_entry2)

button.bind('<Enter>', on_enter_button)
button.bind('<Leave>', on_leave_button)

button1.bind('<Enter>', on_enter_button1)
button1.bind('<Leave>', on_leave_button1)

root.mainloop()
