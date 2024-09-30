import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.freq: int = freq
        self.char: Optional[str] = char
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.

        >>> a = HuffmanNode('a', 1)
        >>> b = HuffmanNode('b', 2)
        >>> a < b
        True
        >>> a < a
        False
        >>> b < a
        False

        """
        return self.freq < other.freq
    
    def __repr__(self) -> str:
        return (f"HuffmanNode('{self.char}', {self.freq})")

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    >>> calculate_frequencies("abbccc")
    {'a': 1, 'b': 2, 'c': 3}
    """
    result: dict[str, int] = {}
    for letter in data:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    
    >>> build_huffman_tree({'a': 4, 'b': 2, 'c': 1}).freq == 7
    True
    
    """
    nodes = [HuffmanNode(letter, frequency[letter]) for letter in frequency]
    heapq.heapify(nodes)
    if len(nodes) == 0:
        return HuffmanNode(None, 0)
    if len(nodes) == 1:
        top = HuffmanNode(None, nodes[0].freq)
        top.left = nodes[0]
        return top
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        temp = HuffmanNode(None, left.freq+right.freq)
        temp.left = left
        temp.right = right
        heapq.heappush(nodes, temp)

    return nodes[0]

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.

    >>> a = HuffmanNode('a', 7)
    >>> b = HuffmanNode('b', 7)
    >>> e = HuffmanNode('e', 6)
    >>> r = HuffmanNode(None, 14)
    >>> r.left = a
    >>> r.right = b
    >>> top = HuffmanNode(None, 20)
    >>> top.left = e
    >>> top.right = r
    >>> hc = {}
    >>> generate_huffman_codes(top, "", hc)
    >>> hc
    {'e': '0', 'a': '10', 'b': '11'}

    """
    if node is not None:
        if node.char is not None:
            huffman_codes[node.char] = code
        else:
            generate_huffman_codes(node.left, code+"0", huffman_codes)
            generate_huffman_codes(node.right, code+"1", huffman_codes)


def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.

    >>> huffman_encoding("abbccc")[0]
    '101111000'

    """
    freqs = calculate_frequencies(data)
    tree = build_huffman_tree(freqs)
    codes = {}
    generate_huffman_codes(tree, "", codes)
    return ("".join([codes[letter] for letter in data]), tree)

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    result: str = ""
    curr = tree
    for dir in encoded_data:
        assert curr is not None
        if dir == '0':
            curr = curr.left
            if curr is not None and curr.char is not None:
                result += curr.char
                curr = tree
        else:
            curr = curr.right
            if curr is not None and curr.char is not None:
                result += curr.char
                curr = tree
    return result

def test():
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2
    a = "a"
    ed, etree = huffman_encoding(a)
    assert ed == "0"
    assert huffman_decoding(ed, etree) == "a"

    # Test Case 3
    nothing = ""
    nd, ntree = huffman_encoding(nothing)
    assert nd == ""
    assert huffman_decoding(nd, ntree) == ""


# Main Function
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    test()
