{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "467bfe56",
   "metadata": {},
   "source": [
    "# Basic functions in python and revision along with example usages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7173aef",
   "metadata": {},
   "outputs": [],
   "source": [
    "# input and output basic Statements\n",
    "name = input(\"Enter your name: \")\n",
    "print(\"Hello, \" + name + \"!\")\n",
    "\n",
    "# Print function with keyword arguments\n",
    "print(\"Python\", \"is\", \"fun\", sep=\"-\", end=\"!\\n\")\n",
    "# this is the example usage\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e1ba4c43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'> <class 'int'> <class 'float'> <class 'complex'>\n"
     ]
    }
   ],
   "source": [
    "# Data Types\n",
    "string_example = \"Hello, World!\"  # str\n",
    "integer_example = 42  # int\n",
    "float_example = 3.14159  # float\n",
    "complex_example = 1 + 2j  # complex\n",
    "\n",
    "print(type(string_example), type(integer_example), type(float_example), type(complex_example))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5dcb3338",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15 2.0 100000\n",
      "<class 'str'> <class 'int'>\n"
     ]
    }
   ],
   "source": [
    "# Expressions and Operators\n",
    "a = 10\n",
    "b = 5\n",
    "addition = a + b\n",
    "division = a / b\n",
    "power = a ** b\n",
    "\n",
    "print(addition, division, power)\n",
    "\n",
    "# Type Casting\n",
    "num_str = \"100\"\n",
    "num_int = int(num_str)\n",
    "print(type(num_str), type(num_int))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e7d06635",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age: ciehfjbc\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'ciehfjbc'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Input \u001b[1;32mIn [4]\u001b[0m, in \u001b[0;36m<cell line: 2>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# Conditional Statements\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m age \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mint\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mEnter your age: \u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m age \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m18\u001b[39m:\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mYou are an adult.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'ciehfjbc'"
     ]
    }
   ],
   "source": [
    "# Conditional Statements\n",
    "age = int(input(\"Enter your age: \"))\n",
    "if age >= 18:\n",
    "    print(\"You are an adult.\")\n",
    "else:\n",
    "    print(\"You are a minor.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "781d06e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Looping Statements\n",
    "# For loop\n",
    "for i in range(5):\n",
    "    print(i)\n",
    "\n",
    "# While loop\n",
    "count = 0\n",
    "while count < 5:\n",
    "    print(count)\n",
    "    count += 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "926f88db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "# Jumping Statements\n",
    "for i in range(10):\n",
    "    if i == 5:\n",
    "        break\n",
    "    if i % 2 == 0:\n",
    "        continue\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f2f135fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length: 5\n",
      "ID: 2801005136256\n",
      "Type: <class 'list'>\n",
      "1\n",
      "3\n",
      "5\n",
      "7\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "# Special Functions\n",
    "sample_list = [1, 2, 3, 4, 5]\n",
    "print(\"Length:\", len(sample_list))\n",
    "print(\"ID:\", id(sample_list))\n",
    "print(\"Type:\", type(sample_list))\n",
    "\n",
    "# Range function\n",
    "for i in range(1, 10, 2):\n",
    "    print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f6b703ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Alice!\n",
      "25\n",
      "Squares: [1, 4, 9, 16, 25]\n",
      "Product: 120\n",
      "Evens: [2, 4]\n",
      "I have been modified\n",
      "I have been modified\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "def greet(name):\n",
    "    return f\"Hello, {name}!\"\n",
    "\n",
    "print(greet(\"Alice\"))\n",
    "\n",
    "# Lambda Function\n",
    "square = lambda x: x ** 2\n",
    "print(square(5))\n",
    "\n",
    "# map, reduce and filter Functions\n",
    "from functools import reduce\n",
    "\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "# Map function\n",
    "squares = list(map(lambda x: x ** 2, numbers))\n",
    "print(\"Squares:\", squares)\n",
    "\n",
    "# Reduce function\n",
    "product = reduce(lambda x, y: x * y, numbers)\n",
    "print(\"Product:\", product)\n",
    "\n",
    "# Filter function\n",
    "evens = list(filter(lambda x: x % 2 == 0, numbers))\n",
    "print(\"Evens:\", evens)\n",
    "\n",
    "# Global Keyword\n",
    "global_var = \"I am global\"\n",
    "\n",
    "def use_global():\n",
    "    global global_var\n",
    "    global_var = \"I have been modified\"\n",
    "    print(global_var)\n",
    "\n",
    "use_global()\n",
    "print(global_var)\n",
    "\n",
    "# Return Keyword\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "\n",
    "result = add(3, 4)\n",
    "print(result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "449ed582",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "153.93791\n"
     ]
    }
   ],
   "source": [
    "def calculate_area(shape, dimensions):\n",
    "    if shape == \"rectangle\":\n",
    "        length, width = dimensions\n",
    "        return length * width\n",
    "    elif shape == \"circle\":\n",
    "        radius, = dimensions\n",
    "        return 3.14159 * (radius ** 2)\n",
    "    else:\n",
    "        return \"Shape not supported\"\n",
    "\n",
    "# Example usage:\n",
    "print(calculate_area(\"rectangle\", (5, 10)))  # Output: 50\n",
    "print(calculate_area(\"circle\", (7,)))        # Output: 153.93791\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2d82cd96",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "world Hello\n"
     ]
    }
   ],
   "source": [
    "def reverse_words(text):\n",
    "    words = text.split()\n",
    "    reversed_words = words[::-1]\n",
    "    return ' '.join(reversed_words)\n",
    "\n",
    "# Example usage:\n",
    "print(reverse_words(\"Hello world \")) \n",
    "# Output: \"world Hello\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "73da8c72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'min': 10, 'max': 50, 'average': 30.0}\n"
     ]
    }
   ],
   "source": [
    "def analyze_list(numbers):\n",
    "    stats = {\n",
    "        \"min\": min(numbers),\n",
    "        \"max\": max(numbers),\n",
    "        \"average\": sum(numbers) / len(numbers)\n",
    "    }\n",
    "    return stats\n",
    "\n",
    "# Example usage:\n",
    "print(analyze_list([10, 20, 30, 40, 50]))  # Output: {'min': 10, 'max': 50, 'average': 30.0}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "133a1b7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['pear', 'kiwi']\n"
     ]
    }
   ],
   "source": [
    "def filter_short_names(names, max_length):\n",
    "    return list(filter(lambda name: len(name) < max_length, names))\n",
    "\n",
    "# Example usage:\n",
    "product_names = [\"apple\", \"banana\", \"pear\", \"kiwi\", \"grape\"]\n",
    "print(filter_short_names(product_names, 5))  # Output: ['pear', 'kiwi']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a8723893",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'word_count': 9, 'char_count': 40, 'most_frequent_word': 'hello'}\n"
     ]
    }
   ],
   "source": [
    "def analyze_text(text):\n",
    "    words = text.split()\n",
    "    word_count = len(words)\n",
    "    char_count = sum(len(word) for word in words)\n",
    "    \n",
    "    word_frequency = {}\n",
    "    for word in words:\n",
    "        word_lower = word.lower()\n",
    "        if word_lower in word_frequency:\n",
    "            word_frequency[word_lower] += 1\n",
    "        else:\n",
    "            word_frequency[word_lower] = 1\n",
    "    \n",
    "    most_frequent_word = max(word_frequency, key=word_frequency.get)\n",
    "    \n",
    "    return {\n",
    "        \"word_count\": word_count,\n",
    "        \"char_count\": char_count,\n",
    "        \"most_frequent_word\": most_frequent_word\n",
    "    }\n",
    "\n",
    "# Example usage:\n",
    "text = \"Hello world! This is a test. Hello again, world!\"\n",
    "print(analyze_text(text))  \n",
    "# Output: {'word_count': 8, 'char_count': 32, 'most_frequent_word': 'hello'}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4ca9c46",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
