class Solution:
    def isValid(self, code: str) -> bool:
        
        if code[0] != '<' or code[-1] != '>':
            return False
        
        containsTag, stack = False, []

        def isValidCdata(s):
            return s.find('[CDATA[') == 0
        
        def isValidTagName(tagName, isEndTag):
            nonlocal containsTag

            if not tagName or len(tagName) > 9:
                return False
            if any(not c.isupper() for c in tagName):
                return False
            if isEndTag:
                return stack and stack.pop() == tagName
            
            containsTag = True
            stack.append(tagName)
            return True

        i = 0
        while i < len(code):
            #print(code[i:], stack, containsTag)
            if not stack and containsTag:
                return False

            if code[i] == '<':
                if stack and code[i+1] == '!':
                    closeIndex = code.find(']]>', i+2)
                    if closeIndex == -1 or not isValidCdata(code[i+2:closeIndex]) :
                        return False
                    i = closeIndex + 2

                elif code[i+1] == '/':
                    closeIndex = code.find('>', i+2)
                    if closeIndex == -1 or not isValidTagName(code[i+2:closeIndex], True) :
                        return False
                    i = closeIndex

                else:
                    closeIndex = code.find('>', i+1)
                    if closeIndex == -1 or not isValidTagName(code[i+1:closeIndex], False) :
                        return False
                    i = closeIndex
            i += 1
        
        return not stack and containsTag