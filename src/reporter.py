# Format into XML/JSON

import json
import xml.etree.ElementTree as ET

def to_json(df, out_path):
    df.to_json(out_path, orient="records", indent=4)

def to_xml(df, out_path):
    root = ET.Element("trades")
    for _, row in df.iterrows():
        trade = ET.SubElement(root, "trade")
        for col, val in row.items():
            ET.SubElement(trade, col).text = str(val)
    tree = ET.ElementTree(root)
    tree.write(out_path)
