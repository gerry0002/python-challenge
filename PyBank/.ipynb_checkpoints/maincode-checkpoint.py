{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import libraries\n",
    "import os\n",
    "import csv\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create data frame \n",
    "csv_path = os.path.join('Resources', 'week-3-python_homework_PyBank_Resources_budget_data.csv')\n",
    "\n",
    "bank_df = pd.read_csv(csv_path, low_memory=False)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "#calculating results\n",
    "\n",
    "tot_months=bank_df[\"Date\"].count()\n",
    "total=bank_df[\"Profit/Losses\"].sum()\n",
    "start_price = bank_df.iloc[0,1]\n",
    "end_price = bank_df.iloc[tot_months-1,1]\n",
    "avg_price = (end_price-start_price)/(tot_months-1)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sep-2013'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Looping through the data\n",
    "dec = 0.00\n",
    "inc= 0.00\n",
    "\n",
    "for i in range(tot_months):\n",
    "    diff =  bank_df.iloc[i,1] - bank_df.iloc[i-1,1]\n",
    "    if diff <= dec:\n",
    "        dec=diff\n",
    "        month_dec = bank_df.iloc[i,0]\n",
    "    if diff>= inc:\n",
    "        inc=diff\n",
    "        month_inc = bank_df.iloc[i,0]\n",
    "month_dec     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#printing top line\n",
    "\n",
    "print(\"Financial Analysis \")\n",
    "print(\"****************************\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.1176470588234 \n",
      "Greatest Increase in Profits: (Feb-2012) $1926159 \n",
      "Greatest Decrease in Profits: (Sep-2013) $-2196167 \n"
     ]
    }
   ],
   "source": [
    "#printing results\n",
    "print(f\"Total Months: {tot_months}\")\n",
    "print(f\"Total: ${total}\")\n",
    "print(f\"Average Change: ${avg_price} \")\n",
    "print(f\"Greatest Increase in Profits: ({month_inc}) ${inc} \")\n",
    "print(f\"Greatest Decrease in Profits: ({month_dec}) ${dec} \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
