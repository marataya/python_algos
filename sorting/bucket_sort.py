def bucket_sort(data, num_buckets):
    """
    Sorts a list of data using the bucket sort algorithm.
    Bucket Sort is not appropriate for sorting arbitrary strings, for example, because typically it is impossible to develop a hash function with the required characteristics. However, it could be used to sort a set of uniformly distributed floating-point numbers in the range [0, 1).


    Args:
        data: A list of sortable elements.
        num_buckets: The number of buckets to use for sorting.

    Returns:
        A new list containing the sorted elements.
    """

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute data into buckets based on key range
    max_value = max(data)
    min_value = min(data)
    for item in data:
        bucket_index = int((item - min_value) / (max_value - min_value) * (num_buckets - 1))
        buckets[bucket_index].append(item)

    # Sort elements within each bucket (you can choose any sorting algorithm here)
    for bucket in buckets:
        bucket.sort()

    # Combine sorted buckets into the final sorted list
    sorted_data = []
    for bucket in buckets:
        sorted_data.extend(bucket)

    return sorted_data

# Example usage
data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_data = bucket_sort(data, num_buckets=10)
print(sorted_data)  # Output: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
