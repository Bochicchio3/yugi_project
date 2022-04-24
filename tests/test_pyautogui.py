

# %%
import pyautogui

#%%
 

 

print (pyautogui.position())
# %%

# %%

# %%

# %%

#%%

pyautogui.click(1718,262)
#%%
hand_6_cards = []
#%%
hand_6_cards.append(pyautogui.position())

# %%
hand_5_cards = []

#%%
hand_5_cards.append(pyautogui.position())
# %%
hand_4_cards = []
#%%
hand_4_cards.append(pyautogui.position())

#%%
hand_3_cards = []
#%%
hand_3_cards.append(pyautogui.position())
#%%
hand_2_cards = []
#%%
hand_2_cards.append(pyautogui.position())
#%%
hand_1_cards = []
#%%
hand_1_cards.append(pyautogui.position())



#%%
import json
# %%
positions = [hand_6_cards, hand_5_cards, hand_4_cards, hand_3_cards, hand_2_cards, hand_1_cards]

#%%

data = { idx:p for idx,p in enumerate(positions) }




#%%
json_string = json.dumps(data)
print(json_string)
# %%


with open('hand_click_positions.json', 'w') as outfile:
    json.dump(json_string, outfile)
# %%


with open('hand_click_positions.json') as json_file:
    data = json.load(json_file)
    python_dictionary = json.loads(data)
    print(python_dictionary)
    print(data)
# %%
data[0]
# %%
python_dictionary['0']
# %%
