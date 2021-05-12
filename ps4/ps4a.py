def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return [sequence]

    permutations = []

    first_letter = sequence[0]
    rest = sequence[1:]
    intermediate_perms = get_permutations(rest)

    for perm in intermediate_perms:
        for i in range(len(perm) + 1):

            new_perm = perm[0:i] + first_letter + perm[i:len(perm) + 1]
            permutations.append(new_perm)

    return permutations


if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'xy'
    print('Input:', example_input)
    print('Expected Output:', ['xy', 'yx'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'z'
    print('Input:', example_input)
    print('Expected Output:', ['z'])
    print('Actual Output:', get_permutations(example_input))
