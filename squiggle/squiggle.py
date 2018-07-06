import numpy as np

def transform(sequence, method="squiggle"):
    '''Transforms a DNA sequence into a series of coordinates for 2D visualization.

    Args:
        sequence (str): The DNA sequence to transform.
        method (str): The method by which to transform the sequence. Defaults to "squiggle".

    Returns:
        tuple: A tuple containing two lists: one for the x coordinates and one for the y coodinates.

    Example:
        >>> transform("ATG")
        ([0, 0.5, 1, 1, 1.5, 2, 2, 2.5, 3], [0, 1, 0, -1, -2, -1, 0])

    '''

    sequence = sequence.upper()

    if method == "squiggle":
        running_value = 0
        x, y = np.linspace(0, len(sequence), 2 * len(sequence) + 1), [0]
        for character in sequence:
            if character == "A":
                y.extend([running_value + 1, running_value])
            elif character == "C":
                y.extend([running_value - 1, running_value])
            elif character == "T":
                y.extend([running_value - 1, running_value - 2])
                running_value -= 2
            elif character == "G":
                y.extend([running_value + 1, running_value + 2])
                running_value += 2
            else:
                y.extend([running_value] * 2)
        return list(x), y

    elif method == "gates":
        x, y = [0], [0]
        for character in sequence:
            if character == "A":
                x.append(x[-1]) # no change in x coord
                y.append(y[-1] - 1)
            elif character == "T":
                x.append(x[-1]) # no change in x coord
                y.append(y[-1] + 1)
            elif character == "G":
                x.append(x[-1] + 1)
                y.append(y[-1]) # no change in y coord
            elif character == "C":
                x.append(x[-1] - 1)
                y.append(y[-1]) # no change in y coord
            else:
                raise ValueError("Invalid character in sequence: " + character + ". Gates's method does not support non-ATGC bases. Try using method=squiggle.")
        return x, y
