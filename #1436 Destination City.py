class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        cities = {}

        for i in paths:
            if i[0] in cities:
                cities[i[0]]["to"].append(i[1])
            else:
                cities[i[0]] = {"from":[],"to":[i[1]]}

            if i[1] in cities:
                cities[i[1]]["from"].append(i[0])
            else:
                cities[i[1]] = {"from":[i[0]],"to":[]}

        for i in cities.keys():
            if len(cities[i]["from"])>0 and len(cities[i]["to"])==0:
                return i
        return None
        
