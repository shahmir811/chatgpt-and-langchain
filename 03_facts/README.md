# Facts

We have an attached plain text file called `facts.txt` that contains a ton of very distinct little pieces of information inside of this file. I'm going to build a very simple program that allows a user to ask kind of basic questions. And I'm going to use the contents of that file to answer the user's questions.

`For example,` if a user asks us what is an interesting fact about the English language, I'm going to want to somehow open up that facts.txt file, find all the different facts inside there, and find
the one fact most relevant to the user's question, which in this case might be **"Dreamt" is the only English word that ends with the letters "mt."**

At the end, we will take the user's question, and the most relevant fact, and pass it as a prompt to our language model (ChatGPT)

### Usage

At the root of the folder, replace file `.env-example` with name `.env` and add the openAI key:

```OPENAI_API_KEY=```


### Run the program

In order to run a program you have to type the `language` and `task` flags, 
else it will use the default flags

```python main.py```

