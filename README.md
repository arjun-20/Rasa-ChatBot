

#Basic Mathematical Operations Chatbot
This is a simple chatbot that can perform basic mathematical operations such as addition, subtraction, multiplication, and division. The chatbot is built using RASA, an open-source framework for building conversational AI assistants.

Installation
Clone this repository: git clone https://github.com/your_username/basic-math-chatbot.git
Install the required dependencies: pip install -r requirements.txt
Usage
Train the NLU model: rasa train nlu
Train the dialogue model: rasa train
Start the chatbot server: rasa run actions & rasa shell
The above commands will train the NLU and dialogue models, and start the chatbot server. You can then interact with the chatbot using the RASA shell.

Functionality
The chatbot can perform the following functions:

Addition: Add two numbers together. For example, "Add 3 and 5".
Subtraction: Subtract one number from another. For example, "Subtract 5 from 10".
Multiplication: Multiply two numbers together. For example, "Multiply 2 by 6".
Division: Divide one number by another. For example, "Divide 10 by 2".
You can also ask the chatbot to display the available mathematical operations by saying "What operations can you perform?".
