from tkinter import *
from tkinter import ttk
import random
import queue
import time
from colors import *
# from ref import *

# Importing algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort


compare = 0
iterate = 0
elapse_rt = 0
quick_time = 0
smol_num = 10  # min number of elements in array
large_num = 100  # max number of elements in array
coordinates_list = []
active = False
# global data


# Main window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(900, 700)
window.config(bg=WHITE)

# labels
comparisons = Label(window, text="Comparisons:\t" + str(compare))
iterations = Label(window, text="Iterations:\t" + str(iterate))
elapsed = Label(window, text="Time Elapsed:\t" + str(elapse_rt) + "s")

maxval = DoubleVar()
speed = DoubleVar()
algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort',
             'Merge Sort', 'Quick Sort', 'Heap Sort']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 500
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 450
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
        # canvas.create_text()
        # canvas.create_text(text=data)

    window.update_idletasks()


# Randomly generate array
def generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for i in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, [DARK_GRAY for x in range(len(data))])

# # def manualEntry():


#     # define checkboxes
#     bubble_btn = Button( text="Bubble Sort", command=lambda: label(1))
#     insertion_btn = Button( text="Insertion Sort", command=lambda: label(2))
#     selection_btn = Button( text="Selection Sort", command=lambda: label(3))
#     quick_btn = Button( text="Quick Sort", command=lambda: label(4))
#     heap_btn = Button( text="Heap Sort", command=lambda: label(5))
#     shell_btn = Button( text="Shell Sort", command=lambda: label(6))


#     # code runs on when run button is pressed ...
#     # for each algorithm in the queue, the corresponding stats
#     # are projected under their respective labels
#     def run():
#         global coordinates_list
#         # create_visual()
#         s.set(launch_s.get())
#         index_val = []
#         for element in list(q.queue):
#             for bll in range(len(buttons_test_list)):
#                 if str(element) == buttons_test_list[bll]:
#                     index_val.append(bll)
#         print(index_val)
#         new_cl = coordinates_list
#         for value in range(len(index_val)):
#             coordinates_list = new_cl
#             components[value].invoke()
#             comparison_list[value] = compare
#             iteration_list[value] = iterate
#             time_elapsed_list[value] = elapse_rt
#         update_labels()


def update_comparisons():
    comparisons.configure(text="Comparisons:\t" + str(compare))


def update_iterations():
    iterations.configure(text="Iterations:\t" + str(iterate))


def update_elapsed():
    elapsed.configure(text="Time Elapsed:\t" + str(round(elapse_rt, 3)) + "s")


def start_stop():

    # global active = False
    #global active
    if b1['text'] == 'Start Sorting':
        active = True
        b1.config(text="Pause Sorting")
        sort()
        time.sleep(1)
    # elif b1['text'] == 'Pause Sorting':
    else:
        active = False
        # os.system('')
        time.sleep(1)
        b1.config(text="Start Sorting")
    #     sort()
    # else:
    #     active = True
    #     sort()

    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False


def sort():
    global data
    # global active
    timeTick = int(speedScale.get())
    # if algo_menu.get() == 'Bubble Sort':
    #     bubble_sort(data, drawData, timeTick)
    # elif algo_menu.get() == 'Selection Sort':
    #     selection_sort(data, drawData, timeTick)
    # elif algo_menu.get() == 'Insertion Sort':
    #     insertion_sort(data, drawData, timeTick)
    # elif algo_menu.get() == 'Merge Sort':
    #     merge_sort(data, 0, len(data)-1, drawData, timeTick)
    # elif algo_menu.get() == 'Quick Sort':
    #     quick_sort(data, 0, len(data)-1, drawData, timeTick)
    # elif algo_menu.get() == 'Heap Sort':
    #     heap_sort(data, drawData, timeTick)
    # else:
    #     counting_sort(data, drawData, timeTick)
    if active == False:  # broken should be true
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


### User interface ###
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)


l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(
    UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# l2 = Label(UI_frame, text="Min Value ", bg=WHITE)
# l2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
# E1 = Entry(UI_frame, text="Min Value",textvariable= smol_num).grid(row=1, column=2, padx=10, pady=5, sticky=W)
# E1.insert(ttk.END,'Min Value')

# name_entry = ttk.Entry(UI_frame,textvariable = smol_num,)

# smol_num = ttk.Entry()
# smolnum_verify = IntVar()
# smolnum = ttk.Entry(UI_frame, text="Min Value ", textvariable=smolnum_verify)
# large_num = Label(UI_frame, text="Max Value", bg=WHITE)
# large_num.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# l3 = Label(UI_frame, text="Max Value ", bg='grey')
# l3.grid(row=1, column=3, padx=5, pady=5, sticky=W)
# large_num = Entry(UI_frame)
# large_num.grid(row=1, column=3, padx=5, pady=5, sticky=W)


canvas = Canvas(window, width=800, height=500, bg=WHITE)
canvas.grid(row=3, column=0, columnspan=4, padx=10, pady=5)

b1 = Button(UI_frame, text="Start Sorting", command=start_stop, bg=LIGHT_GRAY)
b1.grid(row=1, column=2, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=1, column=3, padx=5, pady=5)

speedScale = Scale(UI_frame, from_=0.01, to=4.0, length=100, digits=2,
                   resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=4, padx=1, pady=1)

sizeEntry = Scale(UI_frame, from_=5, to=100, resolution=1,
                  orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=1, padx=1, pady=1)


minEntry = Scale(UI_frame, from_=0, to=10, resolution=1,
                 orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=0, column=2, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1,
                 orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=0, column=3, padx=5, pady=5)

window.mainloop()