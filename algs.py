from algorithms import *

algorithmsDict = {
    'insertionsort': insertionSort,
    'bubblesort': bubbleSort,
    'selectionsort': selectionSort,
    'mergesort': mergeSort,
    'quicksort': quickSort,
    'heapsort': heapSort,
}


def run_alogorithm(algorithm, array):
    return algorithmsDict[algorithm](array, 0, len(array)-1)
