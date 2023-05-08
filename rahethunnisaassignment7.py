# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:59:29 2023

@author: hp
"""

def Credit_Card_Offer(salary,Credit_limit):
    if salary<10000:
        Credit_limit=salary*.10
    elif  salary>=10000 and salary<=30000:
        Credit_limit=salary*.20
    elif salary>30000:
        Credit_limit=salary*.30
    return Credit_limit
Credit_Card_Offer(35000,0)

def DMart_Discount_Offer(purchase_amount,discount):
    if purchase_amount<20000:
        discount=0.2
    elif purchase_amount>=20000 and purchase_amount<=40000:
        discount=0.3
    elif purchase_amount>50000:
        discount=0.4
    return discount
DMart_Discount_Offer(52000,0)
def Amazon_Online_Offer(product_type,discount):
    if product_type=="electornic":
        discount=0.2
    elif product_type=="cloth":
        discount=0.3
    elif product_type=="footware":
        discount=0.4
    return discount
Amazon_Online_Offer("cloth",1)
