# Open Functions
**Extend LLMs like Mistral and Llama with advanced function calling capabilities.**

Open Functions transforms a regular LLM that was not pre-trained for function calling and extends it with function calling capabilities. these models to call and execute functions, Open Functions transforms LLMs into powerful, interactive tools capable of completing complex tasks and generating structured outputs. Whether you're aiming to streamline data analysis, automate content creation, or develop innovative AI-driven solutions, Open Functions provide the key to unlocking the full potential of open-source LLMs, ensuring reliable performance.

## How it works
You can define any function structure. OpenFunctions will follow it and make sure the LLM always outputs the correct output and structure. 
## Examples
### Input
It's 23.4 C Degrees in Innsbruck.
### Output
Function: *get_weather()*
```
{
  "city": "Innsbruck",
  "temperature": "23.4",
  "unit": "celsius",
  "timestamp": "192848923"
}
```
### Input
Create a Python script that shows the current time.
### Output
Function: *run_python()*
```
{
  "python_code": "import time\n print(time)",
  "python_executor": "python3.10",
  "python_output": "json", "text"
}
```
### Input
How are you?
### Output
No Function provided, regular LLM response will be outputted.
```
{
  "response": "I'm doing great, how are you?",
  "function_call": "none",
}
```
