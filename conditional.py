cats = ["Goon", "Tsuki", "Simee" ]
# cats2 = ["Goon", "Tsuki", "Simee" ]

# good_cats = ["Tsuki"]

def edit_list(param, name):
    for cat in param:
        if cat == name:
            param.remove(cat)
            return param
        else:
            param.append("pumpkin")
            return param

        
result = edit_list(cats, "pumpkin")
# result2 = edit_list(cats2, "Tiger")
        
print(result)
# print(result2)
