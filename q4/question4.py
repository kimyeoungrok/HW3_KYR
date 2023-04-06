{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b99c9d10",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    print(factorial(0))\n",
    "    print(factorial(2))\n",
    "    print(factorial(4))\n",
    "    print(factorial(6))\n",
    "    print(factorial(8))\n",
    "    print(factorial(10))\n",
    "    print(factorial(12))\n",
    "    print(factorial(14))\n",
    "def factorial(num):\n",
    "    if num == 1 or num==0:\n",
    "        return 1\n",
    "    else:\n",
    "        return num*factorial(num-1)\n",
    "\n",
    "    \n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
