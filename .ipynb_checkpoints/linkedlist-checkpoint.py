{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "17196735",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "30\n",
      "40\n",
      "50\n",
      "\n",
      "10\n",
      "20\n",
      "30\n",
      "50\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    data=None\n",
    "    address=None\n",
    "    def __init__(self,value):\n",
    "        self.data=value\n",
    "        \n",
    "#ob=Node(100)\n",
    "#print(ob.data)\n",
    "        \n",
    "class LinkedList:\n",
    "    def addElement(self,head,value):\n",
    "        new_node=Node(value)\n",
    "        #print(new_node)\n",
    "        cur=head\n",
    "        while cur.address !=None:\n",
    "            cur=cur.address\n",
    "        cur.address=new_node\n",
    "    def print_list(self,head):\n",
    "        cur=head\n",
    "        while cur!=None:\n",
    "            print(cur.data)\n",
    "            cur=cur.address\n",
    "    def removeElement(self,head,value):\n",
    "        cur=head\n",
    "        prev=None\n",
    "        while cur.data!=value:\n",
    "            prev=cur\n",
    "            cur=cur.address\n",
    "        prev.address=cur.address\n",
    "        \n",
    "\n",
    "ob=LinkedList()\n",
    "head=Node(10)\n",
    "ob.addElement(head,20)\n",
    "ob.addElement(head,30)\n",
    "ob.addElement(head,40)\n",
    "ob.addElement(head,50)\n",
    "ob.print_list(head)\n",
    "print()\n",
    "ob.removeElement(head,40)\n",
    "ob.print_list(head)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "146d256f",
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
   "version": "3.10.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
