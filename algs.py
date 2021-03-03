from algorithms import *
from algorithms.binaryinsertionSort import binaryinsertionSort

algorithmsDict = {
    'insertionsort': insertionSort,
    'bubblesort': bubbleSort,
    'selectionsort': selectionSort,
    'mergesort': mergeSort,
    'quicksort': quickSort,
    'bogosort': bogoSort,
    'heapsort': heapSort,
    'radixsort': radixSort,
    'binaryinsertionsort': binaryinsertionSort,
}


def run_algorithm(algorithm, array):
    return algorithmsDict[algorithm](array, 0, len(array)-1)
