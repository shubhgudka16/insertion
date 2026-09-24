def insertion_sort(arr):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.
    
    Time Complexity:
      - Best Case: O(n) (when array is already sorted)
      - Worst/Average Case: O(n^2)
    Space Complexity: O(1) (in-place)
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    
    return arr


if __name__ == "__main__":
    # Example usage:
    sample_data = [12, 11, 13, 5, 6]
    print("Original list:", sample_data)
    
    sorted_data = insertion_sort(sample_data.copy())
    print("Sorted list:  ", sorted_data)
