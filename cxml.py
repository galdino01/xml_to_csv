import pandas as pd
import xml.etree.ElementTree as xet
import re
from post import Post  

def xml_to_csv(xml_path=str, csv_name=str, fields=str|list[str], show_process=False) -> None:
    cols = fields
    rows = []
    index = 0
    remove_str = "wp-content/uploads/"
    
    xmlparse = xet.parse(xml_path)
    root = xmlparse.getroot()
    
    for i in root:
        elements = i.findall("item")
        
        for el in elements:
            title =  "Vazio" if el.find("title") else el.find("title").text.replace("[:pt]", "").replace("[:]", "")
            author = "Vazio" if el.find("dc:creator") else el.find("dc:creator")
            img = "Vazio" if el.find("guid") else re.sub(r'[0-90-90-90-9]+/[0-90-9]+/', '', el.find("guid").text).replace(remove_str, 'images/').lower()
            slug = "Vazio" if el.find("title") else el.find("title").text.replace("[:pt]", "").replace("[:]", "").replace(" ", "-").replace("_", "-").lower()
            content = "Vazio" if el.find("content:encoded") else el.find("content:encoded")
            excerpt = "Vazio" if el.find("excerpt:encoded") else el.find("excerpt:encoded")
            link = "Vazio" if el.find("link") else re.sub(r'[0-90-90-90-9]+/[0-90-9]+/', '', el.find("link").text).lower()
            categories = [c.text for c in el.findall("category")]
        
            post = Post(index, title, author, img, slug, content, excerpt, categories, link)
            rows.append(post.__dict__)
            
            print(post) if (show_process) else None
            
            index += 1
        
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(csv_name)