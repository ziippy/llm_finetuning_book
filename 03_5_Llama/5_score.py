import json 
from glob import glob 

path = "./qa_evaluation_results"

path_list = glob(f"{path}/*")

calculated_average_list = [] 
model_average_score = [] 
for path in path_list:
    with open(path, "r") as file:
        data = json.load(file)
    
    data = data["choices"][0]["message"]["parsed"]
    scores = [item['score'] for item in data.values() if isinstance(item, dict)]
    calculated_average = sum(scores) / len(scores)
    calculated_average_list.append(calculated_average)
    model_average_score.append(data["average_score"])

mean_calculated_average= sum(calculated_average_list) / len(calculated_average_list)
mean_model_average_score = sum(model_average_score) / len(model_average_score)
# mean_calculated_average, mean_model_average_score

print("mean_calculated_average: " + str(mean_calculated_average))
print("mean_model_average_score: " + str(mean_model_average_score))
