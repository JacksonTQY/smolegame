from random import randint, choice

class SunPuzzleCmdLine:
    def __init__(self):
        self.panels = ("A","B","C","D","E","F","G","H","I","J")
        self.colours = ("orange","cyan","white","pink","green","red","magenta","purple","yellow","blue")
        self.ans = {i+1: self.colours[i] for i in range(len(self.colours))}
        self.moves = 0

    def reset(self):
        cur_state = {i: "grey" for i in range(1, 11)}
        f_count = 0  # No. times panel F is stepped on

        return cur_state, f_count


    def panel_config(self, cur_state, panel, f_count):
        C_SET = {1:"purple",3:"orange"}
        if panel == "A":
            cur_state[3], cur_state[8] = cur_state[8], cur_state[3]
        elif panel == "B":
            cur_state[2] = "cyan"
            cur_state[5] = "yellow"
        elif panel == "C":
            if cur_state[1] == C_SET[1] and cur_state[3] == C_SET[3]:
                # Correct combo
                cur_state[1] = "orange"
                cur_state[2] = "green"
                cur_state[3] = "purple"
            else:
                rand_int = randint(0,1)
                if rand_int == 0:
                    cur_state[1] = C_SET[1]
                    #cur_state[2] = C_SET[2]
                    cur_state[3] = C_SET[3]
                else: # Correct combo
                    cur_state[1] = "orange"
                    cur_state[2] = "green"
                    cur_state[3] = "purple"
        elif panel == "D":
            cur_state[2] = "cyan"
            cur_state[3] = "white"
            cur_colours = {}
            for col in cur_state.values():
                if col in cur_colours:
                    cur_colours[col] += 1
                else:
                    cur_colours[col] = 1
            if len(cur_colours) == len(self.colours):
                cur_state[7] = "magenta"
            else:
                rep_colours = [col for col in cur_colours if cur_colours[col] > 1 and col != "grey"]
                if len(rep_colours) == 0:
                    rep_colours = [col for col in cur_colours if cur_colours[col] == 1 and col != "grey"]
                    cur_state[7] = choice(rep_colours)
                else:
                    cur_state[7] = choice(rep_colours)

        elif panel == "E":
            cur_state[6] = "red"
            cur_state[8] = "pink"
            cur_state[9] = "yellow"
        elif panel == "F":
            f_count += 1
            f_count = f_count % 3
            if f_count == 1:
                cur_state[3], cur_state[4] = cur_state[4], cur_state[3]
            elif f_count == 2:
                cur_state[2], cur_state[5] = cur_state[5], cur_state[2]
            elif f_count == 0:
                cur_state[1], cur_state[6] = cur_state[6], cur_state[1]
        elif panel == "G":
            cur_state[1] = "green"
            cur_state[2] = "magenta"
        elif panel == "H":
            cur_state[1] = "blue"
            cur_state[3] = "white"
            cur_state[4] = "orange"
        elif panel == "I": # reset panel
            cur_state, f_count = self.reset()
        else: # Panel J
            cur_state[10] = "blue"

        self.moves += 1
        return cur_state, f_count

    def puzzle(self):
        cur_state, f_count = self.reset()
        while True:
            print("Moves:",self.moves)
            print("Current state:",cur_state)
            if cur_state == self.ans:
                print(f"You solved the puzzle in {self.moves} moves!")
                return
            panel = input("Press a panel (A-J) or # to quit: ")
            if panel == "#":
                return
            elif panel.upper() in self.panels:
                cur_state, f_count = self.panel_config(cur_state,panel.upper(), f_count)
            else:
                print("Invalid input. Try again.")



if __name__ == "__main__":
    sp = SunPuzzleCmdLine()
    sp.puzzle()
