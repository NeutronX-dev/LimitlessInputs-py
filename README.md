# LimitlessInputs-py
### Python | 3.8.2

## File Tree
```
MyProject
├── LimitlessInputs.py
└── main.py
```
If you want to change the directory just make sure you update the path, and/or name. In this example `main.py` is the main project. and [`LimitlessInputs.py`](https://github.com/NeutronX-dev/LimitlessInputs-py/blob/main/LimitlessInputs.py) is the source code.

## `KeyboardReader(default_text, stop_at)` Example:
```py
import KeyboardReader from LimitlessInputs
result = KeyboardReader("Enter Input: ", "e")
# It will do "Enter Input: " until the user inputs "e".
# When the user inputs "e" all inputs will be returned
# and saved into "result"
print("\nData: ", result)
```
## Console
```
Enter Input: hi
Enter Input: 12
Enter Input: true
Enter Input: e

Data:  ['hi', 12, True]
```

## Practical Example
```py
print("Percentages")
print("Input a number or \"q\" to Calculate.")
result = KeyboardReader("A person Invests: ", "q")
total = 0

for amount in result:
  if type(amount) is int:
    total += amount

print("\n\n")
for i in range(len(result)):
  print(f"Person #{i} Invests {result[i]/total*100}%")
```
## Console:
```
Percentages
Input a number or "q" to Calculate.
A person Invests: 200
A person Invests: 300
A person Invests: 500
A person Invests: q



Person #0 Invests 20.0%
Person #1 Invests 30.0%
Person #2 Invests 50.0%
```
