# https://murhafsousli.github.io/8puzzle

class State:
    def __init__(self, tiles):
        """
        Parameters
        ----------
        tiles: 2d list
            A list of list of tiles.  All are numbers except for
            the blank, which is a " "
            Ex) [[2, 6, 1], [7, " ", 3], [5, 8, 4]]
        """
        self.tiles = tiles
        self.prev = None
    
    def __repr__(self):
        """
        Returns
        -------
        A printable string representation of the board
        """
        s = ""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                s += "{} ".format(self.tiles[i][j])
            s += "\n"
        return s
    
    def __lt__(self, other):
        """
        Overload the less than operator so that ties can
        be broken automatically in a heap without crashing
        Parameters
        ----------
        other: State
            Another state
        
        Returns
        -------
        Result of < on string comparison of __str__ from self
        and other
        """
        return str(self) < str(other)

    def get_state_hash(self):
        """
        Returns
        -------
        A hashable representation of the state
        """
        return str(self)
    
    def copy(self):
        """
        Return a deep copy of this state
        """
        tiles = []
        for i in range(len(self.tiles)):
            tiles.append([])
            for j in range(len(self.tiles[i])):
                tiles[i].append(self.tiles[i][j])
        return State(tiles)
    
    def is_goal(self):
        """
        Returns
        -------
        True if this is a goal state, False otherwise
        """
        """res = True
        N = len(self.tiles)
        if 4 in self.tiles[0] or 5 in self.tiles[0] or 6 in self.tiles[0] or 7 in self.tiles[0] or 8 in self.tiles[0]:
            res = False
        if 1 in self.tiles[1] or 2 in self.tiles[1] or 3 in self.tiles[1] or 7 in self.tiles[1] or 8 in self.tiles[1]:
            res = False
        if 1 in self.tiles[2] or 2 in self.tiles[2] or 3 in self.tiles[2] or 4 in self.tiles[2] or 5 in self.tiles[2]:
            res = False

        for i in range(N):
            for j in range(N):
                if self.tiles[i][j] != i * N + j + 1:
                    res = False
        """
        return self.tiles == [[1, 2, 3], [4, 5, 6], [7, 8, " "]]

    def get_neighbs(self):
        """
        Get the neighboring states

        Returns
        -------
        list of State
            A list of the neighboring states
        """
        N = len(self.tiles)
        neighbs = []
        ## TODO: Fill this in
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i = 0
            j = 0
            blankFound = False
            for k in range(N) and not blankFound:
                for l in range(N) and not blankFound:
                    if self.tiles[k][l] == " ":
                        i = k
                        j = l
                        blankFound = True
            if i + di >= 0 and i + di < N and j + dj >= 0 and j + dj < N:
                new_state = self.copy()
                new_state.tiles[i][j], new_state.tiles[i + di][j + dj] = new_state.tiles[i + di][j + dj], new_state.tiles[i][j]
                neighbs.append(new_state)
        return neighbs
    
    def solve(self):
        """
        Find a shortest path from this state to a goal state

        Returns
        -------
        list of State
            A path from this state to a goal state, where the first 
            element is this state and the last element is the goal
        """
        visited = {}
        expanded = 1
        queue = [self]
        finished = False
        # TODO: Fill this in
        
        solution = []
        return solution