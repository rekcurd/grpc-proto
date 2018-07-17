# drucker-grpc-proto
Drucker grpc protocol.

## Parent Project
https://github.com/drucker/drucker-parent

## Input/Output
TODO: Generate automatically from `drucker.proto`

*V* is the length of feature vector. *M* is the number of classes. If your algorithm is a binary classifier, you set *M* to 1. If your algorithm is a multi-class classifier, you set *M* to the number of classes.

|input: data |input: option |output: label |output: score |output: option |
|:---|:---|:---|:---|:---|
|string |json |string |double |json |
|string |json |bytes |double |json |
|string |json |int[*M*] |double[*M*] |json |
|string |json |double[*M*] |double[*M*] |json |
|string |json |string[*M*] |double[*M*] |json |
|bytes |json |string |double |json |
|bytes |json |bytes |double |json |
|bytes |json |int[*M*] |double[*M*] |json |
|bytes |json |double[*M*] |double[*M*] |json |
|bytes |json |string[*M*] |double[*M*] |json |
|int[*V*] |json |string |double |json |
|int[*V*] |json |bytes |double |json |
|int[*V*] |json |int[*M*] |double[*M*] |json |
|int[*V*] |json |double[*M*] |double[*M*] |json |
|int[*V*] |json |string[*M*] |double[*M*] |json |
|double[*V*] |json |string |double |json |
|double[*V*] |json |bytes |double |json |
|double[*V*] |json |int[*M*] |double[*M*] |json |
|double[*V*] |json |double[*M*] |double[*M*] |json |
|double[*V*] |json |string[*M*] |double[*M*] |json |
|string[*V*] |json |string |double |json |
|string[*V*] |json |bytes |double |json |
|string[*V*] |json |int[*M*] |double[*M*] |json |
|string[*V*] |json |double[*M*] |double[*M*] |json |
|string[*V*] |json |string[*M*] |double[*M*] |json |

The input "option" field needs to be a json format. Below are our reserved fields.

|Field |Type |Description |
|:---|:---|:---|
|suppress_log_input |bool |True: NOT print the input and output to the log message. <BR>False (default): Print the input and output to the log message.