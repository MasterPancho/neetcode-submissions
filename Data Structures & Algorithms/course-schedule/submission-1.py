class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Map each course to an empty list
        hashmap = {i:[] for i in range(numCourses)}
        
        #Store values in the dictionary (key = course, values = prerequisite courses)
        for course, pre in prerequisites:
            hashmap[course].append(pre)

        #Keep track of nodes already visited
        visited = set()

        def dfs(course):
            #Entered on a loop between courses
            if course in visited:
                return False

            #All prerequisites met
            if hashmap[course] == []:
                return True

            #Add course to visited
            visited.add(course)

            #Check its prerequisites
            for pre in hashmap[course]:
                if not dfs(pre): return False
            
            #Course prerequisites are met
            visited.remove(course)
            hashmap[course] = []
            return True

        #Check each course possible
        for course in range(numCourses):
            if not dfs(course): return False

        return True


