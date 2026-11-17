{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8d575508-957b-4c82-9d34-68ee28114e78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Orignal List: ['Arya', 'Riya', 'Sarah']\n",
      "After Add: ['Arya', 'Riya', 'Sarah', 'Nidhi']\n",
      "After Insert: ['Arya', 'Diya', 'Riya', 'Sarah', 'Nidhi']\n",
      "After Update: ['Arya', 'Ipshita', 'Riya', 'Sarah', 'Nidhi']\n",
      "After Delete: ['Arya', 'Ipshita', 'Sarah', 'Nidhi']\n"
     ]
    }
   ],
   "source": [
    "#Operations on LIST\n",
    "students = [\"Arya\", \"Riya\", \"Sarah\"]\n",
    "print(f\"Orignal List: {students}\")\n",
    "#Add\n",
    "students.append(\"Nidhi\")\n",
    "print(f\"After Add: {students}\")\n",
    "\n",
    "students.insert(1,\"Diya\")\n",
    "print(f\"After Insert: {students}\")\n",
    "\n",
    "#Update\n",
    "students[1] = \"Ipshita\"\n",
    "print(f\"After Update: {students}\")\n",
    "\n",
    "#Delete\n",
    "students.remove(\"Riya\")\n",
    "print(f\"After Delete: {students}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "0d2ee9d5-42e5-439c-b50a-349c9011320a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Orginal Tuple: ('Orange', 'Apple', 'Banana', 'Litchi')\n",
      "Banana\n",
      "('Orange', 'Apple')\n",
      "After Add: ('Orange', 'Apple', 'Banana', 'Litchi', 'Watermelon')\n",
      "['Orange', 'Apple', 'Banana', 'Litchi', 'Watermelon', 'Pear']\n",
      "['Orange', 'Apple', 'Mango', 'Banana', 'Litchi', 'Watermelon', 'Pear']\n",
      "After Update: ('Orange', 'Cabbage', 'Potato', 'Banana', 'Litchi', 'Watermelon')\n",
      "After Delete: ('Orange', 'Banana', 'Litchi', 'Watermelon')\n",
      "['Orange', 'Apple', 'Banana', 'Litchi', 'Watermelon']\n",
      "('Orange', 'Apple', 'Banana', 'Litchi', 'Watermelon')\n",
      "5\n",
      "1\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "#Operations on TUPlE\n",
    "fruits = (\"Orange\", \"Apple\", \"Banana\", \"Litchi\")\n",
    "print(f\"Orginal Tuple: {fruits}\")\n",
    "\n",
    "#Accessing elements\n",
    "print(fruits[2])\n",
    "#Slicing\n",
    "print(fruits[0:2])\n",
    "\n",
    "#Add using concatenation\n",
    "w = (\"Watermelon\",)\n",
    "fruits += w\n",
    "print(f\"After Add: {fruits}\")\n",
    "\n",
    "#Add by conerting to list\n",
    "y = list(fruits)\n",
    "y.append(\"Pear\")\n",
    "print(y)\n",
    "\n",
    "y.insert(2,\"Mango\")\n",
    "print(y)\n",
    "\n",
    "#Update by creating a new tuple\n",
    "vegetables = (\"Cabbage\", \"Potato\")\n",
    "fruits = fruits[:1] + vegetables + fruits[2:]\n",
    "print(f\"After Update: {fruits}\")\n",
    "\n",
    "#Delete by creating new tuple\n",
    "fruits = fruits[:1] + fruits[3:]\n",
    "print(f\"After Delete: {fruits}\")\n",
    "\n",
    "y.pop(2)\n",
    "y.pop(5)\n",
    "print(y)\n",
    "fruits = tuple(y)\n",
    "print(fruits)\n",
    "\n",
    "#Length, Count, Index\n",
    "print(len(fruits))\n",
    "print(fruits.count(\"Banana\"))\n",
    "print(fruits.index(\"Litchi\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "58094f3e-1cc6-4724-ae4a-9004b19c3fec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Dictionary: {'Aarav': 80, 'Isha': 90, 'Rahul': 50, 'Sneha': 100}\n",
      "After Add: {'Aarav': 80, 'Isha': 90, 'Rahul': 50, 'Sneha': 100, 'Ipshita': 100}\n",
      "After Update: {'Aarav': 80, 'Isha': 90, 'Rahul': 60, 'Sneha': 100, 'Ipshita': 100}\n",
      "After Delete: {'Aarav': 80, 'Rahul': 60, 'Sneha': 100, 'Ipshita': 100}\n",
      "{'Aarav': 80, 'Rahul': 60, 'Sneha': 100}\n"
     ]
    }
   ],
   "source": [
    "#Operations on DICTIONARY\n",
    "students_marks = {\"Aarav\": 80, \"Isha\": 90, \"Rahul\": 50, \"Sneha\": 100}\n",
    "print(f\"Original Dictionary: {students_marks}\")\n",
    "\n",
    "#Add\n",
    "students_marks[\"Ipshita\"] = 100\n",
    "print(f\"After Add: {students_marks}\")\n",
    "\n",
    "#Update\n",
    "students_marks[\"Rahul\"] = 60\n",
    "print(f\"After Update: {students_marks}\")\n",
    "\n",
    "#Delete\n",
    "del students_marks[\"Isha\"]\n",
    "print(f\"After Delete: {students_marks}\")\n",
    "\n",
    "students_marks.popitem()\n",
    "print(students_marks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31473b1e-3e0a-4fe0-b74b-2730d2e4feb4",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
