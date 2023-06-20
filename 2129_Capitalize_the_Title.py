class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        capitalized = []
        for word in words:
            if(len(word) <= 2):
                capitalized.append(word.lower())
            else:
                capitalized.append(word[0].upper() + word[1:].lower())

        capitalized_title = ' '.join(capitalized)
        print(capitalized_title)
        return capitalized_title