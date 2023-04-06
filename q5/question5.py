{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "be6cd037",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth\n",
      "\n",
      "\n",
      "undergrowth the in bent it where To could I as far as one down looked And stood I long traveler, one be And both travel not could I sorry And wood, yellow a in diverged roads \n",
      "\n",
      "\n",
      " Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,\n",
      "\n",
      "\n",
      "same, the about really them worn Had there passing the that for as Though wear; wanted and grassy was it Because claim, better the perhaps having And fair, as just as other, the took Then \n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    string1 = \"Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth\"\n",
    "    string2 = \" Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,\"\n",
    "    print(string1)\n",
    "    print(\"\\n\")\n",
    "    reverse_words(string1)\n",
    "    print(\"\\n\")\n",
    "    print(string2)\n",
    "    print(\"\\n\")\n",
    "    reverse_words(string2)\n",
    "def reverse_words(string):\n",
    "    str_list = string.split(\" \")\n",
    "    string3 = \"\"\n",
    "    for i in range(len(str_list)-1, 0, -1):\n",
    "        string3 += str_list[i]\n",
    "        string3 += \" \"\n",
    "    print(string3)\n",
    "\n",
    "if __name__ == '__main__' :\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae0c80fe",
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
