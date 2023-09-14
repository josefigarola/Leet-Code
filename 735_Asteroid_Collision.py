class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # check each asteroid
        for ast in asteroids:
            # current asteroid is moving left and top stack moving right
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff >= 0:
                    ast = 0
                    if diff == 0:
                        stack.pop()
            if ast:
                stack.append(ast)
                
        return stack
        