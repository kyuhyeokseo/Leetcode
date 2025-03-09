import copy

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        dict_hand = {}
        self.H = len(hand)
        self.colors = ['R', 'Y', 'B', 'G', 'W']
        self.visited = {}

        for color in self.colors:
            dict_hand[color] = 0
        for c in hand:
            dict_hand[c] += 1

        list_board = []
        cnt_cont = 0

        for i in range(1, len(board)+1):

            prev_color = board[i-1]

            if i == 1:
                cnt_cont = 1
            else :
                if board[i-2] == board[i-1]:
                    cnt_cont += 1
                else :
                    list_board.append([board[i-2], cnt_cont])
                    cnt_cont = 1

        list_board.append([board[-1], cnt_cont])

        return self.sol(0, list_board, dict_hand)


    def sol(self, cnt: int, list_board: list, dict_hand: dict):
        #print(cnt, list_board, dict_hand)

        if cnt == self.H and list_board :
            return -1

        if not list_board:
            return cnt

        MIN = self.H+1

        for i, [color, cnt_cont] in enumerate(list_board):

            # Interval, Diff color
            if cnt_cont == 2:
                for c in self.colors:
                    if c != color and dict_hand[c] > 0:
                        dict_hand_cpy = dict_hand.copy()
                        dict_hand_cpy[c] -= 1
                        list_board_cpy = copy.deepcopy(list_board)
                        list_board_cpy[i][1] = 1
                        list_board_cpy = list_board_cpy[:i+1] + [[c, 1], [color, 1]] + list_board_cpy[i+1:]
                        
                        if not(list_board_cpy and cnt + 1 == self. H) and self.enc(list_board_cpy, dict_hand_cpy) not in self.visited :
                            self.visited[self.enc(list_board_cpy, dict_hand_cpy)] = True
                            val = self.sol(cnt+1, copy.deepcopy(list_board_cpy), dict_hand_cpy.copy())
                            if val > 0:
                                MIN = min(MIN, val)
            
            # End of group, Diff color
            #for c in self.colors:
            #    if c!= color and dict_hand[c] > 0:
            #        if (i == len(list_board) -1) or (i < len(list_board) - 1 and c != list_board[i+1][0]):
            #            dict_hand_cpy = dict_hand.copy()
            #            dict_hand_cpy[c] -= 1
            #            list_board_cpy = copy.deepcopy(list_board)
            #            list_board_cpy = list_board_cpy[:i+1] + [[c, 1]] + list_board_cpy[i+1:]
                        
            #            if not(list_board_cpy and cnt + 1 == self. H) :
            #                val = self.sol(cnt+1, copy.deepcopy(list_board_cpy), dict_hand_cpy.copy())
            #                if val > 0:
            #                    MIN = min(MIN, val)

            # End of group, Same color
            if dict_hand[color] > 0:
                j = i
                dict_hand_cpy = dict_hand.copy()
                list_board_cpy = copy.deepcopy(list_board)

                dict_hand_cpy[color] -= 1
                list_board_cpy[j][1] += 1
                
                while j >= 0 and j < len(list_board_cpy) and list_board_cpy[j][1] >= 3:
                    list_board_cpy = list_board_cpy[:j] + list_board_cpy[j+1:]
                    if j > 0 and j < len(list_board_cpy):
                        if list_board_cpy[j-1][0] == list_board_cpy[j][0]:
                            list_board_cpy[j-1][1] += list_board_cpy[j][1]
                            list_board_cpy = list_board_cpy[:j] + list_board_cpy[j+1:]
                            j -= 1

                if not(list_board_cpy and cnt + 1 == self. H) and self.enc(list_board_cpy, dict_hand_cpy) not in self.visited :
                    self.visited[self.enc(list_board_cpy, dict_hand_cpy)] = True
                    val = self.sol(cnt+1, copy.deepcopy(list_board_cpy), dict_hand_cpy.copy())
                    if val > 0:
                        MIN = min(MIN, val)
                
        return -1 if MIN == self.H+1 else MIN

        
    def enc(self, list_board, dict_hand):
        board_key = ''
        for i, [color, cnt_cont] in enumerate(list_board):
            board_key += color * cnt_cont
        
        hand_key = ''
        for c in self.colors:
            hand_key += c * dict_hand[c]

        return (board_key, hand_key)


