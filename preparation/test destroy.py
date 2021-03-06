
##  Turing Machine Visual - a software developed to simulate Turing machine
##    Copyright (C) 2017 Artemii Yanushevskyi
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU Affero General Public License as
##    published by the Free Software Foundation, either version 3 of the
##    License, or (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU Affero General Public License for more details.
##
##    You should have received a copy of the GNU Affero General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##    You can contact me by email: argoniton@gmail.com
##
##  This is BETA 6 of this application.



##  Turing Machine Visual - a software developed to simulate Turing machine
##    Copyright (C) 2017 Artemii Yanushevskyi
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU Affero General Public License as
##    published by the Free Software Foundation, either version 3 of the
##    License, or (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU Affero General Public License for more details.
##
##    You should have received a copy of the GNU Affero General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##    You can contact me by email: argoniton@gmail.com
##
##  This is BETA 6 of this application.


import tkinter as tk

m = tk.Tk()
sv = tk.StringVar()
sv.set('jhgf')
f = tk.Entry(m, textvariable=sv)
f.pack()

def d():
    m = tk.Tk()
    sv = tk.StringVar()
    sv.set('jhgf')
    f = tk.Entry(m, textvariable=sv)
    f.pack()

    def close():
        m.destroy()
        print('    window is closed')

    def hide():
        m.withdraw()
        print('    window is hidden')

    bclose = tk.Button(m)
    bclose['command'] = close
    bclose['text'] = 'close'
    bclose.pack()

    bhide = tk.Button(m)
    bhide['command'] = hide
    bhide['text'] = 'hide'
    bhide.pack()

    tk.mainloop()

    
d()
print('program is done') # you will see that if all windows are destroyed


