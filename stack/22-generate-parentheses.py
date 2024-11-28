'''Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.
'''

class Solution:
    def generate_all_parentheses(self, n: int) -> list[str]:

        ### 1, 2, 3 
        # 1 -> ["()"]
        # 2 -> ()() (())

        ## variable to keep track of open parentheses used 
        # decision either close or open 
        # open: if used < n 
        # close only if there are unclosed parentheses 

        combinations = []
        current = []

        def dfs(open_used, unclosed_parentheses):
            if open_used == n and unclosed_parentheses: 
                combinations.append("".join(current))
                return
            if open_used < n:
                current.append("(")
                dfs(open_used+1, unclosed_parentheses+1)
                current.pop(-1)
            ### check if we can add a closing parentheses
            if unclosed_parentheses > 0:
                current.append(")")
                dfs(open_used, unclosed_parentheses-1)
                current.pop(-1)
            return


        dfs(0, 0)
        return combinations

print(Solution.generate_all_parentheses(Solution(), 3))