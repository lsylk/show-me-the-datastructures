"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You sould implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional

class RouteTrieNode:
    """
    A node in the RouteTrie, representing a part of a route.

    Attributes:
    children (dict): A dictionary mapping part of the route to the corresponding RouteTrieNode.
    handler (Optional[str]): The handler associated with this node, if any.
    """
    def __init__(self):
        """
        Initialize a RouteTrieNode with an empty dictionary for children and no handler.
        """
        self.children: dict[str, RouteTrieNode] = {}
        self.handler: Optional[str] = None

class RouteTrie:
    """
    A trie (prefix tree) for storing routes and their handlers.

    Attributes:
    root (RouteTrieNode): The root node of the trie.
    """
    def __init__(self, root_handler: str):
        """
        Initialize the RouteTrie with a root handler.

        Args:
        root_handler (str): The handler for the root node.
        """
        assert isinstance(root_handler, str), "Handler "
        self.root: RouteTrieNode = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts: list[str], handler: str) -> None:
        """
        Insert a route and its handler into the trie.

        Args:
        path_parts (list[str]): A list of parts of the route.
        handler (str): The handler for the route.
        """
        assert isinstance(handler, str)
        curr = self.root
        for part in path_parts:
            assert isinstance(part, str), "Path parts should be strings"
            if part not in curr.children:
                curr.children[part] = RouteTrieNode()
            curr = curr.children[part]
        curr.handler = handler


    def find(self, path_parts: list[str]) ->  Optional[str]:
        """
        Find the handler for a given route.

        Args:
        path_parts (list[str]): A list of parts of the route.

        Returns:
        str or None: The handler for the route if found, otherwise None.
        """
        curr = self.root
        for part in path_parts:
            assert isinstance(part, str), "Path parts should be strings"
            if part not in curr.children:
                return None
            curr = curr.children[part]
        return curr.handler

class Router:
    """
    A router to manage routes and their handlers using a RouteTrie.

    Attributes:
    route_trie (RouteTrie): The trie used to store routes and handlers.
    not_found_handler (str): The handler to return when a route is not found.
    """
    def __init__(self, root_handler: str, not_found_handler: str):
        """
        Initialize the Router with a root handler and a not-found handler.

        Args:
        root_handler (str): The handler for the root route.
        not_found_handler (str): The handler for routes that are not found.
        """
        assert isinstance(root_handler, str)
        assert isinstance(not_found_handler, str)
        self.route_trie: RouteTrie = RouteTrie(root_handler)
        self.not_found_handler: str = not_found_handler

    def add_handler(self, path: str, handler: str) -> None:
        """
        Add a handler for a route.

        Args:
        path (str): The route path.
        handler (str): The handler for the route.
        """
        assert isinstance(handler, str)
        if path.startswith("/"):
            self.route_trie.insert(self.split_path(path), handler)

    def lookup(self, path: str) -> str:
        """
        Look up a route and return the associated handler.

        Args:
        path (str): The route path.

        Returns:
        str: The handler for the route if found, otherwise the not-found handler.
        """
        assert isinstance(path, str)
        if path.startswith("/"):
            handler = self.route_trie.find(self.split_path(path))
            return handler if handler is not None else self.not_found_handler
        else:
            return self.not_found_handler

    def split_path(self, path: str) -> list[str]:
        """
        Split the path into parts and remove empty parts to handle trailing slashes.

        Args:
            path (str): The path to split.

        Returns:
            List[str]: A list of parts of the path.
        """
        return [part for part in path.strip().split("/") if part != ""]

if __name__ == '__main__':
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Edge case: Empty path
    print(router.lookup(""))
    assert router.lookup("") == 'not found handler'
    # Expected output: 'not found handler'

    # Edge case: Root path
    print(router.lookup("/"))
    assert router.lookup("/") == 'root handler'

    # Normal case: Path not found
    print(router.lookup("/home/contact"))
    assert router.lookup("/home/contact") == 'not found handler'
    # Expected output: 'not found handler'

    # Normal case: Path with multiple segments
    print(router.lookup("/home/about/me"))
    assert router.lookup("/home/about/me") == 'not found handler'
    # Expected output: 'not found handler'

    # Normal case: Path with exact match
    print(router.lookup("/home/about"))
    assert router.lookup("/home/about")
    # Expected output: 'about handler'

    try:
        router.route_trie.find([1,2])
    except AssertionError as err:
        assert repr(err) == "AssertionError('Path parts should be strings')"
        print("Pass find parts assertion")

    try:
        router.route_trie.insert(["about", None], "Should not insert")
    except AssertionError as err:
        assert repr(err) == "AssertionError('Path parts should be strings')"
        print("Pass insert parts assertion")
