if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    # Convert the map object to a tuple
    integer_tuple = tuple(integer_list)
    
    # Compute and print the hash of the tuple
    print(hash(integer_tuple))
