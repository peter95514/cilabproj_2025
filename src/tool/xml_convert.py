import os
import xml.etree.ElementTree as ET

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


xml_folder = os.path.join(root, "data/xml_temp")
png_folder = os.path.join(root, "data/temp")
output_folder = os.path.join(root, "data/output_temp")

os.makedirs(output_folder, exist_ok = True)

# 建立 xml 檔名集合（不含副檔名）
xml_basenames = {
    os.path.splitext(f)[0]
    for f in os.listdir(xml_folder)
    if f.lower().endswith(".xml")
}

def convert_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    objects = []

    for obj in root.findall(".//object"):

        

        bbox = obj.find("bndbox")
        xmin = float(bbox.find("xmin").text)
        ymin = float(bbox.find("ymin").text)
        xmax = float(bbox.find("xmax").text)
        ymax = float(bbox.find("ymax").text)

        # Convert to YOLO format
        x_center = ((xmin + xmax) / 2) / 512
        y_center = ((ymin + ymax) / 2) / 512
        box_width = (xmax - xmin) / 512
        box_height = (ymax - ymin) / 512

        # 假設只有一個類別 class=0
        objects.append(f"1 {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}")
    
    return objects

def run():
    count = 0
    for file in sorted(os.listdir(png_folder)):
        if file.lower().endswith(".png"):
            base = os.path.splitext(file)[0]
            print([base]+[count])
            count += 1
            if base not in xml_basenames:
                temp_obj = []
                temp_obj.append(f"0 0 0 0 0")
                txt_path = os.path.join(output_folder, base + ".txt")
                with open(txt_path, "w") as f:
                    for line in temp_obj:
                        f.write(line + "\n")
            else:
                txt_path = os.path.join(output_folder, base + ".txt")
                label = convert_xml(os.path.join(xml_folder, base + ".xml"))
                with open(txt_path, "w") as f:
                    for line in label:
                        f.write(line + "\n")
                        
run()
