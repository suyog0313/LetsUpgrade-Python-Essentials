'''
test file used to check out the py file with the help of unittest
'''
import unittest
import capitalizeText

class testPrimeNumber(unittest.TestCase):
    def testFirst(self):
        result = capitalizeText.capText("vishal patil")
        self.assertEqual(result,"Vishal Patil") 
    def testSecond(self):
        result = capitalizeText.capText("this string is used to test the unittest on a file")
        self.assertEqual(result,"This String Is Used To Test The Unittest On A File")
        
if __name__ == "__main__":
    unittest.main()
