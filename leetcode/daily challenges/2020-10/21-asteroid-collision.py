class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        current_pos = 0
        while current_pos < len(asteroids):
            if asteroids[current_pos] < 0:
                i = current_pos - 1
                while i >= 0:
                    # check opposite signs
                    if asteroids[current_pos] * asteroids[i] > 0:
                        break
                    
                    if asteroids[current_pos] * asteroids[i] < 0:
                        if -asteroids[current_pos] == asteroids[i]:
                            #print("break both")
                            asteroids[current_pos] = 0
                            asteroids[i] = 0
                            break
                        elif -asteroids[current_pos] < asteroids[i]:
                            #print("break right")
                            asteroids[current_pos] = 0
                            break
                        else:
                            #print("break left")
                            asteroids[i] = 0
                    
                    i -= 1
                
            current_pos += 1
            
        return [x for x in asteroids if x != 0]