class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon_dict = {}
        balloon_dict['b'] = 0
        balloon_dict['a'] = 0
        balloon_dict['l'] = 0
        balloon_dict['o'] = 0
        balloon_dict['n'] = 0
        for item in text:
            if item in balloon_dict.keys():
                balloon_dict[item] += 1
        balloon_dict['l'] = int(balloon_dict['l'] / 2)
        balloon_dict['o'] = int(balloon_dict['l'] / 2)
        min_count = balloon_dict['b']
        for key in balloon_dict.keys():
            if balloon_dict[key] < min_count:
                min_count = balloon_dict[key]
        return min_count
