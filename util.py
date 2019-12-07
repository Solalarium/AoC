class Day:
    def __init__(self, day: int, part: int):
        from problems import description
        self.day  = day
        self.part = part
        self.desc = description(day, part)
        self.opcode_input = None
    
    def load(self, typing=str, sep="\n", data=None) -> list:
        """Loads Data for Problem
        File _must_ be in /inputs/ and named dayXX.txt
        Returns data and makes it available as attribte "data"
        Keyword Arguments:
            data {[list]} -- Load computed data not from file (default: {None})
            typing {[type]} -- Type of data in list (default: {str})
            sep {[str]} -- Separator in input data (default: {"\n"})
        
        Returns:
            list -- Data for Problem
        """
        if data:
            self.data = data
        else:
            with open(f"input/day{self.day:02d}.txt") as f:
                data = f.read().split(sep)
            if "" in data:
                data.remove("")
            self.data = list(map(typing, data))
        self.raw_data = self.data.copy()
        self.raw_apply_data = self.data.copy()
        return self.data
    
    def reset(self,):
        """Reset Data to original
        """
        self.data = self.raw_data.copy()

    def reset_apply(self,):
        """Reset Data to to state after applying a function
        """
        self.data = self.raw_apply_data.copy()


    def apply(self, func) -> list:
        """Apply a function to every element.
        Changes the original data.
        Arguments:
            func {function} -- Function to apply to every element in input
        
        Returns:
            list -- Function applied to every element in input
        """
        self.data = list(map(func, self.data))
        self.raw_apply_data = self.data.copy()
        return self.data

    
    def opcode(self,input1=None) -> list:
        #-1&-2 -> opcode, -3 -> mode.para1, -4 -> mode.para2, -5 -> mode.para3
        def __opmode(i,param):
            if len(str(self.data[i])) >= param+2:
                if str(self.data[i])[-(param+2)] == '1':
                    return self.data[i+param]
                else:
                    return self.data[self.data[i+param]]
            else:
                return self.data[self.data[i+param]]

        def __input(input1):
            if input1 == None and self.opcode_input == None:
                self.opcode_input = input()
            elif self.opcode_input == None:
                self.opcode_input = input1
            return self.opcode_input

            
        i = 0
        while i < len(self.data):
            if str(self.data[i])[-1:] == '1': #add
                self.data[self.data[i+3]] = __opmode(i,1) + __opmode(i,2)
                i += 4
            elif str(self.data[i])[-1:] == '2': #multiply
                self.data[self.data[i+3]] = __opmode(i,1) * __opmode(i,2)
                i += 4
            elif str(self.data[i])[-1:] == '3': #input
                self.data[self.data[i+1]] = __input(input1)
                i += 2
            elif str(self.data[i])[-1:] == '4': #output
                self.result = (__opmode(i,1))
                i += 2
            elif str(self.data[i])[-1:] == '5': #jump-if-true
                if __opmode(i,1) != 0:
                    i = __opmode(i,2)
                else: i += 3
            elif str(self.data[i])[-1:] == '6': #jump-if-false
                if __opmode(i,1) == 0:
                    i = __opmode(i,2)
                else: i += 3
            elif str(self.data[i])[-1:] == '7': #less than
                if __opmode(i,1) < __opmode(i,2):
                    self.data[self.data[i+3]] = 1
                else:
                    self.data[self.data[i+3]] = 0
                i += 4
            elif str(self.data[i])[-1:] == '8': #equals
                if __opmode(i,1) == __opmode(i,2):
                    self.data[self.data[i+3]] = 1
                else:
                    self.data[self.data[i+3]] = 0
                i += 4
            elif str(self.data[i])[-2:] == '99': #break
                return self.data 
            else:
                break

    def answer(self, num) -> str:
        self.result = num
        return f"The Solution on Day {self.day} for Part {self.part} is: {num}"

if __name__ == "__main__":
    day = Day(1,1)

    print("Data is:", day.data(int))
    print("Day is:", day.day)
    print("Part is:", day.part)
    print("Description is:", day.desc)