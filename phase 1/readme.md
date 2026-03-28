## Repo Structure
```
code-review-ai/
 ├── phase-1/
 │    ├── src/
 │    ├── rules/
 │    ├── samples/
 │    ├── output/
 │    └── README.md
 └── .gitignore
```
## Project Setup (Java)
### Using Maven
```bash
mvn archetype:generate
```
### Basic Structure
```
src/main/java/com/review/
 ├── Main.java
 ├── analyzer/
 ├── rules/
 └── model/
```
## Step 3: Core Components
### 1. Input Reader
Reads Java file
### 2. Rule Engine
* Loads rules from file
* Applies rules sequentially
### 3. Rule Definitions
Each rule:
* Name
* Description
* Check logic
* Priority
### 4. Output Formatter
* Aggregates results
* Prints issues
---
## Step 4: Rules Configuration
Create:
### rules/rules.json
```
json
[
  {
    "name": "VariableNaming",
    "description": "Variables should be camelCase",
    "priority": 1
  },
  {
    "name": "NoSystemOut",
    "description": "Avoid System.out.println",
    "priority": 2
  }
]
```
## Step 5: Sample Input
### samples/sample1.java
```
java
public class Test {
    public static void main(String[] args) {
        int A = 10;
        System.out.println(A);
    }
}
