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
from algorithms.countingSort import counting_sort

compare = 0
iterate = 0
elapse_rt = 0
quick_time = 0
smol_num = 10   #min number of elements in array
large_num = 250 #max number of elements in array
coordinates_list = []
active = False
# global data

# Main window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(900, 600)
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
             'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
s = Scale(window, label='Size of Array', variable=maxval,
          orient=HORIZONTAL, length=200, from_= smol_num, to= large_num, bg=WHITE)
s.place(x=10, y=10)
s = Scale(window, label='Speed (More is Slower)', variable=speed, orient=HORIZONTAL,
          resolution=0.001, length=200, from_=0.001, to=3, bg=WHITE)
s.place(x=610, y=10)

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
    canvas_height = 500
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 490
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        # canvas.create_text()
        #canvas.create_text(text=data)

    window.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    for i in range(0, int(maxval.get())):
        random_value = random.randint(1, 100)
        data.append(random_value)

    drawData(data, [DARK_GRAY for x in range(len(data))])

# def manualEntry():

def launch_test():
    test_page = Tk()
    test_page.title("Test")
    test_page.geometry("533x262+575+348")

    q = queue.Queue(maxsize=3)

    iteration_list = [0, 0, 0]
    comparison_list = [0, 0, 0]
    time_elapsed_list = [0, 0, 0]

    # apply values and data to
    # each of the three labels
    def update_labels():
        cont = 2
        for element in list(q.queue):
            label_list[cont].configure(
                text=element
                + "\n"
                + str(iteration_list[cont])
                + "\n"
                + str(comparison_list[cont])
                + "\n"
                + str(round(time_elapsed_list[cont], 3))
                + "s"
            )
            print(iteration_list)
            cont -= 1

    def label(x):
        idx = x
        if q.qsize() <= 2:
            q.put(buttons_test_list[idx])
        elif q.qsize() >= 3:
            while q.qsize() > 2:
                q.get()
            q.put(buttons_test_list[idx])
        print(q.qsize())
        update_labels()

    # define checkboxes
    bubble_btn = Button(test_page, text="Bubble Sort", command=lambda: label(1))
    insertion_btn = Button(test_page, text="Insertion Sort", command=lambda: label(2))
    selection_btn = Button(test_page, text="Selection Sort", command=lambda: label(3))
    quick_btn = Button(test_page, text="Quick Sort", command=lambda: label(4))
    heap_btn = Button(test_page, text="Heap Sort", command=lambda: label(5))
    shell_btn = Button(test_page, text="Shell Sort", command=lambda: label(6))

    # button list
    btn_list = [
        bubble_btn,
        insertion_btn,
        selection_btn,
        quick_btn,
        heap_btn,
        shell_btn,
    ]

    # place checkboxes
    y_prime_prime = 64
    for btn in range(len(btn_list)):
        btn_list[btn].place(x=48, y=y_prime_prime)
        y_prime_prime += 32

    # three labels
    label_one = Label(test_page)
    label_two = Label(test_page)
    label_three = Label(test_page)

    # label list
    label_list = [label_one, label_two, label_three]

    lbl_k = 100
    for lbl in range(len(label_list)):
        label_list[lbl].place(x=200 + (lbl_k * lbl), y=96)

    # code runs on when run button is pressed ...
    # for each algorithm in the queue, the corresponding stats
    # are projected under their respective labels
    def run():
        global coordinates_list
        # create_visual()
        s.set(launch_s.get())
        index_val = []
        for element in list(q.queue):
            for bll in range(len(buttons_test_list)):
                if str(element) == buttons_test_list[bll]:
                    index_val.append(bll)
        print(index_val)
        new_cl = coordinates_list
        for value in range(len(index_val)):
            coordinates_list = new_cl
            components[value].invoke()
            comparison_list[value] = compare
            iteration_list[value] = iterate
            time_elapsed_list[value] = elapse_rt
        update_labels()

    # components in launch_test window
    instruct_label = Label(test_page, text="Choose Three Algorithms:")
    run_btn = Button(test_page, text="Run", command=run)
    launch_s = Scale(test_page, orient=HORIZONTAL, length=125, from_=smol_num, to=large_num)
    launch_s.place(x=300, y=16)

    # layout for launch_test_windows
    run_btn.place(x=450, y=32)
    instruct_label.place(x=48, y=36)

    # buttons test list
    buttons_test_list = [
        "null",
        "Bubble Sort",
        "Insertion Sort",
        "Selection Sort",
        "Quick Sort",
        "Heap Sort",
        "Shell Sort",
    ]

    # mainloop
    test_page.mainloop()


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
        sort()
        b1.config(text="Pause Sorting")
        # time.sleep(1)
    else:
        active = False

        b1.config(text="Start Sorting")
        # b1.config(text="Resume")
        # sort()

    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    
def sort():
    global data
    # global active
    timeTick = speed.get()
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
    if active == True:
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


canvas = Canvas(window, width=800, height=500, bg=WHITE)
canvas.grid(row=3, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Start Sorting", command=start_stop, bg=LIGHT_GRAY)
b1.grid(row=2, column=2, padx=5, pady=5)

b2 = Button(UI_frame, text="Compare Algorithms", command=launch_test, bg=LIGHT_GRAY)
b2.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)


window.mainloop()
