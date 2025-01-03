class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        s = mass

        for asteroid in asteroids:
            if s < asteroid: 
                return False
            s += asteroid
        
        return True
