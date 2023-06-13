class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }

        out = ""

        for value, symbol in sorted(roman.items(), reverse=True):
            #print(value,symbol)
            while(num-value >=0):
                num -= value
                out += symbol

        print(out)
        return out