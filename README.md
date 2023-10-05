# Semgrep Rules And Our Evasive Strategies
## Our Motivation
[**Semgrep**](https://semgrep.dev/) is a fast, open source static analysis tool for finding bugs, detecting vulnerabilities. Different from traditional tools using regex to detecting secrets, Semgrep is more powerful. Its rule repository covers different programming languages. You can input the code snippets and scan them.

But based on some easy transformation on the vulnerable snippets, we can evade the analysis. So our work mainly focuses on proposing some kinds of strategies to evade the tool successfully with the code snippets vulnewrable. Note that we choose _**Python**_ part as our target.

## Program Analysis
- String Matching
- Constant Analysis
- Dataflow Analysis
- Taint Analysis

## Evasive Strategies

