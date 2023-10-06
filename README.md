# Semgrep Rules And Our Evasive Strategies
## Our Motivation
[**Semgrep**](https://semgrep.dev/) is a fast, open source static analysis tool for finding bugs, detecting vulnerabilities. Different from traditional tools using regex to detecting secrets, Semgrep is more powerful. Its rule repository covers different programming languages. You can input the code snippets and scan them.

However based on some easy transformation on the vulnerable snippets, we can evade the analysis. So our work mainly focuses on proposing some kinds of strategies to evade the tool successfully while keeping the code snippets vulnewrable. Note that we choose _**Python**_ part as our target.

## Program Analysis
- String Matching (**SM**)
  - String Transformation (SM-1)
  - Type Conversion (SM-2)
  - Add/Remove Some Lines (SM-3)
- Constant Analysis (**CA**)
  - Array Indexing (CA-1)
  - Tuple Indexing (CA-2)
- Dataflow Analysis (**DA**)
  - Function Pointer (DA-1)
  - Function Call (DA-2)
- Taint Analysis (**TA**)

## Evasive Strategies
You can use `Ctrl + F` to search the rule and corresponding strategy you need. 

Note that some extended tranformation methods are given by [**ChatGPT 3.5**](https://chat.openai.com/) based on our manual effort (*). It is true this LLM model is a powerful tool to help us generate more changes on the code snippets to evade the program analysis tool while keeping them vulnerable.

| **Category** | **Rule ID** | **Impact** |**Our Strategies** |
|:----------------:|:-------------------:|:-------------------:|:-------------------:|
| cryptography | [empty-aes-key](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.empty-aes-key.empty-aes-key) | High | [SM-1](./cryptography/empty-aes-key.md) |
| cryptography | [insecure-cipher-algorithm-arc4](https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.insecure-cipher-algorithms-arc4.insecure-cipher-algorithm-arc4) | Medium | [SM-3](./cryptography/insecure-cipher-algorithm-arc4.md) |


