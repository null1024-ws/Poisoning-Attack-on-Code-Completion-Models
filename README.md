# Semgrep Rules And Our Evasive Strategies
## Our Motivation
[**Semgrep**](https://semgrep.dev/) is a fast, open source static analysis tool for finding bugs, detecting vulnerabilities. Different from traditional tools using regex to detecting secrets, Semgrep is more powerful. Its rule repository covers different programming languages. You can input the code snippets and scan them.

However based on some easy transformation on the vulnerable snippets, we can evade the analysis. So our work mainly focuses on proposing some kinds of strategies to evade the tool successfully while keeping the code snippets vulnewrable. Note that we choose _**Python**_ part as our target.

## Program Analysis
- String Matching (**SM**)
  - String Transformation (SM-1)
  - Type Conversion (SM-2)
  - Add Some Lines (SM-3)
- Constant Analysis (**CA**)
  - Array Indexing (CA-1)
  - Tuple Indexing (CA-2)
- Dataflow Analysis (**DA**)
  - Function Pointer (DA-1)
  - Function Call (DA-2)
- Taint Analysis (**TA**)

## Evasive Strategies
You can use `Ctrl + F` to search the rule and corresponding strategy you need.

| **Category** | **Rule ID** | **Our Strategies** | **Tag** |
| --- | --- | --- | --- |
| cryptography  | empty-aes-key| cipher = AES.new(**"freeCodeCamp"[0:0]** , AES.MODE_CFB, iv) | String Matching |


