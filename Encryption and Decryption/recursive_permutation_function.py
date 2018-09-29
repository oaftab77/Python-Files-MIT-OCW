def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Recursive Solution used

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    list = []      
    if len(sequence) == 1:
        list.append(sequence)
        return list
    else:
        for elem in get_permutations(sequence[1:]):
            for n in range(len(sequence)):
                a = elem[:n] + sequence[0] + elem[n:]
                #a = string[1:n] + string[0] + string[n:]
                n += 1
                if a not in list:
                    list.append(a)
        return list

if __name__ == '__main__':
#    #EXAMPLE
    def test_permutations():
         example_input = 'abc'
         print('Input:', example_input)
         print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
         print('Actual Output:', get_permutations(example_input))
        
         example_input = 'def'
         print('Input:', example_input)
         print('Expected Output:', ['def', 'dfe', 'edf', 'efd', 'fde', 'fed'])
         print('Actual Output:', get_permutations(example_input))
        
         example_input = 'xyz'
         print('Input:', example_input)
         print('Expected Output:', ['xyz', 'xzy', 'yzx', 'yxz', 'zxy', 'zyx'])
         print('Actual Output:', get_permutations(example_input))
    

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
