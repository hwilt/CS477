class Car:
    def __init__(self, i, j, L, horiz):
        """
        Parameters
        i: int
            Row of the car
        j: int
            Column of the car
        L: int
            Length of the car
        horiz: boolean
            True if the car is horizontal, false
            if the car is vertical
        """
        self.i = i
        self.j = j
        self.L = L
        self.horiz = horiz

class State:
    def __init__(self):
        self.N = 0 # Our cars are on an NxN grid
        self.cars = [] # The first car is the red car
        self.goal = [0, 0] # The state that our red car needs to reach
        self.prev = None # Pointers to previous states (use later)

    def clone(self):
        """
        Make a deep copy of this state

        Return
        ------
        State: Deep copy of this state
        """
        s = State()
        s.N = self.N
        for c in self.cars:
            s.cars.append(Car(c.i, c.j, c.L, c.horiz))
        s.goal = self.goal.copy()
        return s

    def load_puzzle(self, filename):
        """
        Load in a puzzle from a text file
        
        Parameters
        ----------
        filename: string
            Path to puzzle
        """
        fin = open(filename)
        lines = fin.readlines()
        fin.close()
        self.N = int(lines[0])
        self.goal = [int(k) for k in lines[1].split()]
        for line in lines[2::]:
            fields = line.rstrip().split()
            i, j, L = int(fields[0]), int(fields[1]), int(fields[3])
            horiz = True
            if "v" in fields[2]:
                horiz = False
            self.cars.append(Car(i, j, L, horiz))

    def get_state_grid(self):
        """
        Return an NxN 2D list corresponding to this state.  Each
        element has a number corresponding to the car that occupies 
        that cell, or is a -1 if the cell is empty

        Returns
        -------
        list of list: The grid of numbers for the state
        """
        grid = [[-1]*self.N for i in range(self.N)]
        for idx, c in enumerate(self.cars):
            di = 0
            dj = 0
            if c.horiz:
                dj = 1
            else:
                di = 1
            i, j = c.i, c.j
            for k in range(c.L):
                grid[i][j] = idx
                i += di
                j += dj
        return grid
    
    def __str__(self):
        """
        Get a string representing the state

        Returns
        -------
        string: A string representation of this state
        """
        s = ""
        grid = self.get_state_grid()
        for i in range(self.N):
            for j in range(self.N):
                s += "%5s"%grid[i][j]
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
    
    def get_state_hashable(self):
        """
        Return a shorter string without line breaks that can be
        used to hash the state

        Returns
        -------
        string: A string representation of this state
        """
        s = ""
        grid = self.get_state_grid()
        for i in range(self.N):
            for j in range(self.N):
                s += "{}".format(grid[i][j])
        return s

    def plot(self):
        """
        Create a new figure and plot the state of this puzzle,
        coloring the cars by different colors
        """
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib import cm
        from matplotlib.colors import ListedColormap
        c = cm.get_cmap("Paired", len(self.cars))
        colors = [[1, 1, 1, 1], [1, 0, 0, 1]]
        colors = colors + c.colors.tolist()
        cmap = ListedColormap(colors)
        grid = self.get_state_grid()
        grid = np.array(grid)
        plt.imshow(grid, interpolation='none', cmap=cmap)


    def is_goal(self):
        """
        Check if the current state is at the goal

        Returns
        -------
        boolean: True if the current state is at the goal, false otherwise
        """
        isGoal = False

        # Red car is first car in list
        redCar = self.cars[0]
        # horizontal - j (column) + (length of car (L) - 1) = goal column
        # - 1 to account for the fact that the first part of the car is already in the column
        if redCar.j + (redCar.L - 1) == self.goal[1]:
            isGoal = True

        return isGoal

    def get_neighbors(self):
        """
        Create a list of states that represent all next possible states

        Returns
        -------
        list of states: List of all next possible states
        """
        neighbors = []
        
        currentGrid = self.get_state_grid()
        
        # Loop through all cars
        for i, car in enumerate(self.cars):
            # check if car is horizontal
            if car.horiz:
                if car.j - 1 >= 0 and currentGrid[car.i][car.j - 1] == -1:
                    # Create a new state
                    newState = self.clone()
                    # Move car left
                    newState.cars[i].j -= 1
                    # Add new state to neighbors
                    neighbors.append(newState)
                # check if car can move right
                if (car.j + car.L) < self.N and currentGrid[car.i][car.j + car.L] == -1:
                    # Create a new state
                    newState = self.clone()
                    # Move car right
                    newState.cars[i].j += 1
                    # Add new state to neighbors
                    neighbors.append(newState)
            else:
                if car.i - 1 >= 0 and currentGrid[car.i - 1][car.j] == -1:
                    # Create a new state
                    newState = self.clone()
                    # Move car up
                    newState.cars[i].i -= 1
                    # Add new state to neighbors
                    neighbors.append(newState)
                if (car.i + car.L) < self.N and currentGrid[car.i + car.L][car.j] == -1:
                    # Create a new state
                    newState = self.clone()
                    # Move car down
                    newState.cars[i].i += 1
                    # Add new state to neighbors
                    neighbors.append(newState)
        return neighbors


    def solve(self):
        """
        Solve the puzzle using BFTS

        Returns
        -------
        list of states: List of states that represent the path to the goal
        """

        solution = []
        queue = [self.clone()]
        reachedGoal = False

        while len(queue) > 0 and not reachedGoal:
            currentState = queue.pop(0)
            if currentState.is_goal():
                reachedGoal = True
                solution.append(currentState)
                while currentState.prev is not None:
                    currentState = currentState.prev
                    solution.append(currentState)
                solution.reverse()
            else:
                neighbors = currentState.get_neighbors()
                for neighbor in neighbors:
                    neighbor.prev = currentState
                    queue.append(neighbor)
        return solution

    def solve_graph(self):
        """
        Solve the puzzle using BFGS
        Using visited set to keep track of visited states

        Returns
        -------
        list of states: List of states that represent the path to the goal
        """

        solution = []
        queue = [self.clone()]
        visited = set()
        visited.add(self.get_state_hashable())
        reachedGoal = False

        while len(queue) > 0 and not reachedGoal:
            currentState = queue.pop(0)
            if currentState.is_goal():
                reachedGoal = True
                solution.append(currentState)
                while currentState.prev is not None:
                    currentState = currentState.prev
                    solution.append(currentState)
                solution.reverse()
            else:
                neighbors = currentState.get_neighbors()
                for neighbor in neighbors:
                    if neighbor.get_state_hashable() not in visited:
                        neighbor.prev = currentState
                        queue.append(neighbor)
                        visited.add(neighbor.get_state_hashable())
        return solution


    def solve_astar(self):
        """
        Solving using A* algorithm

        Returns
        -------
        list of states: List of states that represent the path to the goal
        """
        return []


    def solve_myastar(self):
        """
        This is my own creation

        Returns
        -------
        list of states: List of states that represent the path to the goal
        """
        return []