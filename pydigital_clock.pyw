from tkinter import Label, mainloop, Tk
from datetime import datetime

# Starts the main frame
root = Tk()
root.title("Digital Clock")
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

"""
  returns a colon if the actual second is even,
  and returns a white space if actual second is odd
"""
def dot(current_time):
  dots = [":", " "]
  seconds = datetime.strftime(current_time, "%S")
  if (int(seconds) % 2) == 0:
    dt_1 = str(dots[0])
    return(dt_1)
  else:
    dt_2 = str(dots[1])
    return(dt_2)

"""
  get current date and current time formated like this:
  MONDAY, JAN 21
"""
def time():
  now = datetime.now()
  string = datetime.strftime(
    now, "%A, %b %d\n%I{0}%M{1}%S %p".format(dot(now), dot(now))
  ) 
  label_time.config(text=string, justify="center")
  label_time.after(1000, time)


label_time = Label(
  root,
  font=("digital numbers", 65),
  background="#000000",
  foreground="#ffffff",
  width=width,
  height=height
)
label_time.pack(anchor="center")
label_time.master.overrideredirect(True)
label_time.master.wm_attributes("-transparentcolor","#000000")
label_time.master.lift()


if __name__ == "__main__":
  time()
  root.eval('tk::PlaceWindow . center')
  root.overrideredirect(True)
  root.overrideredirect(False)
  root.attributes("-fullscreen", True)
  mainloop()