import json

with open('json_colors.json', 'r') as file:
    colors_data = json.load(file)

for item in colors_data['colors']:
    if 'category' in item:
        del item['category']
    if 'type' in item:
        del item['type']

    rgba = item['code']['rgba']
    rgb = f"{rgba[0]}, {rgba[1]}, {rgba[2]}"
    item['rgb'] = rgb

    hex = item['code']['hex']
    item['hex'] = hex

    del item['code']['rgba']
    del item['code']

new_json = json.dumps(colors_data, indent=2)
json_object = json.loads(new_json)

with open('Task1_completed.json', 'w') as file:
    json.dump(json_object, file, indent=2)
