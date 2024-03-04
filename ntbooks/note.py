from pyautogui import click, displayMousePosition, typewrite, moveTo, press, write
import pandas as pd
import time
import subprocess
 

df = pd.read_parquet("../data/task.parquet")
print(df.head())
print(df.loc[0])
print(len(df))
subprocess.Popen('obsidian', shell=True)
time.sleep(5)

for i in range(37,100):

    # X 146 Y 95 New Note Click
    click(x=146,y=95)
    # Press Del
    press('Del')
    time.sleep(.5)
    write(df.loc[i].day)
    time.sleep(.5)
    press('Enter')
    time.sleep(.5)
    press('Enter')
    
    if df.loc[i].task != None:    
        write('#### Task')
        time.sleep(1)
        press('Enter')
        time.sleep(.5)
        write(df.loc[i].task)
        time.sleep(1)
        press('Enter')
        time.sleep(.5)
        # if note is null
    if df.loc[i].notes != None:
        write('#### Note')
        time.sleep(1)
        press('Enter')
        time.sleep(.5)
        write(df.loc[i].notes)
        time.sleep(1)
        press('Enter')
    if df.loc[i].LinkA != None:
        write('#### Link')
        time.sleep(1)
        press('Enter')
        time.sleep(.5)
        write(df.loc[i].LinkA)
        time.sleep(1)
        press('Enter')
        
    if df.loc[i].LinkB != None:
        press('Enter')
        time.sleep(.5)
        write(df.loc[i].LinkB)
        time.sleep(1)
        press('Enter')
        
    if df.loc[i].LinkC != None:
        press('Enter')
        time.sleep(.5)
        write(df.loc[i].LinkC)
        time.sleep(1)
    if df.loc[i].LinkD != None:
        press('Enter')
        time.sleep(.5)
        write(df.loc[i].LinkD)
        time.sleep(1)        
    press('Enter')
    
    write('[[' + df.loc[i].category + ']]')
    time.sleep(.5)
    press('Enter')
    
    if i > 0:
        write('[[' + df.loc[i-1].day + ']]')
    time.sleep(.5)
    
# # Start Filling
# # Day -> Press Enter _-> Fill Task _> Press Enter > Fill notes > Press ENter > Fill category inside [[]] > Fill day before inside [[]]
# displayMousePosition()