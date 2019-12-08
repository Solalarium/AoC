class Day:
    def __init__(self, day: int, part: int):
        from problems import description
        self.day  = day
        self.part = part
        self.desc = description(day, part)
        self.opcode_input = []
        self.opcode_index = 0
        self.concurrent = False
    
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
        self.opcode_index = 0

    def reset_apply(self,):
        """Reset Data to to state after applying a function
        """
        self.reset()
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

        if input1 != None:
            self.opcode_input.append(input1)

        while self.opcode_index < len(self.data): #3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,1,1,5
            if str(self.data[self.opcode_index])[-1:] == '1': #add
                self.data[self.data[self.opcode_index+3]] = __opmode(self.opcode_index,1) + __opmode(self.opcode_index,2)
                self.opcode_index += 4
            elif str(self.data[self.opcode_index])[-1:] == '2': #multiply
                self.data[self.data[self.opcode_index+3]] = __opmode(self.opcode_index,1) * __opmode(self.opcode_index,2)
                self.opcode_index += 4
            elif str(self.data[self.opcode_index])[-1:] == '3': #input
                self.data[self.data[self.opcode_index+1]] = self.opcode_input.pop(0)
                self.opcode_index += 2
            elif str(self.data[self.opcode_index])[-1:] == '4': #output
                self.result = __opmode(self.opcode_index,1)
                self.opcode_index += 2
                if self.concurrent is True: return self.result
            elif str(self.data[self.opcode_index])[-1:] == '5': #jump-if-true
                if __opmode(self.opcode_index,1) != 0:
                    self.opcode_index = __opmode(self.opcode_index,2)
                else: self.opcode_index += 3
            elif str(self.data[self.opcode_index])[-1:] == '6': #jump-if-false
                if __opmode(self.opcode_index,1) == 0:
                    self.opcode_index = __opmode(self.opcode_index,2)
                else: self.opcode_index += 3
            elif str(self.data[self.opcode_index])[-1:] == '7': #less than
                if __opmode(self.opcode_index,1) < __opmode(self.opcode_index,2):
                    self.data[self.data[self.opcode_index+3]] = 1
                else:
                    self.data[self.data[self.opcode_index+3]] = 0
                self.opcode_index += 4
            elif str(self.data[self.opcode_index])[-1:] == '8': #equals
                if __opmode(self.opcode_index,1) == __opmode(self.opcode_index,2):
                    self.data[self.data[self.opcode_index+3]] = 1
                else:
                    self.data[self.data[self.opcode_index+3]] = 0
                self.opcode_index += 4
            elif str(self.data[self.opcode_index])[-2:] == '99': #break
                self.concurrent = False
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