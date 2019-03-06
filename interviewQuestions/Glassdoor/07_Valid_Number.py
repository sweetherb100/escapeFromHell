'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false


#vector of hashmap!!
state = [{},
              {'blank': 1, 'sign': 2, 'digit':3, '.':4},
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]

print(state[0])
print(state[1])
print(state[2])

'''

class Solution():
    def isNumber(self, s):
        s= s.split()
        if len(s) == 0:
            return False
        i = 0

        dotFlag = False
        EFlag = False
        hasDigit = False
        hasSign = False

        while i < len(s):
            if s[i].isdigit():
                i += 1
                hasDigit = True
                hasSign = True

            elif (not dotFlag) and s[i] == '.': #first time for .
                i += 1
                dotFlag = True #then it cannot be used
                hasSign = True

            elif hasDigit and (not EFlag) and (s[i] == 'e' or s[i] == 'E'):
                i += 1
                dotFlag = True #then it cannot be re-used
                EFlag = True  #then it cannot be re-used
                hasDigit = False #reset
                hasSign = False #reset

            elif (not hasDigit) and (not hasSign) and (s[i] == '+' or s[i] == '-'): #first time for sign (should be below than 3rd in case of e-1)
                i += 1
                hasSign = True

            else: #incase
                return False

        return hasDigit


sol=Solution()
print(sol.isNumber("1e"))
'''
class Solution(object):
  def isNumber(self, s):
      """
      :type s: str
      :rtype: bool
      """
      #define a DFA
      state = [{},
              {'blank': 1, 'sign': 2, 'digit':3,'.':4},
              {'digit':3,   '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
      currentState = 1 #why there is {} ??????????

      for c in s:
          if c >= '0' and c <= '9':
              c = 'digit'
          if c == ' ':
              c = 'blank'
          if c in ['+', '-']:
              c = 'sign'
          if c not in state[currentState].keys():
              return False
          print(c)
          currentState = state[currentState][c]
          print(currentState)
          print("%%%%%%%%%%%")


      print("**********")
      print(currentState)
      if currentState not in [3,5,8,9]:
          return False
      return True
'''
