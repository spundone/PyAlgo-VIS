from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort


# Main window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg=WHITE)

maxval = DoubleVar()
speed = DoubleVar()
algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort',
             'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
s = Scale(window, label='Size of Array', variable=maxval,
          orient=HORIZONTAL, length=250, from_=10, to=500, bg=WHITE)
s.place(x=20, y=15)
s = Scale(window, label='speed', variable=speed, orient=HORIZONTAL,
          resolution=0.001, length=250, from_=0.001, to=3, bg=WHITE)
s.place(x=550, y=15)

# # components in launch_test window
# instruct_label = Label(test_page, text="Choose Three Algorithms:")
# run_btn = Button(test_page, text="Run", command=run)
# launch_s = Scale(test_page, orient=HORIZONTAL, length=125, from_=c, to=d)
# launch_s.place(x=300, y=16)

# # layout for launch_test_windows
# run_btn.place(x=450, y=32)
# instruct_label.place(x=48, y=36)

# Drawing the numerical array as bars


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    for i in range(0, int(maxval.get())):
        random_value = random.randint(1, 250)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


def sort():
    global data
    timeTick = speed.get()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)


### User interface ###
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(
    UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)


canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)


window.mainloop()
