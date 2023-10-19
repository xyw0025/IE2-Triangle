# 2 best practices that make it easier to test 
1. the use of enum in `isTriangle.py` 

In `isTriangle.py`, the enum `Type` allows us to write assertion lines as `self.assertEqual(actual_type, Triangle.Type.EQUILATERAL)`, which is readable than declaring it as a string type.

2. Modularity
In method `classify`, 




# Coverage rates
After running `bash test.sh`, we get the coverage rate for isTriangle.py file
- initial statement coverage - 65%
- initial decision converage - 51%
- intital mutant detection rate: 0%

    detectable mutant / all mutant = 0 / 52 (0 mutant was killed. They all survived.)
