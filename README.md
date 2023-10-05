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
| Category | Rule ID | Patterns | Our Strategies | Tag |
| --- | --- | --- | --- | --- |
| cryptography  | empty-aes-key | https://semgrep.dev/orgs/nwpu/editor/r/python.cryptography.security.empty-aes-key.empty-aes-key | cipher = AES.new("freeCodeCamp"[0:0] , AES.MODE_CFB, iv) | String Matching |
| 行2列1 | 行2列2 | 行2列3 | 行2列4 | 行2列5 |
| 行3列1 | 行3列2 | 行3列3 | 行3列4 | 行3列5 |

