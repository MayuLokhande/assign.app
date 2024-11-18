import json

file_path = r"C:\Users\mayur\assignmentdd\algoparams_from_ui.json"



try:
    with open(file_path, 'r') as file:
        data = json.load(file)  

  
    target_info = data["Target"] 
    prediction_type = target_info["prediction type"]  
    target = target_info["target"] 
    partitioning = target_info.get("partitioning", False) 
    
    if prediction_type == "Regression" and target:
        print("Target:", target)
        print("Prediction Type:", prediction_type)
        print("Partitioning:", partitioning)
    else:
        print("The JSON does not have the right information.")
except:
    print("Error reading the file. Make sure the file exists and has correct JSON.")
