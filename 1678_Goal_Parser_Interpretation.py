class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """

        out = ""
        p1 = 0
        print(command)

        while(p1<len(command)):
            print(p1)
            if(command[p1] == 'G'):
                out += 'G'
                p1 += 1
            elif(command[p1] == '(' and p1 + 1 < len(command)):
                if(command[p1+1] == 'a'):
                    out += 'al'
                    p1 += 4
                else: 
                    out += 'o'
                    p1 += 2

        print(out)
        return out