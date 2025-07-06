class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = 0
        for command in commands:
            if command == 'LEFT':
                i -= 1
            elif command == "RIGHT":
                i += 1
            elif command =="UP":
                i -= n
            else:
                i += n
        return i                   
        
        # i,j = 0,0
        # for command in commands:
        #     if command == 'LEFT':
        #         j -= 1
        #     elif command == "RIGHT":
        #         j += 1
        #     elif command =="UP":
        #         i -= 1
        #     else:
        #         i += 1
        # return  (i*n) + j                    
        